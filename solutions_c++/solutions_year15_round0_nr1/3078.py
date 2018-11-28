#include<bits/stdc++.h>
using namespace std;
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out2.txt","w",stdout);
	int t,r;
	cin>>t;
	for(int r=1;r<=t;r++){
		int s;
		cin>>s;
		char a[s+1];
		cin>>a;
		int l=strlen(a);
		int b[s+1];
		for(int i=0;i<l;i++)
		b[i]=(a[i]-'0');
		int count=b[0];
		int flag=0;
		for(int i=1;i<l;i++){
			if(b[i]==0)
			continue;
			if(count+flag < i)
			flag+=i-(count+flag);
			count+=b[i];
		}
		cout<<"Case #"<<r<<": "<<flag<<"\n";
	}
}
