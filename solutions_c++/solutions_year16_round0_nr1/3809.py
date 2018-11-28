#include<cstdio>
#include<fstream>
using namespace std;
int T,N,arr[10];
int main(){
	ifstream fin;
	fin.open("A-small.in");
	ofstream fout;
	fout.open("A-small.out");
	
	fin>>T;
	
	for(int i=0;i<T;++i){
		for(int j=0;j<10;++j) arr[j]=0;
		fin>>N;
		fout<<"Case #"<<(i+1)<<": ";
		if(N==0){
			fout<<"INSOMNIA"<<endl;
			continue;
		}
		else{
			int curN=N,conut=1;
			bool sleep=false;
			while(!sleep){
				curN=conut*N;
				int tmpN=curN;
				while(tmpN>0){
					int curD=tmpN%10;
					tmpN=tmpN/10;
					arr[curD]=1;
				}
				sleep=true;
				for(int l=0;l<10;++l) sleep=sleep&arr[l];
				conut++;
			}
			fout<<curN<<endl;
		}
	}
	
	fin.close();
	fout.close();
	
	return 0;
	
}
