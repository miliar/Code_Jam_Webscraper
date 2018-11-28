//coder: handa.vikalp
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
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

int main(int argc, char const *argv[])
{
	FILE *input = freopen("D-small-attempt0.in","r", stdin);
	FILE *output = freopen("D-small-0.out", "w", stdout);

	int T;
	scanf("%d",&T);
	for(int t = 1; t<=T; ++t)
	{
        int x,r,c, flag=0;
        scanf("%d%d%d", &x,&r,&c);
        if(1 == x) flag=1;
        else if(r*c < x) flag=0;
        else if(2 == x)
        {
            if((r*c)%x == 0) flag=1;
            else flag=0;
        }
        else if(3 == x)
        {
            if((r*c)%x ==0 )
            {
                if((r*c) == x) flag=0;
                else flag=1;
            }
            else flag=0;
        }
        else if(4 == x)
        {
            if((r*c)%x ==0 )
            {
                if((r*c) == x) flag=0;
                else if((r==2) || (c==2)) flag=0;
                else flag=1;
            }
            else flag=0;

        }
        else
        {
            if((r*c)%x ==0 )
            {
                if(r*c == x) flag=0;
                else flag=1;
            }
            else flag=0;

        }
        if(flag) printf("Case #%d: %s\n", t, "GABRIEL");
        else printf("Case #%d: %s\n", t, "RICHARD");
    }
    fclose(input);
    fclose(output);
    return 0;
}
