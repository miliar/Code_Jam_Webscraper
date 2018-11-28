#include<bits/stdc++.h>
using namespace std;
char a[200];

void fun(int i){
	char aa;
	if(a[i]=='+')
		aa='-';
	else if(a[i]=='-')
		aa='+';
	
	for(int k=0; k<=i; k++){
		a[k]=aa;
	}
}

int main(){
	int c=0,l,ind,ans,ii,i,j,k,t,n;
	FILE *fin1 = freopen("input.txt", "r", stdin);
	FILE *fin2 = freopen("output.txt", "w", stdout);
	cin>>t;
	while(t--){
		c++;
		cin>>a;
		ans=0;
		l=strlen(a);
		for(i=1;i<l;i++){
			if(a[i-1]!=a[i])
				{
					fun(i-1);
					ans++;
				}
		}
		
		if(a[l-1]=='-')
			ans++;
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
return 0;
}