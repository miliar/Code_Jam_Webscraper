#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    long long int t,c=0;
    cin>>t;
    for(long long int i=0; i<t; i++){
    string s;
    cin>>s;
    c=0;
    int len=s.length();
    for(int i=(len-1); i>=0; i--){
    if(s[i]=='-'){
    if(s[i]=='-'&& s[i-1]=='+')
    c=c+2;
    else if(s[i]=='-' && s[i-1]=='-')
    c=c+0;
    else c=c+1;
    }
    }
    printf("Case #%lld: %lld\n",(i+1),c);
    }
}
