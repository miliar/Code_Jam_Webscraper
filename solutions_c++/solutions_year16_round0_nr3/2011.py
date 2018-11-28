#include <iostream>
#include <fstream>
using namespace std;
typedef long long ll;
int main(){
	ofstream ofs("out.txt");
	int t;	cin>>t;
	for(int i=1;i<=t;i++){
		int N,J;	cin>>N>>J;
		ll cur=(1<<(N-1))+1;
		ofs<<"Case #"<<i<<":"<<endl;
		for(int j=0;j<J;cur+=2){
			int cnt=0;
			for(int k=0;k<N;k++){
				if(cur&(1<<k)){
					cnt+=(k%2?1:-1);
				}
			}
			if(cnt!=0)	continue;
			for(int k=N-1;k>=0;k--){
				ofs<<(cur&(1<<k)?1:0);
			}
			for(int k=2;k<=10;k++)	ofs<<" "<<k+1;
			ofs<<endl;
			j++;
		}
	}
	return 0;
}
