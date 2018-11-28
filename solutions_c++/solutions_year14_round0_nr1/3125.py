// Coder nyble
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

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
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        int temp,found=0,ans1,ans2,ans;
        set<int> card1,card2;
        cin>>ans1;
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {
            scanf("%d",&temp);
            if(i==ans1)
            {
                card1.insert(temp);
            }
        }
         cin>>ans2;
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {
            scanf("%d",&temp);
            if(i==ans2)
            {
                card2.insert(temp);
            }
        }
        set<int>::iterator it1=card1.begin(),it2=card2.begin();
        for(;it1!=card1.end();++it1)
        {
            for(it2=card2.begin();it2!=card2.end();++it2)
            {
                if(*it1==*it2)
                {
                    found++;
                    ans=*it1;
                }
            }

        }
        if(found==1)
        {
            printf("Case #%d: %d\n",z,ans);
        }
        else if(found==0)
        {
            printf("Case #%d: Volunteer cheated!\n",z);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",z);
        }
    }
    return 0;
}
