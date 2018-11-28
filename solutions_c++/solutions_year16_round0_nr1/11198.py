#include <iostream>
using namespace std;

int main() {
	long long t,n,nn;
	int cnt;
	cin>>t;
	for(int i=1;i<=t;i++){
		cnt =0;
		nn=0;
		cin>>n;
		int a[10] ={0};
		int j=1;
		int inf=0;
		while(1){
			if(n*j==nn){
				inf = 1;
				break;
			}
			nn=n*j;
			while(nn>0){
				int last = nn%10;
				//cout<<"nn last"<<nn<<" "<<last<<"\n";
				if(a[last]==0){
					a[last]++;
					cnt++;
				}
				nn/=10;
				
			}
			if(cnt==10){
					nn=n*j;
					inf=2;
					break;
				}
			nn=n*j;
			j++;
			}
			if(inf==1){
				cout<<"case #"<<i<<": INSOMNIA\n";
			}
			else if(inf==2){
				cout<<"case #"<<i<<": "<<nn<<"\n";
			}
		}
	
	return 0;
}
