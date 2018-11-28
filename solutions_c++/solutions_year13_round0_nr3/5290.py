/*
LANG: C++
TASK: xxx
*/
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<sstream>

using namespace std;
#define x first
#define y second

#define FOR(i,a,b) for(__typeof(b)i = a; i < b;i++)
#define FORE(i,a,b) for(__typeof(b)i = a; i <= b;i++)
#define FOR_R(i,a,b) for(__typeof(b)i = a; i > b;i--)
#define FORE_R(i,a,b) for(__typeof(b)i = a; i >= b;i--)
#define TR(it , c) for(__typeof((c).end())it = (c).begin(); it != (c).end();it++)

string convertInt(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}
bool isPal(int i)
{
    string tmp = convertInt(i);
    for(int i=0;i<=tmp.size()/2;i++)
    {
        if(tmp[i] != tmp[tmp.size()-i-1]) return false;
    }
    return true;
}
bool isSquare(int i)
{
    return ((sqrt(i)*sqrt(i)) == i) && isPal(sqrt(i));
}
int tCase;
int solve(int tt)
{
    int a,b;
    printf("Case #%d: ",tt);
    int cnt = 0;
    scanf("%d %d",&a,&b);

    FORE(i , a , b)
    {
        if(isPal(i) == true && isSquare(i))
        {
            cnt++;
        }
    }
    printf("%d\n",cnt);
}


int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
    cin >> tCase;
    FOR(tt , 0 , tCase)
    {
        solve(tt+1);
    }
    return 0;
}

