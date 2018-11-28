#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <vector>
#include <sstream>
#include <iostream>
#include<time.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> paii;


#define PI (2*acos(0))
#define ERR 1e-5
#define mem(a,b) memset(a,b,sizeof a)
#define pb push_back
#define popb pop_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define SZ(x) (int)x.size()
#define oo (1<<25)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define Contains(X,item)        ((X).find(item) != (X).end())
#define popc(i) (__builtin_popcount(i))
#define fs      first
#define sc      second
#define EQ(a,b)     (fabs(a-b)<ERR)
#define MAX 15050
#define wait getchar()

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t,row1,row2,arr1[5][5],arr2[5][5],loop=1;
    vector<int>v;
    scanf("%d",&t);
    while(t--)
    {
        v.clear();
        scanf("%d",&row1); row1--;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) scanf("%d",&arr1[i][j]);
        scanf("%d",&row2); row2--;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) scanf("%d",&arr2[i][j]);

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(arr1[row1][i]==arr2[row2][j]) v.pb(arr1[row1][i]);

        if(SZ(v)==1) printf("Case #%d: %d\n",loop++,v[0]);
        else if(SZ(v)>1) printf("Case #%d: Bad magician!\n",loop++);
        else if(SZ(v)==0) printf("Case #%d: Volunteer cheated!\n",loop++);

    }
    return 0;
}

