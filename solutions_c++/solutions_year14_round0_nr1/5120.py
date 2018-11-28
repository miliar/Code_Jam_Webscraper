#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <string.h>

#define SZ(c) c.size()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define SORT(a) sort(a.begin(),a.end())
#define tests int test; scanf("%d",&test); while(test--)
#define dbg(n) cout<<#n<<" = "<<n<<endl;

using namespace std;

int strToInt(string str) {int ans; stringstream s; s<<str; s>>ans; return ans;}
string intToStr(int n) {string str; stringstream s; s<<n; s>>str; return str;}
int MAX(int a,int b) {if(a >b) return a; return b;}
int MIN(int a,int b) {if(a <b) return a; return b;}
int ABS(int a) {if(a >0) return a; return -a;}

int debug = 0;

int main()
{
    freopen("A-small-attempt0.txt", "r", stdin);
    freopen("writeAA.txt", "w", stdout);
    int test;
    scanf("%d",&test);
    int row;
    int arr[4][4];
    int numbers[17];
    for(int current =1; current <=test; current++)
    {
        for(int i=1; i<17; i++)
            numbers[i] =0;
        scanf("%d",&row);
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d", &arr[i][j]);

        for(int j=0; j<4;j++)
            numbers[arr[row-1][j]]++;

        scanf("%d", &row);
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            scanf("%d", &arr[i][j]);
        for(int j=0; j<4; j++)
            numbers[arr[row-1][j]]++;

        if(debug)
        {
            for(int i=1; i<17; i++)
                printf("%d[%d] ",i, numbers[i]);
        }


        int counter =0, ans =0;
        for(int i=1; i<17; i++)
            if(numbers[i] == 2)
        {
            counter++;
            ans = i;
        }

        if(counter ==1)
        {
            printf("Case #%d: %d\n", current, ans);
        }
        else if(counter >1)
        {
            printf("Case #%d: Bad magician!\n", current);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n", current);

        }

    }

    return 0;
}

