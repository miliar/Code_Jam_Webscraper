#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <ctime>
#include <math.h>
#include <algorithm>
#include <iomanip>
#include <assert.h>
#include <map>
#include <queue>
#include <cstring>
#include <set>
using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;
#define vi vector<int>
#define vvi vector< vector<int> >
#define vd vector<double>
#define vb vector<bool>
#define vs vector<string>
#define pi pair<int,int>
#define pb push_back
#define out(a) cout<<(a)<<endl
#define pout(a,b) cout<<(a)<<' '<<(b)<<endl
#define sz(c) (int)(c).size()
#define foreach(n,i) for(int (i)=0;(i)<(n);(i)++)
#define range(s,e,i) for(int (i)=(s);(i)<=(e);(i)++)
#define all(c) (c).begin(),(c).end()
template<typename typ> void vout(vector<typ>& v){for(int vint=0;vint<sz(v);vint++)cout<<(v)[vint]<<' ';cout<<endl;}
template<typename typ> void arrout(typ* arr,int l){for(int i=0;i<l;i++)cout<<arr[i]<<' ';cout<<endl;}

#define debug
#ifdef debug
#define dbg(a) cout << #a << ' ' << a << endl
#endif
#ifndef debug
#define dbg(a)
#endif

int main()
{
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; ++t)
    {
        printf("Case #%d: ",t);
        int n,m;
        cin >> n >> m;
        int lawn[n][m];
        for(int i = 0 ; i < n ; ++i)
            for(int j = 0 ; j < m ; ++j)
                scanf("%d",&lawn[i][j]);

        int row[n],col[m];
        memset(row,0,sizeof(row));
        memset(col,0,sizeof(col));
        for(int i = 0 ; i < n ; ++i)
            for(int j = 0 ; j < m ; ++j)
            {
                row[i] = max(row[i], lawn[i][j]);
                col[j] = max(col[j], lawn[i][j]);
            }

        int uncut[n][m];
        for(int i = 0 ; i < n ; ++i)
            for(int j = 0 ; j < m ; ++j)
                uncut[i][j] = 100000;
        for(int i = 0 ; i < n ; ++i)
            for(int j = 0 ; j < m ; ++j)
            {
                if( lawn[i][j] == row[i] )
                {
                    for(int k = 0 ; k < m ; ++k)
                        uncut[i][k] = min(uncut[i][k], row[i]);
                }
                if( lawn[i][j] == col[j] )
                {
                    for(int k = 0 ; k < n ; ++k)
                        uncut[k][j] = min(uncut[k][j], col[j]);
                }
            }
        bool works = true;
        for(int i = 0 ; i < n ; ++i)
            for(int j = 0 ; j < m ; ++j)
                if( lawn[i][j] != uncut[i][j] )
                {
                    works = false;
                    break;
                }
        if( works )
            printf("YES\n");
        else
            printf("NO\n");
    }
}