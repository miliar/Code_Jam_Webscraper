// Coder nyble
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;

#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(__typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define nl          printf("\n")

int main()
{
    int t;
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        int s;
        scanf("%d",&s);
        string shyStr;
        cin>>shyStr;
        int shyPersons[1005];
        for(int i=0;i<s+1;i++)
        {
            shyPersons[i] = shyStr[i] - 48;
        }
        int mxlvl=0, req=0;
        for(int i=0;i<s+1;i++)
        {
            if(i<=mxlvl)
            {
                mxlvl+=shyPersons[i];
                //cout<<"mxlvl : "<<mxlvl<<" i = "<<i<<" req = "<<req<<endl;
            }
            else
            {
                req += i-mxlvl;
                //cout<<"mxlvl : "<<mxlvl<<" i = "<<i<<" req = "<<req<<endl;
                mxlvl=i;
                i--;
            }
        }

        if(1)
        {
            printf("Case #%d: %d\n",z,req);
        }
    }
    return 0;
}
