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
        fscanf(fp1,"%lld",&n);
        fprintf(fp2,"Case #%d: ",test);
        if(n==0){
            fprintf(fp2,"INSOMNIA\n");
            continue;
        }
        bool marked[10];
        int i=1,j;
        memset(marked,false,sizeof(marked));
        while(i){
            string s = to_string(n*i);
            REP(j,s.length()) marked[s[j]-'0']=true;
            REP(j,10) if(!marked[j]) break;
            if(j==10) break;
            i++;
        }
        fprintf(fp2,"%lld\n",n*i);
    }
    return 0;
}
