//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

int ar[1000009],convert[1009][1009];


int poss(int curr,int N)
{
    int i,j,k,ans;

    for(i=1;i<=curr;i++)
    {
        ans=i;
        for(j=1;j<=N;j++)
        {
            ans+=convert[ar[j]][i];
        }
        if(ans<=curr) return 1;
    }
    return 0;
}

int check(int low,int high,int N)
{
    if(low==high) return low;
    if(low==high-1)
    {
        if(poss(low,N)) return low;
        return high;
    }

    int mid;
    mid=low+high;
    mid/=2;

    if(poss(mid,N)) return check(low,mid,N);
    return check(mid,high,N);
}

int  main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);

    int i,j,k,N,T,S,ans,temp,cas=0,M,K;

    for(i=1;i<=1000;i++)
    {
        for(j=1;j<=1000;j++)
        {
            if(i<=j) convert[i][j]=0;
            else
            {
                convert[i][j]=100000;
                for(k=1;;k++)
                {
                    if(k*j<i)
                    {
                        continue;
                    }
                    M=k-1+convert[i/k][j]*(k-i%k)+convert[i/k+1][j]*(i%k);
                    //cout<<i<<" "<<j<<" "<<k<<" "<<M<<endl;
                    if(M>convert[i][j]) break;
                    convert[i][j]=M;
                    //cout<<i<<" "<<j<<" "<<k<<endl;
                }
            }
        }
    }


    cin>>T;
    while(T--)
    {
        cas++;
        cin>>N;

        for(i=1;i<=N;i++)
        {
            cin>>ar[i];
        }

        sort(ar+1,ar+1+N);
        reverse(ar+1,ar+1+N);

        ans=check(1,1000000,N);

        printf("Case #%d: %d\n",cas,ans);

    }

}
