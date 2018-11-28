#include<iostream>

using namespace std;

double Nao[1001];
double Ken[1001];
int N;
int NumBlocks;

void bubble_sortNao(){
	
	double max;
	int last = N;
	for(int j = 0; j < N ;j++){
		
		for(int i = 0; i < last-1; i++){
			if(Nao[i]>Nao[i+1]){
				//swap	
				double temp = Nao[i];
				Nao[i] = Nao[i+1];
				Nao[i+1] = temp;
			}
		}
		last--;
	}
}


void bubble_sortKen(){
	
	double max;
	int last = N;
	for(int j = 0; j < N ;j++){
		
		for(int i = 0; i < last-1; i++){
			if(Ken[i]>Ken[i+1]){
				//swap	
				double temp = Ken[i];
				Ken[i] = Ken[i+1];
				Ken[i+1] = temp;
			}
		}
		last--;
	}
}

void printKen(){
	
	cout<<"\n Printing Ken \n";
	for(int j = 0; j < NumBlocks; j++){
		cout<<Ken[j]<<" ";
	}
}

void printNao(){
	
	cout<<"\n Printing Nao \n";
	for(int j = 0; j < NumBlocks; j++){
		cout<<Nao[j]<<" ";
	}
}

double getSmallestNao(){
	return Nao[0];
}

double getSmallestKen(){
	return Ken[0];
}

double getLargestNao(){
	return Nao[N-1];
}

double getLargestKen(){
	return Ken[N-1];
}

double getSmallestKenGreaterThanNao(double d){

	for(int j = 0; j < N; j++){
		if(d < Ken[j])
			return Ken[j];
	}
	//not present return 0(d is greater than Ken[])
	return 0.0;
}

void deleteFromNao(double d){

	int flag = 0;
	
	for(int j = 0; j < NumBlocks; j++){
		
		if(d == Nao[j]){
			flag = 1;
			//put d at the end
			Nao[NumBlocks] = d;
			
		}
		if(flag == 1 && j != NumBlocks){
			//move j+1 to j
			Nao[j] = Nao[j+1];
		}
	}
	
}

void deleteFromKen(double d){

	int flag = 0;
	
	for(int j = 0; j < NumBlocks; j++){
		
		if(d == Ken[j]){
			flag = 1;
			Ken[NumBlocks] = d;
		}
		if(flag == 1 && j != NumBlocks){
			//move j+1 to j
			Ken[j] = Ken[j+1];
		}
	}
	
}

int presentInKen(double d){
	
	for(int j = 0; j < NumBlocks; j++){
		if(d == Ken[j]){
			return 1;
		}
	}
	return 0;
}


int main()
{
	int numTestCases; 
	int winD_War = 0;
	int winWar;
	cin>>numTestCases;
	
	for(int i = 0; i < numTestCases; i++){
		
		cin>>NumBlocks;
		N = NumBlocks;
		for(int j = 0; j < N; j++){
			cin>>Nao[j];
		}
		
		for(int j = 0; j < N; j++){
			cin>>Ken[j];
		}
		
		bubble_sortKen();
		bubble_sortNao();
		
		winD_War = 0;
		double incr = 0.0000001;
		double decr = 0.0000001;
		//DecietfulWar
		while(N > 0){
			if(getSmallestKen() > getSmallestNao()){
				//Naomi cannot win, so tries to make Ken use largest possible
				double max_Ken = getLargestKen();
				while(presentInKen(max_Ken - decr)){
					decr = decr + 0.0000001;
				}
				double Nao_Told = max_Ken - decr;
				//Naomi plays with its min
				deleteFromKen(getSmallestKenGreaterThanNao(Nao_Told));
				deleteFromNao(getSmallestNao());
			}
			else{
				double max_Ken = getLargestKen();
				double min_Nao = getSmallestNao();
				while(presentInKen(max_Ken + incr)){
					incr = incr + 0.0000001;
				}
				
				if((max_Ken + incr) >= 1.0){
					//Naomi cannot win, so tries to make Ken use largest
					while(presentInKen(max_Ken - decr)){
						decr = decr + 0.0000001;
					}
					double Nao_Told = max_Ken - decr;
					//Naomi plays with its min
					deleteFromKen(getSmallestKenGreaterThanNao(Nao_Told));
					deleteFromNao(getSmallestNao());
					
				}
				else{
					//Naomi wins by playing smallest
					if(getSmallestKenGreaterThanNao(max_Ken + incr) == 0.0){
						//Ken puts up smallest valued log, and Nao wins
						deleteFromKen(getSmallestKen());
						deleteFromNao(getSmallestNao());
						winD_War++;
					}
					
				}
				
			}
			N--;	
		}
		
		
		N = NumBlocks;
		bubble_sortKen();
		bubble_sortNao();
		//War
		winWar = 0;
		while(N > 0){
			
			double Nao_chosen = getSmallestNao();
			double Ken_chosen = getSmallestKenGreaterThanNao(Nao_chosen);
			
			if(Ken_chosen == 0.0){
				//Naomi wins for rest all cases
				//Output Naomi : N
				winWar = N;
				break;
			}
			else if(Ken_chosen > Nao_chosen){
				//Ken wins, and blocks burned
				deleteFromKen(Ken_chosen);
				deleteFromNao(Nao_chosen);
			}	
			N--;
		}
		
		cout<<"Case #"<<(i+1)<<": "<<winD_War<<" "<<winWar<<"\n";
		
		
		
		
	}
	
	return 0;
}
