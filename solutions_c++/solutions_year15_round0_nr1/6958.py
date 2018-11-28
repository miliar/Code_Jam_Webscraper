#include<iostream>
#include<cstdio>
using namespace std;
int a[1005];

int main()
{
    FILE *fin=fopen("f:/A-large.in","r");
    FILE *fout=fopen("f:/gccbj.txt","w");
    int t,n,tot,ans;
    fscanf(fin,"%d",&t);
    int T=t;
    while(t--)
    {
        ans=0;tot=0;
        fscanf(fin,"%d",&n);
        for(int i=0;i<=n;++i)
        {
            fscanf(fin,"%1d",&a[i]);
        }
        for(int i=0;i<=n;++i)
        {
            if(tot<i)
            {
                ans+=(i-tot);
                tot=tot+a[i]+i-tot;
            }
            else
               tot+=a[i];
        }
        fprintf(fout,"Case #%d: %d\n",T-t,ans);
      //      cout<<"Case #"<<T-t<<": "<<ans<<endl;

    }
}
