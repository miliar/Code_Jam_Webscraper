#include<iostream>
#include<cstdio>
#include<climits>
#include<cstring>
#include<string>
#include<vector>
#include<queue>
#include<set>

#define INF 100000
#define pb push_back
#define mo 1000000007
#define ll long long int
#define ld long double
#define mp make_pair
#define ull unsigned long long int

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    int T,c,i,j;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        c=0;
        cout<<"Case #"<<i<<": ";
        cin>>s;
        for(j=0;j<s.length()-1;j++)
        {
            if(s[j]!=s[j+1])
                c++;
        }
        c++;
        if(s[s.length()-1]=='+')
            c--;
        cout<<c<<"\n";
    }
    return 0;
}
