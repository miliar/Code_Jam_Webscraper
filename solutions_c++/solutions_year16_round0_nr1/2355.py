#include<iostream>
#include<fstream>
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;cin>>t;
	for(int x=1;x<=t;x++){
		bool check=0,arr[10]={0};
		long long int n,p=0;cin>>n;
		if(n==0)cout<<"Case #"<<x<<": INSOMNIA"<<endl;
		else{
			for(int i=1;;i++){
				p=n*i;
				while(p){
					arr[p%10]=1;
					p/=10;
				}
				check=arr[0];
				for(int j=1;j<10;j++){
					check=check&arr[j];
				}
				if(check==1){
					p=n*i;cout<<"Case #"<<x<<": "<<p<<endl;break;
				}
			}
		}
	}
	return 0;
}
