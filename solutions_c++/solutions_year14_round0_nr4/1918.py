#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <queue>
using namespace std;

typedef long long LL;

LL gcd(LL a, LL b) { return b?gcd(b,a%b):a; }

int main()
{
    std::ios_base::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
        freopen("in44.in","r",stdin);
    #endif
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        int n;
        cin>>n;
        float arr[n],brr[n],crr[n];
        for(int j=0;j<n;j++)
            cin>>arr[j];
        for(int j=0;j<n;j++)
            {cin>>brr[j];crr[j]=brr[j];}
        sort(arr,arr+n);
        sort(brr,brr+n);
        int r1=0,r2=0;
        for(int j=n-1;j>=0;j--)
        {
            float tmp=arr[j];
            if(tmp>brr[j])
            {
                r2++;
                brr[0]=brr[j];
                sort(brr,brr+j);
                continue;
            }
            int k;
            for(k=j-1;k>=0;k--)
            {
                if(brr[k]<tmp)
                    break;
            }
            float x=brr[k+1];
            brr[k+1]=brr[j];
            brr[j]=x;
            sort(brr,brr+j);
        }
        sort(arr,arr+n);
        for(int j=0;j<n;j++)
            {brr[j]=crr[j];}
        sort(brr,brr+n);
        for(int j=n-1;j>=0;j--)
        {
            float tmp=arr[j];
            //cout<<"tmp="<<tmp<<endl;
            if(tmp>brr[j])
            {
                r1++;
                int l;
                for(l=0;l<=j;l++)
                {
                    if(arr[l]>brr[0])
                        break;
                }
                arr[l]=arr[j];
                sort(arr,arr+j);
                brr[0]=brr[j];
                sort(brr,brr+j);
              //  for(int l=0;l<=j;l++)
                //    cout<<brr[l]<<" ";cout<<endl;
                continue;
            }
            int k;
            for(k=j-1;k>=0;k--)
            {
                if(brr[k]<tmp)
                    break;
            }
            float x=brr[k+1];
            brr[k+1]=brr[j];
            //cout<<k+1<<" "<<j<<endl;
            brr[j]=x;
            arr[0]=arr[j];
            sort(arr,arr+j);
            sort(brr,brr+j);
        }

        printf("Case #%d: %d %d\n",i,r1,r2);
    }
    return 0;
}

