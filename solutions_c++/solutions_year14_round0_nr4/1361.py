#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <limits>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807
#define INF 2000000000
#define PI acos(-1.0)
#define EPS 1e-9
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair

using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t;
    cin >> t;
    int temp = t;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        double arr1[n],arr2[n];
        for(int i=0;i<n;i++) scanf("%lf",&arr1[i]);
        for(int i=0;i<n;i++) scanf("%lf",&arr2[i]);
        int res=0;
        cout << "Case #" << temp-t << ": ";
        bool taken[1005];
        memset(taken,false,sizeof(taken));
        for(int i=0;i<n;i++)
        {
            double temp=10;
            int ind=0;
            bool big=false;
            for(int j=0;j<n;j++)
            {
                if(arr1[j] < arr2[i] && arr1[j] < temp && !taken[j])
                    temp = arr1[j],ind=j;
                if(arr1[j] > arr2[i] && !taken[j])
                {
                    big = true;
                    break;
                }
            }
            if(big)
            {
                temp=10;
                for(int j=0;j<n;j++)
                    if(arr1[j] > arr2[i] && arr1[j] < temp && !taken[j])
                        temp = arr1[j],ind=j;
                res++;
            }
            taken[ind]=true;
        }
        cout << res << " ";
        memset(taken,false,sizeof(taken));
        res=0;
        for(int i=0;i<n;i++)
        {
            double mini=10;
            int minind=0;
            for(int j=0;j<n;j++)
                if(arr1[i] < arr2[j] && arr2[j] < mini && !taken[j])
                    mini=arr2[j],minind=j;
            if(mini != 10)
                taken[minind]=true;
            else res++;
        }
        cout << res << endl;
    }
    return 0;
}
