/*
written by- Piyush Golani
language- c++
country- India
College- N.I.T Jamshedpur
*/
#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<map>
#include<set>
#include<queue>
#include<cctype>
using namespace std;
#define pb push_back
#define all(s) s.begin(),s.end()
#define f(i,a,b) for(int i=a;i<b;i++)
#define F(i,a,b) for(int i=a;i>=b;i--)
#define PI 3.1415926535897932384626433832795
#define INF 2000000000
#define BIG_INF 7000000000000000000LL
#define mp make_pair
#define eps 1e-9
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define mod 1000000007
#define mm 10000000

typedef long long LL;


string inttostring(int n)
{
    stringstream a;
    a<<n;
    return a.str();
}

int stringtoint(string A)
{
    istringstream a(A);
    int p;
    a>>p;
    return p;
}

//////////////////////////////////////////////////////


int ch(string A)
{
    if(A=="XXXT" || A=="XXXX") return 1;
    if(A=="OOOT" || A=="OOOO") return 2;
    reverse(all(A));
    if(A=="XXXT" || A=="XXXX") return 1;
    if(A=="OOOT" || A=="OOOO") return 2;
    else return -1;
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("pp.txt","w",stdout);
    int t,u=1;
    si(t);
    while(t--)
    {
        int xx=0;
        char A[5][5];
        f(i,0,4)
        {
            f(j,0,4) {cin>>A[i][j];
            if(A[i][j]=='.') xx=1;}
        }
        bool gg=false;
        int a;
        string B;
        f(i,0,4)
        {
            B="";
            f(j,0,4)
            {
                B+=A[i][j];
            }
            int c=ch(B);
            if(c!=-1)
            {
                a=c;
                gg=true;
                break;
            }
        }
        if(!gg)
        {
            f(j,0,4)
            {
                B="";
                f(i,0,4)
                {
                    B+=A[i][j];
                }
                int c=ch(B);
                if(c!=-1)
                {
                    a=c;
                    gg=true;
                    break;
                }
            }
        }
        if(!gg)
        {
            B="";
            B+=A[0][0];
            B+=A[1][1];
            B+=A[2][2];
            B+=A[3][3];
            int c=ch(B);
            if(c!=-1)
                {
                    a=c;
                    gg=true;
                    //break;
                }

        }
        ////////////
        if(!gg)
        {
            B="";
            B+=A[0][3];
            B+=A[1][2];
            B+=A[2][1];
            B+=A[3][0];
            int c=ch(B);
            if(c!=-1)
                {
                    a=c;
                    gg=true;
                    //break;
                }

        }
        if(!gg)
        {
            if(xx==1)
            {
                a=3;
            }
            else a=4;
        }
        string res;
        if(a==1) res="X won";
        if(a==2) res="O won";
        if(a==3) res="Game has not completed";
        if(a==4) res="Draw";
        cout<<"Case #"<<u++<<": "<<res<<"\n";
    }
}
