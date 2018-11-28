#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<cmath>
#include<algorithm>
#include<iterator>
#include<sstream>
#include<time.h>
using namespace std;
#define scan(n) scanf("%d",&n)
#define INF 1000000007
typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;

int main()
{
    int t; scan(t); for (int test=1; test<=t; test++)
    {
        cout<<"Case #"<<test<<": ";
        int n; scan(n); int arr[n+1]; string s; cin>>s;
        for (int i=0; i<s.length(); i++)
        {
            arr[i]=s[i]-'0';
        }
        int ans=0; int p=0; int total=0;
        for (int i=0; i<n+1; i++)
        {
            if (total<i)
            {
                if (arr[i]) {
                ans+=(i-total);
                total=i;}
            }
            total+=arr[i];
        }
        cout<<ans<<endl;

    }


}
