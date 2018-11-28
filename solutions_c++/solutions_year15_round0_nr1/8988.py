#include <bits/stdc++.h>

#define pb push_back
#define ull  unsigned long long
#define ll  long long
#define pii pair<int,int>
#define vpii vector<pii>
#define vll  vector<ll >
#define mp make_pair
#define mii map<int, int>
#define F first
#define S second
#define M 1000000007
#define iofast (ios_base::sync_with_stdio(false))

using namespace std;

int main()
{
    int T;
    string k;

    int a,ans,no;
    ifstream input;
    input.open("input");
    ofstream myfile;
	myfile.open("output.txt");
    
	input>>T;

    for(int i=1;i<=T;i++)
    {
        ans=0;
        no=0;
        input>>a>>k;
        for(int j=0;j<=a;j++)
        {
            if (j>no)
            {
                ans+=j-no;
                no=j;
            }
            no+=k[j]-'0';
        }
       	myfile<<"Case #"<<i<<": "<<ans<<endl;
    }
}
