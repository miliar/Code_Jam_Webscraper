#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,j;
//	freopen("1.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	cin>>t;
	for(j=1;j<=t;j++){
		int sm,i,f=0;
		string s;
		cin>>sm>>s;
		int a[sm+1];
		for(i=0;i<=sm;i++){
			if(i==0)
			a[i]=s[i]-'0';
			else{
				if(a[i-1]>=i){
					a[i]=a[i-1]+s[i]-'0';
				}
				else{
					f=f+i-a[i-1];
					a[i]=i+s[i]-'0';
					//cout<<a[i]<<" ";
				}
			}
		}
		//cout<<"\n";
		cout<<"Case #"<<j<<": "<<f<<"\n";
	}
	return 0;
}
