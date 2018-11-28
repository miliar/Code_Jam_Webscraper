#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
int a[100][100];
int r[100],c[100];
int main()
{
    int n,m,i,j,k,x,t,T;
    cin >> t;
    T=t;
    while(t--)
    {
        int cant=0;
        cin >>n>>m;
        for(int i=0;i<n;i++)r[i]=0;
        for(int i=0;i<m;i++)c[i]=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                cin >> a[i][j];
                if(a[i][j]> r[i])r[i]=a[i][j];
                if(a[i][j]> c[j])c[j]=a[i][j];
            }
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(a[i][j]!= r[i] && a[i][j]!=c[j])
                {
                    cant=1;
                    break;
                }
            }
        cout << "Case #"<<T-t<<": ";
        if(cant)
            cout << "NO\n";
        else
            cout << "YES\n";

    }

}

