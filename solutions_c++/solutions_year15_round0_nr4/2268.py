
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <cmath>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <limits.h>
#include <time.h>
#include <bitset>
#include <list>
#include <cassert>

#define EPS 1e-11
#define PI acos(-1)
#define LL long long
#define INF 1000000009
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define SZ(a) ((int)a.size())
#define OPENR(a) freopen(a,"r",stdin)
#define OPENW(a) freopen(a,"w",stdout)
#define pii pair<int,int>

int x4[4] = { 0, 0,-1, 1};
int y4[4] = {-1, 1, 0, 0};
int x8[8] = {-1,-1,-1, 0, 0, 1, 1, 1};
int y8[8] = {-1, 0, 1,-1, 1,-1, 0, 1};
int xhorse[8] = {1,2,1,2,-1,-2,-1,-2};
int yhorse[8] = {2,1,-2,-1,2,1,-2,-1};

using namespace std;

int t;

int main()
{
    scanf("%d",&t);

    for (int tc=1;tc<=t;tc++)
    {
        int x,r,c;
        scanf("%d %d %d",&x,&r,&c);

        printf("Case #%d: ",tc);

        if (r*c < x) printf("RICHARD\n");
        else
        {
            if (x==1) printf("GABRIEL\n");
            else if (x==2)
            {
                if ((r*c)%2==0) printf("GABRIEL\n");
                else printf("RICHARD\n");
            }
            else if (x==3)
            {
                if ((r*c)%3==0 && (r>=2 || c>=2) && r>=2 && c>=2) printf("GABRIEL\n");
                else printf("RICHARD\n");
            }
            else if (x==4)
            {
                if ((r*c)%4==0 && (r!=2 && c!=2) && r>=3 && c>=3) printf("GABRIEL\n");
                else printf("RICHARD\n");
            }
        }
    }


    return 0;
}
