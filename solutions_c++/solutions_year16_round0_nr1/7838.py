#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

bool f[20];
int n,t,tmp,ans,p,u;

int main (){
	//freopen ("a.in","r",stdin);
	//freopen ("a.out","w",stdout);
	cin>>t;
	int i,j;
	for (i=1;i<=t;i++){
		cout<<"Case #"<<i<<": "; 
		cin>>n;
		if (!n){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		tmp=ans=0;
		memset (f,0,sizeof (f));
		for (j=1;;j++){
			tmp+=n;
			p=tmp;
			//cout<<tmp<<endl;
			while (p){
				u=p%10;
				if (!f[u]){f[u]=1;ans++;}
				p/=10; 
			}
			if (ans==10){
				cout<<tmp<<endl;
				break;
			}
		}
	}
				
	return 0;
}
