
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int main()
{   //READ("A-Small.in");
    //WRITE("A-Small.out");
    int t;
    double A[10],B[10];
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        memset(A,0.0,sizeof(A));
        memset(B,0.0,sizeof(B));
        int p,q,r,n;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>A[i];
        }
        for(int i=0;i<n;i++)
        {
            cin>>B[i];
        }
        int cnt1=0,cnt2=0;
        sort(A,A+n);
        sort(B,B+n);

        p=0;
        q=n-1;
        for(int i=0;i<n;i++)
        {
            if(A[i]>B[p] && p<=q)
            {
                cnt1++;
                p++;
            }
            else
            {
                q--;
            }
        }
        p=0;
        q=n-1;
        for(int i=n-1;i>=0;i--)
        {
            if(A[i]>B[q] && p<=q)
            {
                cnt2++;
                p++;
            }
            else
            {
                q--;
            }

        }
        //cout<<cnt1<<" "<<cnt2<<endl;
        printf("Case #%d: %d %d\n",k,cnt1,cnt2);

    }
    return 0;
}
