// GCJ2013_QR_B_Large.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
using namespace std;

int a[100][100];
set<int> s1;
int v[100];

int main(int argc, char* argv[])
{
    freopen("c:/txt/B-large.in","r",stdin);
    freopen("c:/txt/2013-QR-B-large.txt","w",stdout);
    int i, j, k, l, m, T, M, N;
    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
        scanf("%d %d",&M, &N);
        s1.clear();
        for(j=0;j<M;j++)
        {
            for(k=0;k<N;k++)
            {
                scanf("%d", &a[j][k]);
                s1.insert(a[j][k]);
            }
        }
        set<int>::iterator itr;
        j=0;
        for(itr=s1.begin();itr!=s1.end();itr++)
        {
            v[j++]=*itr;
        }
        bool Yes=true;
        for(j=0;j<s1.size();j++)
        {
            for(k=0;k<M;k++)
            {
                for(l=0;l<N;l++)
                {
                    if(a[k][l]<=v[j])
                    {
                        a[k][l]=v[j];
                    }
                }
            }
            bool isValidate=true;
            for(k=0;k<M;k++)
            {
                bool isPossible=true;
                for(l=0;l<N;l++)
                {
                    if(a[k][l]==v[j])
                    {
                        int p=0;
                        for(m=0;m<N;m++)
                        {
                            p+=a[k][m];
                        }
                        int q=0;
                        for(m=0;m<M;m++)
                        {
                            q+=a[m][l];
                        }
                        if(p!=N*v[j] && q!=M*v[j])
                        {
                            isPossible=false;
                            break;
                        }
                    }
                }
                if(!isPossible)
                {
                    isValidate=false;
                    break;
                }
            }
            if(!isValidate)
            {
                Yes=false;
                break;
            }
        }
        if(Yes)
        {
            printf("Case #%d: YES\n", i+1);
        }
        else
        {
            printf("Case #%d: NO\n", i+1);
        }
    }
    return 0;
}

