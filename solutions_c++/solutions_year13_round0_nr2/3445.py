#include<fstream.h>
ifstream in("BL.in");
ofstream out("output.txt");
int Map[102][102];
int Input[102][102];
int N,M;
int Max;
int Test;
int Flag;
int Min=1000000;
void Lawn()
{
	int i,j,k;
	Max=0;
	for(i=0;i<N;i++){
		for(j=0;j<M;j++){
			if(Map[i][j]!=Input[i][j] && Max<Input[i][j]){
				Max=Input[i][j];
			}
		}
	}
	for(i=0;i<N;i++){
		for(j=0;j<M;j++){
			if(Input[i][j]<=Max){
				for(k=0;k<N;k++){
					if(Input[k][j]>Max)break;
				}
				if(k==N){
					for(k=0;k<N;k++){
						if(Map[k][j]>Max){
							Map[k][j]=Max;
						}
					}
				}
				for(k=0;k<M;k++){
					if(Input[i][k]>Max)break;
				}
				if(k==M){
					for(k=0;k<M;k++){
						if(Map[i][k]>Max){
							Map[i][k]=Max;
						}
					}
				}
			}
		}
	}
	for(i=0;i<N;i++){
		for(j=0;j<M;j++){
			if(Map[i][j]<Input[i][j] || (Map[i][j]!=Input[i][j] && Map[i][j]>Max)){
				Flag=1;
				return;
			}
		}
	}
}
int main()
{
	int i,j,k;
	in>>Test;
	for(k=0;k<Test;k++){
		in>>N>>M;
		Min=10000000;
		Flag=0;
		for(i=0;i<N;i++){
			for(j=0;j<M;j++){
				in>>Input[i][j];
				Map[i][j]=1000000;
				if(Input[i][j]<Min){
					Min=Input[i][j];
				}
			}
		}
		for(;;){
			Lawn();
			if(Flag==1){
				out<<"Case #"<<k+1<<": NO\n";
				break;
			}
			if(Max<=Min){
				out<<"Case #"<<k+1<<": YES\n";
				break;
			}
		}
	}
	return 0;
}