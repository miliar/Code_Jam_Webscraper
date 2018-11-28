#include <iostream>

using namespace std;

int main()
{
    int T,i,j,k,l,N,war=0,dwar=0,minIndex,naomiWar,index[1000];
    double naomi[1000],ken[1000],copyKen[1000],copyNaomi[1000],min;
    bool bitKen[1000],bitNaomi[1000];
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cin>>N;
        for(j=0;j<1000;j++)
        {
            bitKen[j]=1;
        }
        for(j=0;j<1000;j++)
        {
            bitNaomi[j]=1;
        }
        war=0;
        dwar=0;
        for(j=0;j<N;j++)
        {
            cin>>naomi[j];
        }
        for(j=0;j<N;j++)
        {
            cin>>ken[j];
        }
        for(j=0;j<N;j++)
        {
            copyKen[j]=ken[j];
        }
         for(j=0;j<N;j++)
        {
            copyNaomi[j]=naomi[j];
        }
        for(j=0;j<N;j++)
        {
            l=0;
            for(k=0;k<N;k++)
            {
                if(naomi[j]<copyKen[k]&&bitKen[k])
                {
                    index[l]=k;
                    l++;
                }
            }
            if(l>0)
            {
                min=copyKen[index[0]];
                minIndex=index[0];
                for(k=0;k<l;k++)
                {
                    if(min>copyKen[index[k]])
                    {
                        min=copyKen[index[k]];
                        minIndex=index[k];
                    }
                }
                war++;
                bitKen[minIndex]=0;
            }

        }
        naomiWar=N-war;
        for(j=0;j<N;j++)
        {
            l=0;
            for(k=0;k<N;k++)
            {
                if(ken[j]<copyNaomi[k]&&bitNaomi[k])
                {
                    index[l]=k;
                    l++;
                }
            }
            if(l>0)
            {
                min=copyNaomi[index[0]];
                minIndex=index[0];
                for(k=0;k<l;k++)
                {
                    if(min>copyNaomi[index[k]])
                    {
                        min=copyNaomi[index[k]];
                        minIndex=index[k];
                    }
                }
                dwar++;
                bitNaomi[minIndex]=0;
            }

        }
        cout<<"Case #"<<i<<": "<<dwar<<" "<<naomiWar<<endl;
    }
    return 0;
}
