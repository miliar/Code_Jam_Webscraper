#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int t,a,b,c,d[17];
int main()
{
	int i,j,k,cnt,ans;
	//freopen("A-small-attempt3.in","r",stdin);
	//freopen("A-small-attempt3.out","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++){
		memset(d,0,sizeof(d));
		cnt=0;
		cin>>a;
		for(i=1;i<5;i++){
			for(j=1;j<5;j++){
				cin>>c;
				if(i==a) d[c]=1;
				//if(i==a)cout<<c<<" ";
			}
		}
		//cout<<endl;
		cin>>b;
		for(i=1;i<5;i++){
			for(j=1;j<5;j++){
				cin>>c;
				if(i==b && d[c])cnt++,ans=c;
				//if(i==b)cout<<c<<" ";
			}
		}
		//cout<<endl;
		cout<<"Case #"<<k<<": ";
		if(cnt==1)cout<<ans;
		else if(cnt>1)cout<<"Bad magician!";
		else cout<<"Volunteer cheated!";
		cout<<endl;
	}
	return 0;
}
