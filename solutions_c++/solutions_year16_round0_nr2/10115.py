#include<iostream>
#include<fstream>
#include<string>

void flipPancakes(int);
int allHappy(char*);

char pstring[11];
int main(){
	
	int cases=1,T;
	
	std::ifstream fin("B-small-attempt0.in"); 
	std::ofstream fout("pancakeoutput.txt");

	fin>>T;// std::cout<<T;
	fin.ignore(1,' ');
	do{
	
	fin.getline(pstring,11);
	//strcpy(string,str.c_str());
	
	// std::cout<<"\n \""<<pstring<<"\" enter this\n";
	//fout<<pstring;
	//std::cin.getline(pstring,10);
	int flip=0,count=0;
	//std::cout<<"\n"<<allHappy(pstring);
	for(int i=0;pstring[i]!='\0';i++){
		
		
		if(pstring[i]!=pstring[i+1]){
			//cout<<"\n"<<pstring;
			
			if(allHappy(pstring)==1){ 
			//fout<<"\nbroke";
			 break;}
			

			flipPancakes(i);
			//fout<<"\n flipped";
			//if(!allHappy(pstring))
			count++;
		}
	}
	
	fout<<"\nCase #"<<cases<<": "<<count;
	//std::cout<<"\nCase #"<<cases<<"count: "<<count;
	cases++;
	}while(cases<=T);

	//std::fout<<"\n the final pstring: "<<pstring;
	//std::cout<<"\n"<<allHappy(pstring);

	fin.close();
	fout.close();
	return 0;

}


void flipPancakes(int i){
	
	for(int j=0;j<=i;j++){
		if(pstring[j]=='+'){
			pstring[j]='-';

		}else pstring[j]='+';
	}

}

int allHappy(char* string){
	
	for(int i=0;i<string[i]!='\0';i++){
		if(string[i]=='-'){
		//std::cout<<"\n I am not happy now!";
		return 0;		
		}
	
	
	}

return 1;
}
