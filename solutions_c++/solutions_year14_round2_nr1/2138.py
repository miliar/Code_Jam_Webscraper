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
        freopen("1.in","r",stdin);
    #endif
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
        int n,i,j;
        cin>>n;
        string arr[n];
        for(i=0;i<n;i++)
            cin>>arr[i];
        i=0;j=0;
        int res=0,ch=1;
        string a,b;
        while(i<arr[0].length()&&j<arr[1].length())
        {

            if(arr[0][i]==arr[1][j])
            {
                i++;j++;
            }
            else
            {
                if(i==0||j==0)
                {
                    ch=0;
                    break;
                }
                if(arr[0][i-1]==arr[0][i])
                {
                    i++;res++;
                }
                else if(arr[1][j-1]==arr[1][j])
                {
                    j++;res++;
                }
                else
                {
                    ch=0;
                    break;
                }
            }
        }
        if(ch)
        {
            if(i!=arr[0].length())
            {
                char ch1=arr[0][i-1];
                while(i<arr[0].length())
                {
                    if(arr[0][i]!=ch1)
                    {
                        ch=0;
                        break;
                    }
                    res++;i++;
                }
            }

            if(j!=arr[1].length())
            {
                char ch1=arr[1][j-1];
                while(j<arr[1].length())
                {
                    if(arr[1][j]!=ch1)
                    {
                        ch=0;
                        break;
                    }
                    res++;j++;
                }
            }
        }
        if(!ch)
            cout<<"Case #"<<x<<": Fegla Won\n";
        else
            cout<<"Case #"<<x<<": "<<res<<endl;

    }
    return 0;
}
