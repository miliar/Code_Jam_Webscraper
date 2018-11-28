#include <iostream>
#include <stdio.h>
#include<string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
typedef long long int ll;
map<ll,ll>m;

bool check(string s){
	ll i=0;
	while(i<s.length()-1){if(s[i]!=s[i+1])return 0;i++;}
	return 1;
}
int main()
{
    freopen("in", "r",stdin );
    freopen("out.txt", "w",stdout );

    ll t;cin>>t;
    string s;
    for(ll i=1;i<=t;i++){
       cout<<"Case #"<<i<<": ";
       cin>>s;
       ll count=0;
       if(s.length()==1 ){if(s[0]=='+')cout<<"0\n";else cout<<"1\n";continue;}
       while(!check(s)){
       	ll i=1,k=0;
       	while(s[i-1]==s[i])i++;
       	while(k<i)s[k++]=s[i];
       	count++;
       }
       if(s[0]=='-')count++;
       cout<<count<<"\n";
    }
    return 0;
}
