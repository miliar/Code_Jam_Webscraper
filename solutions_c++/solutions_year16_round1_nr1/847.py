#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ull;
#define A first
#define B second
#define MP make_pair
#define PB push_back
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        string s;
        cin>>s;
        string ans;
        for(int i=0;i<s.length();i++)
        {
            if(ans+s[i]>s[i]+ans)
                ans=ans+s[i];
            else
                ans=s[i]+ans;
        }
        cout<<"Case #"<<cas++<<": "<<ans<<endl;
    }
    return 0;
}
