
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;

int main(){
	ofstream fout("ans7.txt");
	ifstream fin("inp7.IN");
	int t;
	fin>>t;
	int tt=0;
	while(tt++!=t){
		int n,temp;
		fin>>n;
		int ans[50];
		int het[2501];
		for(int i=0;i<2501;++i)
			het[i]=0;
		for(int i=0;i<(2*(n)-1);++i){
			for(int j=0;j<n;++j){
				fin>>temp;
				++het[temp];
			}
		}
		

		int index=0;
		for(int i=1;i<2501;++i){
			if((het[i]%2)==1){
				ans[index++]=i;
			}
		}
		
		fout<<"Case #"<<tt<<": ";
		for(int i=0;i<n;++i)
			fout<<ans[i]<<" ";
		fout<<"\n";


	}

}
