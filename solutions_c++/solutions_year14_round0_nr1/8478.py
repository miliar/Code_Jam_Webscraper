#define CRT_SECURE_NO_WARNINGS 1

#include <string>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctime>
#include <limits.h>
#include <bitset>
#include <functional>
#include <numeric>
#include <complex>

typedef long long unsigned int llu;
typedef long long int lld;
typedef long long ll;

using namespace std;

#define MOD 1000000007LL
#define returnzero1 return 0;
#define SWAP(a,b) (((a) ^= (b)), ((b) ^= (a)), ((a) ^= (b)))
#define refresh(arr, n, k) REP(i, n) arr[i]=k
#define in_arr(arr, n) REP(i, n) si(arr[i])
#define copy_arr(arr1, arr2, n) REP(i, n) arr2[i]=arr1[i]
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?-(x):(x))
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define FORR(i,n) for(int i=(n);i>=0;i--)
#define REV(i,n) for(int i=(n);i>=1;i--)
#define DB(x) cout<<#x<<" = "<<(x)<<"\n";
#define si(n) scanf("%d",&n);
#define pf(n) printf("%d",n);
#define pn(n) printf("%d\n",n);

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, a, b, matrix1[4][4], matrix2[4][4], arr[20], counter2, index, testcase = 0;
    si(t)
    while(t--)
    {
        counter2 = index = 0;
        testcase += 1;
        refresh(arr, 20, 0);
    	si(a)
    	REP(i, 4)
    	{
    		REP(j, 4)
    			si(matrix1[i][j])
    	}
    	si(b)
    	REP(i, 4)
    	{
    		REP(j, 4)
    			si(matrix2[i][j])
    	}
    	REP(i, 4)
        {
            arr[matrix1[a-1][i]] += 1;
            arr[matrix2[b-1][i]] += 1;
        }
        REP(i, 20)
        {
            if(arr[i] == 2){
                counter2 += 1;
                index = i;
            }
        }
        cout<<"Case #"<<testcase<<": ";
        if(counter2 == 1)
            pn(index)
        else if(counter2 > 1)
            puts("Bad magician!");
        else
            puts("Volunteer cheated!");
    }
    returnzero1
}