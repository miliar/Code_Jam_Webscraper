#include<iostream.h>
#include<conio.h>
#include<fstream.h>





void main(){

clrscr();

ofstream output;
output.open("output.txt");
ifstream input;
input.open("input.txt");

int T;
input>>T;
int i=0;
for(i=0;i<T;i++){
int M,N;
input>>N>>M;
int j=0,k=0;
int** lawn=new int*[N];

for(j=0;j<N;j++){
	lawn[j]=new int[M];
	for(k=0;k<M;k++){
		input>>lawn[j][k];
	}
}


for(j=0;j<N;j++){
	int f=0;
	for(k=0;k<M;k++){
		f=0;
		for(int u=0;u<M;u++){

		if(u!=k&&lawn[j][u]>lawn[j][k]){

		f=1;
				break;
			}
		}
		if(f==1)
		for(u=0;u<N;u++){
			if(u!=j&&lawn[u][k]>lawn[j][k]){
				f=2;
				break;
																									}



		}
		if(f==2)
			break;


	}
	if(f==2){
		output<<"Case #"<<i+1<<": NO"<<endl;
			break;
	}

}

	if(j==N&&k==M){
		output<<"Case #"<<i+1<<": YES"<<endl;
	}

}
getch();
}