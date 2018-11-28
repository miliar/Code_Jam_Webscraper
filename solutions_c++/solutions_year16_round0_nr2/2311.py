#include<iostream>
#include<cstring>
#include<fstream>
#include<string>
using namespace std;
int T;
#define rep(i,j,k) for(int i=j;i<=k;i++)
#define mem(a) memset(a,0,sizeof(a))
int main(){
	//freopen("B-large.in","r",stdin);
	//freopen("out","w",stdout);
	cin>>T;
	rep(i,1,T){
		string tmp;
		cin>>tmp;
		int len=tmp.length();
		int ans=0;
		for(int j=len-1;j>=0;j--){
			if(tmp[j]=='-'){
				ans++;
				tmp[j]='+';
				rep(k,0,j-1){
					if(tmp[k]=='+') tmp[k]='-';
					else tmp[k]='+';
				}
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
