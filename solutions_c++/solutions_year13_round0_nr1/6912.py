/**
	* Author: Arif
	* Date:
*/

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <iomanip>
using namespace std;

#define INF_MAX 	2147483647
#define INF_MIN 	-2147483648
#define INF 		(1 << 30)
#define EPS			1e-9
#define PI 			acos(-1.0)
#define N 		    2 + 1000000
#define MOD			10000000007
#define sz(x) 		(int)(x).size()
#define all(x) 		(x).begin(), (x).end()
#define pb 			push_back
#define mp			make_pair
#define ms(x, a) 	memset((x), (a), sizeof(x))
#define F           first
#define S           second
#define rep(i,a,b)  for(int i=(a); i<(b); i++)
#define repC(i,x) 	for(size_t i=0; i<x.size(); i++)
#define repIT(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

typedef long long 		LL;
typedef pair<int,int> 	pii;
typedef vector<int> 	vi;
typedef vector<string> 	vs;
typedef vector<char>	vc;
typedef vector<bool>    vb;
typedef map<string,int> msi;
typedef map<int,int>	mii;
typedef map<char,int>   mci;
typedef map<int,string>	mis;

template<class T> T Abs(T x) {return x>0 ? x : -x;}
template<class T> T Max(T a, T b) {return a>b ? a : b;}
template<class T> T Min(T a, T b) {return a<b ? a : b;}
template<class T> T gcd(T a, T b) {return a%b==0 ? b : gcd(b,a%b);}
bool isVowel(char ch){ch=tolower(ch);return(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u');}


int main()
{
	#ifndef ONLINE_JUDGE
		freopen("A-large.in", "r", stdin);
		freopen("Aout.txt", "w", stdout);
	#endif

	int i, j, k, n, tc;
	string s[6];

    cin >> tc;
    cin.ignore();
	rep(cn, 1, tc+1)
	{
        rep(i, 0, 4) getline(cin, s[i]);
        cin.ignore();

        int xCount, oCount, dotCount = 0, tCount;
        bool xWon = false, oWon = false, draw = false, gotResult = false;

        // check row
        rep(i, 0, 4)
        {
            xCount = oCount = tCount = 0;
            rep(j, 0, 4)
                if(s[i][j] == 'X') xCount++;
                else if(s[i][j] == 'O') oCount++;
                else if(s[i][j] == 'T') tCount++;
                else dotCount++;

            if(xCount+tCount == 4)
            {
                xWon = true;
                gotResult = true;
                break;
            }
            else if(oCount+tCount == 4)
            {
                oWon = true;
                gotResult = true;
                break;
            }
        } // end checking row

        // check column
        if(!gotResult) rep(j, 0, 4)
        {
            xCount = oCount = tCount = 0;
            rep(i, 0, 4)
                if(s[i][j] == 'X') xCount++;
                else if(s[i][j] == 'O') oCount++;
                else if(s[i][j] == 'T') tCount++;
                else dotCount++;

            if(xCount+tCount == 4)
            {
                xWon = true;
                gotResult = true;
                break;
            }
            else if(oCount+tCount == 4)
            {
                oWon = true;
                gotResult = true;
                break;
            }
        } // end checking column

        // check left-right diagonal
        if(!gotResult)
        {
            xCount = oCount = tCount = 0;
            rep(i, 0, 4)
            {
                if(s[i][i] == 'X') xCount++;
                else if(s[i][i] == 'O') oCount++;
                else if(s[i][i] == 'T') tCount++;
                else dotCount++;
            }
            if(xCount+tCount == 4) xWon = gotResult = true;
            else if(oCount+tCount == 4) oWon = gotResult = true;
        }

        // check right-left diagonal
        if(!gotResult)
        {
            xCount = oCount = tCount = 0;
            for(i=0,j=3; i<4; i++,j--)
            {
                if(s[i][j] == 'X') xCount++;
                else if(s[i][j] == 'O') oCount++;
                else if(s[i][j] == 'T') tCount++;
                else dotCount++;
            }
            if(xCount+tCount == 4) xWon = gotResult = true;
            else if(oCount+tCount == 4) oWon = gotResult = true;
        }

        if(!gotResult && !dotCount) draw = true;

        printf("Case #%d: ", cn);
        if(xWon) puts("X won");
        else if(oWon) puts("O won");
        else if(draw) puts("Draw");
        else puts("Game has not completed");
    }

	return 0;
}
