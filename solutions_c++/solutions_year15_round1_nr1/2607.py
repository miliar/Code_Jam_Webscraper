#include <iterator>
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
///#include<bits/stdc++.h>


using namespace std ;

typedef long long ll; ///NOTES:int64
typedef vector<int> vi;
typedef pair<int,int> pii;


const double eps = 1e-10; ///NOTES:eps
const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
const double pi = acos(-1.0); ///NOTES:pi
const int MAX_INT = (1<<30) ; /// 10^9
const ll MAX_LL = (1LL<<62) ; /// 10^18

#define SZ(x)           (int)x.size()
#define ALL(x)          (x).begin(),(x).end()
#define ALLR(x)         (x).rbegin(),(x).rend()
#define PB( x )         push_back(x)
#define MP(x , y)       make_pair(x,y)
#define rep(i,st,en)    for(int i=st ; i< en; i++)
#define repR(i,st,en)   for(int i=st;i>=en ; i--)


///-----------*  Topcoder Contest class  *-----------------///////////////////
class
RandomPancakeStackDiv2
{
public :



};
///----------------------------------------------------------------------------------




int arr[10000];
///----------------------------------------------///
int main()
{

freopen("in.txt" , "rt",stdin) ;
freopen("out.txt", "wt", stdout);

int nTest;
cin >> nTest ;
rep(t,1,nTest+1)
{
    int n ;
    cin >> n ;
    rep(i,0,n)
        cin >> arr[i] ;
    int c1 = 0 , c2 = 0 , mxDiff = 0;
    rep(i,1,n)
    {
        if(arr[i]<arr[i-1])
        {
            c1+= arr[i-1]-arr[i];
            mxDiff = max(mxDiff , arr[i-1]-arr[i]);
        }


    }
    rep(i,0,n-1)
    {
        if(arr[i]<mxDiff)
            c2+=arr[i];
        else
            c2+=mxDiff ;
    }

    cout << "Case #" << t << ": " << c1 << ' ' << c2 << '\n';




}

return 0;
}




