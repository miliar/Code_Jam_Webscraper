#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <climits>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>

#define pii pair<int,int>
#define vi vector<int>

#define mp make_pair
#define pb push_back
#define F first
#define S second
#define MOD 1000000007
#define PI 3.14159265358979323846

#define POS(x) ((x)<0?(-1*(x)):(x))
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))

#define sz(c) (int)(c.size())
#define all(c) c.begin(), c.end()

using namespace std;

char in[1123];
FILE *fr = fopen("input.txt","r");
FILE *fw = fopen("output.txt","w");

int main()
{
    int tc, x;
    fscanf(fr, "%d", &tc);

    for(int t=1 ; t<=tc ; t++)
    {
        fscanf(fr, "%d %s", &x, in);
        long long ans = 0, curr = 0;

        for(int i=0 ; in[i] != '\0' ; i++)
        {
            if(in[i]=='0')
                continue;

            if(curr >= i)
                curr += (in[i]-'0');

            else
            {
                ans += (i-curr);
                curr += (i-curr);
                curr += in[i]-'0';
            }
        }

        fprintf(fw, "Case #%d: %I64d\n", t, ans);
    }

	return 0;
}

