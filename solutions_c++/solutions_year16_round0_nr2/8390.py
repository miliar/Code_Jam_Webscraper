#include<bits/stdc++.h>
using namespace std;
int main(){
	#ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif 
	int t,k;
	cin>>t;
	k=t;
	while(t--){
		int i;
		char s[105];
		int a[105]={0};
		cin>>s;
		if(s[0]=='-')
		a[0]=1;
		else 
		a[0]=0;
		int l=strlen(s);
		for(i=1;i<l;i++){
			if(s[i]=='-'&&s[i-1]=='+')
			a[i]=a[i-1]+2;
			else
			a[i]=a[i-1];
		}
		cout<<"Case #"<<k-t<<": "<<a[l-1]<<endl;
	}
	return 0;
}
