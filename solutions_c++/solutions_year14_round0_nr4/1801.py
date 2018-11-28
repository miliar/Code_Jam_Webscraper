#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define vi vector<int>
#define vvi vector< vi >
#define vs vector<string>
#define rep(i,s,e) for(int i=s;i<=e;i++)
#define fori(s,e) for(i=s;i<=e;i++)
#define forj(s,e) for(j=s;j<=e;j++)
#define fork(s,e) for(k=s;k<=e;k++)
#define ull unsigned long long
#define ll signed long long
#define imax INT_MAX
#define imin INT_MIN
#define sz(x) (int)x.size()
#define ppb pop_back
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x));
#define pii pair<int,int>
#define in(c,x) scanf("%"#c,&x);
#define out(c,x) printf("%"#c,x);
#define aa first
#define bb second
#define MOD 1000000007

using namespace std;

int main()
{
	int i, j, k;
	int caseno, t, vella;
	FILE *in, *out;
    in = fopen ("D-large.in", "r");
    out = fopen ("A-small-practice.out", "w");
	fscanf (in, "%d", &t);
	for (caseno = 1; caseno <= t; caseno ++)
	{
		fprintf (out, "Case #%d: ", caseno);
        int n;
        vector <double> naomi, ken, naomis, kens;
        double temp;
        fscanf (in, "%d", &n);
        fori (0, n - 1)
            {fscanf (in, "%lf", &temp); naomi.pb(temp);}
        fgetc(in);
        fori (0, n - 1)
            {fscanf (in, "%lf", &temp); ken.pb(temp);}
        naomis = naomi;
        kens = ken;
        sort(naomis.begin(), naomis.end());
        sort(kens.begin(), kens.end());
        vector <double> :: iterator it;
        //deceitful
        int deceit = 0;
        vector <double> v;
        string nk;
        for (i = 0, j = 0; i < n && j < n;)
        {
            if (kens[i] < naomis[j])
            {
                v.pb(kens[i ++]);
                nk.pb('k');
            }
            else
            {
                v.pb(naomis[j]);
                j ++;
                nk.pb('n');
            }
        }
        if (i != n)
        {
            while (i < n)
            {
                v.pb(kens[i ++]);
                nk.pb('k');
            }
        }
        else if (j != n)
        {
            while (j < n)
            {
                v.pb(naomis[j ++]);
                nk.pb('n');
            }
        }
        vella = 0, deceit = 0;
        fori (0, nk.size() - 1)
        {
            if (nk[i] == 'k')
                vella ++;
            else
            {
                if (vella != 0)
                {
                    vella --;
                    deceit ++;
                }
            }
        }
        //war

        int war = 0, idx = -1;
        fori (0, n - 1)
        {
            idx = -1;
            for (it = kens.begin(); it != kens.end(); it ++)
                if (*it > naomi[i])
                {
                    idx = 1;
                    war ++;
                    break;
                }
            if (idx != -1)
                kens.erase(it);
        }
        fprintf (out, "%d %d\n", deceit, n - war);
	}
	return 0;
}
