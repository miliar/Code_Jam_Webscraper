#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
#include <stdio.h>
using namespace std;
double a[1001],b[1001];

int comp(const void *a, const void *b)
{
    return *(double*)a>*(double*)b?1:-1;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
    int t;
    int count;
    cin>>t;
    int j;
    for (int k=1;k<=t;k++)
    {
        cout<<"Case #"<<k<<": ";
        int n;
        cin>>n;
        for (int i=0;i<=n-1;i++) cin>>a[i];
        for (int i=0;i<=n-1;i++) cin>>b[i];
    //    memset(aa,0,sizeof(aa));
     //   memset(bb,0,sizeof(bb));
        count=0;
        qsort(a,n,sizeof(a[0]),comp);
        qsort(b,n,sizeof(b[0]),comp);
        j=0;
        for (int i=0;i<=n-1;i++)
        {
            while (a[j]<b[i] && j<n) j++;
            if (j<n)
            {
                count++;
                j++;
            }
        }
        cout<<count<<" ";
        count=0;
        j=0;
        for (int i=0;i<=n-1;i++)
        {
            while (b[j]<a[i] && j<n) j++;
            if (j<n)
            {
                count++;
                j++;
            }
        }
        cout<<n-count<<endl;
    }
    return 0;
}
