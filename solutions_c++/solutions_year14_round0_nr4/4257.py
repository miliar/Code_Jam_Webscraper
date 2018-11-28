#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<set>
#include<map>
using namespace std;

int main()
{
     freopen("D-large.in","r",stdin);
    // freopen("cj_input.txt","r",stdin);
     freopen("D-small-11.out","w",stdout);//D-small-4.out
    int ti,t;
    cin>>ti;
    for(t=1;t<=ti;t++)
    {
        int n,i,j;
        cin>>n;
        vector< float >nao(n);
        vector< float >ken(n);
        int ans1=0,ans=0,temp=0;
            for(j=0;j<n;j++)
                cin>>nao[j];
                for(j=0;j<n;j++)
                cin>>ken[j];

        sort(nao.begin(),nao.end());
        sort(ken.begin(),ken.end());
        int k;
        j=0;
        k=0;
        for(i=0;i<n;i++)
        {
            for(;j<n;j++)
            {
                if(ken[j]>nao[i])
               {
                break;
               }
               // j++;
            }
            if(j==n)
           {
            ans1+=n-i;
            break;
           }
           else
            j++;
        }
        j=0;k=0;
        int mpos=n-1,it;
        for(i=0;i<n;i++)
        {
            if(nao[j]<ken[k])
            {
                it=j;
            while(nao[it]<ken[k] && it<n)
                it++;
                if(it>=n)
                {
                  swap(ken[k],ken[mpos]);
                  mpos--;
                  k++;
                  j++;
                }
                else
                {
                    swap(nao[it],nao[j]);
                    ans++;
                    j++;k++;
                }
            }
            else
            {
                ans++;
                j++;
                k++;
            }
        }

        printf("\nCase #%d: %d %d",t,ans,ans1);
    }
    return 0;
}

