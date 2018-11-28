#include <bits/stdc++.h>
#define ll long long 
#define maxn 100005
using namespace std;

int main(){
	int t,cumulate[maxn]={0},k;
	cin>>t;
	k=t;
	while(t--){
	int smax,def=0;
	string s;
	cin>>smax>>s;
	int slen=s.size();
	for(int i=0;i<slen;i++){
		if(i==0) cumulate[i]=s[i]-'0';
		else cumulate[i]=cumulate[i-1]+s[i]-'0';
		if (cumulate[i]<(i+1))
		{
			def+=abs(cumulate[i]-(i+1));
			cumulate[i]+=abs(cumulate[i]-(i+1));
		}
	}
	printf("Case #%d: %d\n",k-t,def);
}
	return 0;
}