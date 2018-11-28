#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>

using namespace std;
int main()
{

    int t,n,j,st,gotj,temp,ind,k,valb;
    long long vl,pv;
    FILE * fin, * fot;
    fin = fopen ("smallC.in","r");
    fot = fopen ("ans.out","w");
    fscanf(fin,"%d",&t);
    for(int i=0; i<t; i++)
    {
        fscanf(fin,"%d%d",&n,&j);
        vector<int> all(n,1);
        vector<int> fact(9,2);
        gotj=0;
        st=0;
        fprintf(fot,"Case #%d:\n",i+1);
        valb=1<<n-2;
        while(gotj<j&&st<valb)
        {
            temp=st;
            printf("st: %d, gotj: %d\n",st,gotj);
            ind=1;
            while(temp)
            {
                if(temp&1)
                {
                    all[ind]=1;
                }
                else
                {
                    all[ind]=0;
                }
                ind++;
                temp>>=1;
            }
            while(ind<n-1)
                all[ind++]=0;
            for(k=2;k<=10;k++)
            {
                vl=0;pv=1;
                for(int b=0;b<n;b++)
                {
                    if(all[b]==1)
                        vl+=pv;
                    pv*=k;
                }
                printf("k: %d, pv: %lld\n",k,vl);
                bool prime=true;
                for(long long b=2;b<=sqrt(vl);b++)
                {
                 if(vl%b==0)
                 {
                     prime=false;
                     fact[k-2]=b;
                     break;
                 }
                }
                if(prime)
                    break;
            }
            if(k==11)
            {
                gotj++;
                for(int b=n-1;b>=0;b--)
                    fprintf(fot,"%d",all[b]);
                for(int b=0;b<9;b++)
                    fprintf(fot," %d",fact[b]);
                fprintf(fot,"\n");
            }
            st++;
        }
    }

    fclose(fin);
    fclose(fot);

}
