#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);

    int T,x,y,n,sol1,sol2;
    float A[1001], B[1001];
    int MA[1001];

    cin>>T;
    for(int i=1; i<=T; i++)
    {
        memset(MA,0,sizeof MA);
        sol1 = sol2 = 0;
        cin>>n;
        for(int k=0;k<n;k++)
            cin>>A[k];
        for(int k=0;k<n;k++)
            cin>>B[k];

        sort(A,A+n);
        sort(B,B+n);

        printf("Case #%d: ",i);

        //sol1
        for(int j=0;j<n;j++)
        {
            bool f = false;
            for(int k=0; B[k] < A[j]; k++)
            {
                if(MA[k] == 0)
                {
                    MA[k] = 1;
                    f = true;
                    break;
                }
            }
            if(f)
            {
                sol1++;
            }
            else
            {
                for(int k=n-1; k>=0 ; k--)
                {
                    if(MA[k] == 0)
                    {
                        MA[k] = 1;
                        break;
                    }
                }
            }
        }
        printf("%d ",sol1);
        //sol2
        memset(MA,0,sizeof MA);

        for(int j=0;j<n;j++)
        {
            bool f = false;
            for(int k=0; k < n; k++)
            {
                if(MA[k] == 0 and B[k] > A[j])
                {
                    MA[k] = 1;
                    f = true;
                    break;
                }
            }
            if(!f)
            {
                sol2++;
                for(int k=0; k<n ; k++)
                {
                    if(MA[k] == 0)
                    {
                        MA[k] = 1;
                        break;
                    }
                }
            }
        }

        printf("%d\n",sol2);
    }
    return 0;
}

