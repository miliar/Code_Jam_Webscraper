#include <iostream>
#include <algorithm>
#include<stdlib.h>
#include <stdio.h>
using namespace std;
int main()
{
    int n,ans,aud,k;
    char s[10000];
    FILE *fp,*fpi;
    fpi=fopen("A-large.in.txt","r");
    fp=fopen("alarge.txt","w");
    int t;
    //cin>>t;
    fscanf(fpi,"%d ",&t);
    k=1;
    //for(int k=1;k<=t;k++)
    while(fscanf(fpi,"%d %s ",&n,s)!=EOF)
    {
        ans=0;aud=0;

        //cin>>n;
        //cin>>s;
        aud=aud+s[0]-48;
        for(int i=1;i<=n;i++)
        {
            if(aud>=i)aud=aud+s[i]-48;
            else
            {
                ans=ans+i-aud;
                aud=i+s[i]-48;
            }
        }
        //cout<<"Case #"<<k<<": "<<ans<<endl;
        fprintf(fp,"Case #%d: %d\n",k,ans);
        k++;
    }
    fclose(fpi);
    fclose(fp);
    return 0;
}
