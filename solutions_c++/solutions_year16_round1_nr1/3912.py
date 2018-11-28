#include<iostream>
#include<algorithm>
#include<cstdio>
#include<climits>
#include<cstring>
#include<string>
#include<vector>
#include<queue>
#include<list>

#define INF 100000
#define mo 1000000007
#define ll long long int
#define ld long double
#define ull unsigned long long int
#define mp make_pair
#define pb push_back
#define pf push_front

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T,i,j;
    list<char> ls;
    list<char>::iterator iter;
    string s;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>s;
        ls.pb(s[0]);
        for(j=1;j<s.length();j++)
        {
            if(s[j]>=ls.front())
            {
                ls.pf(s[j]);
            }
            else
            {
                ls.pb(s[j]);
            }
        }
        for(iter=ls.begin();iter!=ls.end();iter++)
        {
            cout<<*iter;
        }
        cout<<"\n";
        ls.clear();
    }
    return 0;
}

