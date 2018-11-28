#include <iostream>

using namespace std;

int matriz[4][4]={0};
int matriz2[4][4]={0};
bool compareMatriz(){
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(matriz[i][j]!=matriz2[i][j])
				return false;
	return true;
			
}
int main(){
	int t=0,n=0;
	cin>>t;
	while (n<t){
		n++;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				matriz[i][j]=0;
				matriz2[i][j]=0;
			}
				
		int answ1=0,answ2=0;
		cin>>answ1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>matriz[i][j];

		cin>>answ2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>matriz2[i][j];
		
		if(compareMatriz() && answ1!=answ2)
				cout<<"Case #"<<n<<": Volunteer cheated!"<<endl;
		else{
			int cont=0,number=-1;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++)
					if(matriz[answ1-1][i]==matriz2[answ2-1][j]){
						cont++;
						if(cont>1){
							i=5;
							i=5;
						}else
							number=matriz[answ1-1][i];
							
					}
		
		if(cont==1)
			cout<<"Case #"<<n<<": "<<number<<endl;	
		else if(cont>0)
				cout<<"Case #"<<n<<": Bad magician!"<<endl;
			else
				cout<<"Case #"<<n<<": Volunteer cheated!"<<endl;
		
				
		}
	}
	
	return 0;
}
