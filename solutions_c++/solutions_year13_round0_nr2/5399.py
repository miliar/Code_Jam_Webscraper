#include<fstream>

using namespace std;

int main(){

	int T;


	ifstream in("in.txt");
	ofstream out("out.txt");

	in>>T;
	for(int t=1;t<=T;t++){
		int N,M;
		int a[101][101];

		in>>N>>M;

		for(int i=0;i<N;i++){
			for(int j=0;j<M;j++){
				in>>a[i][j];
			}
		}
		int impossible=0;

		for(int cutval=100;cutval>0;cutval--){
			int exist=0;
			int row[101]={0,};
			int col[101]={0,};
			for(int i=0;i<N;i++){
				for(int j=0;j<M;j++){
					if(a[i][j]==cutval) exist=1;
					if(a[i][j]>cutval){
						row[i]=1;
						col[j]=1;
					}
				}
			}

			if(exist!=0){
				for(int i=0;i<N;i++){
					for(int j=0;j<M;j++){
						if(a[i][j]==cutval &&(row[i]&&col[j]))
							impossible=1;
					}
				}
			}
		}

		if(impossible) out<<"Case #"<<t<<": NO"<<endl;
		else out<<"Case #"<<t<<": YES"<<endl;
	}
}