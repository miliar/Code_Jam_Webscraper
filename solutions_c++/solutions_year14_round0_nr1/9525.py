#include<cstdio>
#include<cmath>
#include<iostream>
#include<set>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<cstring>
#include<map>
#include<iterator>
#include<sstream>
#include<stack>
#include<queue>
#include<limits.h>
#define fi(a, b) for(int i=a; i<b; i++)
#define fj(a, b) for(int j=a; j<b; j++)
#define fk(a, b) for(int k=a; k<b; k++)
#define SZ(x) (int)x.size()
#define pp() pop_back()
#define pb(x) push_back(x)
#define mp make_pair
#define sf scanf
#define pf printf
#define ssf sscanf
#define rsrt(x) sort(x.rbegin(), x.rend())
#define srt(x) sort(x.begin(), x.end())
#define mem(name, value) memset(name, value, sizeof(name))
#define Max 1000
#define oo 1000000000
//#include<conio.h>
//#define WT getch()


using namespace std;

typedef pair<int, int>ii;
map<string, int>stin;
map<char, int>chin;
map<int, int>inin;
map<string, string>stst;
map<vector<string>, int>vsin;
typedef vector<int>vi;
typedef vector<string>vs;
typedef vector<char>vc;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef char C;
typedef string S;
//int dx[4] = {+0,-1,+0,+1}, dy[4] = {-1,+0,+1,+0}; /*row and column moves*/
//int dx[8] = {-1,-1,-1,+0,+1,+1,+1,+0}, dy[8] = {-1,0,+1,+1,+1,0,-1,-1};/*8-direction*/
/**
knight moves:
dx[8] = {-1,-2,-2,-1,+1,+2,+2,+1};
dy[8] = {-2,-1,+1,+2,+2,+1,-1,-2};
*/

struct type
{
    type() {}
};

typedef vector<type> vt;
typedef vector<ii> vii;

int arr1[5][5], arr2[5][5];

int call(int ans1, int ans2)
{
    vi store, vct;
    for(int j = 1; j <= 4; j++)
        store.pb(arr1[ans1][j]);
//    for(int i=0; i<store.size(); i++)
//        pf("%d\n", store[i]);

    for(int j = 1; j <= 4; j++)
    {
//        pf("arr2[%d] = %d\n", j, arr2[j])
        for(int k = 0; k<(int)store.size(); k++)
            if(store[k] == arr2[ans2][j])
            {
                vct.pb(store[k]);
            }
    }
    if((int)vct.size()==0)
        return -1;
    if((int)vct.size()>1)
        return 20;
    return vct[0];
}

void read(int cases)
{
    int ans1, ans2;
    sf("%d", &ans1);
    fi(1, 5) fj(1, 5) sf("%d", &arr1[i][j]);
    sf("%d", &ans2);
    fi(1, 5) fj(1, 5) sf("%d", &arr2[i][j]);
    int ans = call(ans1, ans2);
    pf("Case #%d: ", cases++);
    if(ans==-1)
        pf("Volunteer cheated!\n");
    else if(ans==20)
        pf("Bad magician!\n");
    else pf("%d\n", ans);
    return ;
}

int main()
{
//    freopen("A-small-attempt4.in", "r", stdin);
//    freopen("out.txt", "w", stdout);
    int test_cases, cases = 1;
    sf("%d", &test_cases);
    while(test_cases--)
    {
        read(cases++);
    }
    return 0;
}





















