#include<bits/stdc++.h>

using namespace std;

int main()
{
    FILE *p,*q;
    p=fopen("input.txt","r");
    q=fopen("output.txt","w");
    int t,smax,ii=0,res,ans,i;
    char s[10000];
    fscanf(p,"%d",&t);
    while(t--)
    {
        fscanf(p,"%d%s",&smax,s);
        //cout<<smax<<" "<<s<<endl;
        res=s[0]-'0';
        ans=0;
        for(i=1;i<=smax;i++){
            if(res<i) {ans+=i-res;res+=s[i]-'0'+(i-res);}
            else res+=s[i]-'0';
        }
        fprintf(q,"Case #%d: %d\n",++ii,ans);
        //printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}
