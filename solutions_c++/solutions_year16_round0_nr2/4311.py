#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define pb(v,x) v.push_back(x)
#define REP(i,n) for(i=0;i<n;i++)
using namespace std;
string to_string(ll n)
{
    string s="";
    while(n>0){
        char ch = n%10+48;
        s+=ch;
        n = n - n%10;
        n/=10;
    }
    return s;
}
int main()
{
    FILE *fp1;FILE *fp2;
    fp1 = fopen("input.txt","r");
    fp2 = fopen("output.txt","w");
    int t;
    ll n;
    fscanf(fp1,"%d",&t);
    for(int test=1;test<=t;test++)
    {
        char s[105];
        fscanf(fp1,"%s",s);
        int ans=0,i;
        fprintf(fp2,"Case #%d: ",test);
        string s1 = string(s);s1+='+';
        for(i=1;i<s1.length();i++){
            if(s1[i]!=s1[i-1]) ans++;
        }
        fprintf(fp2,"%d\n",ans);
    }
    return 0;
}
