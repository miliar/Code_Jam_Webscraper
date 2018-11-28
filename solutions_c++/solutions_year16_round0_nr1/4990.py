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
    set<int> s;
    int T,i;
    ull n,j,a;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>n;
        if(n==0)
        {
            cout<<"INSOMNIA\n";
            continue;
        }
        for(j=1;true;j++)
        {
            a=j*n;
            while(a!=0)
            {
                s.insert(a%10);
                a/=10;
            }
            if(s.size()==10)
            {
                cout<<j*n<<"\n";
                break;
            }
        }
        s.clear();
    }
    return 0;
}
