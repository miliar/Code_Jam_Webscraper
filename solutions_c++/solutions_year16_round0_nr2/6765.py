#include <bits/stdc++.h>
using namespace std;

int main(void)
{
	int t,min;;
	string s;
	int a[101];
	cin>>t;
	while(t--){
		min=0;
		cin>>s;
		for(i=0;i<s.length();i++){
			if(s[i]=='-')
				a[i]=0;
			else
				a[i]=1;
		}
		for(i=1;i<s.length();i++){
			if(a[i]!=a[i-1]){
				a[i-1]=a[i];
				min++;
			}
		}
		if(a[s.length()-1]==0)
			min++;

		cout<<"Case #"<<i<<": "<<min<<endl;
	}
}