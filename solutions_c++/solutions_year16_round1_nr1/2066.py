#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define pb(v,x) v.push_back(x)
#define REP(i,n) for(i=0;i<n;i++)
using namespace std;
FILE * fp1 , * fp2;
void rec(int i, int n, string s, int a[])
{
    if(i==-1) return;
    if(i==0){
        fprintf(fp2,"%c",s[i]);
        return;
    }
    int j;
    fprintf(fp2,"%c",s[a[i]]);
    rec(a[i]-1,n,s,a);
    for(j=a[i]+1;j<=i;j++) fprintf(fp2,"%c",s[j]);
}
int main()
{
    fp1 = fopen("input.txt","r");
    fp2 = fopen("output.txt","w");
    int t;
    fscanf(fp1,"%d",&t);
    for(int test=1;test<=t;test++)
    {
        char s[1005];
        fscanf(fp1,"%s",s);
        int i,n=strlen(s);
        char maxi=s[0];
        int a[n+1];
        a[0]=0;
        for(i=1;i<n;i++){
            if(s[i]>=maxi){
                maxi=s[i];
                a[i]=i;
            }
            else a[i]=a[i-1];
        }
        fprintf(fp2,"Case #%d: ",test);
        //REP(i,n) cout<<a[i]<<" ";
        fprintf(fp2,"%c",s[a[n-1]]);
        rec(a[n-1]-1,n,s,a);
        for(i=a[n-1]+1;i<n;i++) fprintf(fp2,"%c",s[i]);
        fprintf(fp2,"\n");
    }
    return 0;
}
