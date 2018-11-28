#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <math.h>

#define ss stringstream
#define pb push_back
#define ppb pop_back
#define fo(a, b, c) for(a = (b); a < ( c ); a++ )
#define fr(a, b) fo(a, 0, ( b ) )
#define fi(a) fr(i, ( a ) )
#define fj(a) fr (j, ( a ) )
#define fk(a) fr(k, ( a ) )
#define _(a, b) memset(a, b, sizeof( a ) )

using namespace std;

int ni() { int a; cin>>a;  return a;}
char nc() { char a; cin>>a; return a;}
float nf() { float a; cin>>a; return a;}
long long  nll() { long long  a; cin>>a; return a;}

typedef long long ll;
typedef unsigned long long int lli;
typedef vector<int> vi;
typedef vector<string> vs;

#define MAX 100
#define MAX_HEIGHT 100

int l[MAX][MAX];
int r[MAX+1][MAX], c[MAX+1][MAX];

void init()
{
    int i, j;
    fi(MAX)
    fj(MAX)
        l[i][j] = MAX_HEIGHT;
    fi(MAX+1)
        fj(MAX)
        {
            r[i][j] = 1;
            c[i][j] = 1;
        }

}

int main()
{

    int tcase, flag1, flag2, n, m, i, j, k, tt;
    int mx;
    init();
    freopen("B-large.IN","r", stdin);
    freopen("B-large.OUT", "w", stdout);
    cin>>tt;
    fr(tcase, tt)
    {
        cout<<"Case #"<<tcase+1<<": ";
        cin>>n>>m;
        fi(n)
        fj(m)
            cin>>l[i][j];

        fi(n)
        fk(m)
        fj(m)
            if(l[i][k]<l[i][j])
             {
                 r[l[i][k]][i] = 0;
                 break;
             }
        fi(n)
        fk(m)
        {
            fj(n)
            {
                if(l[i][k]<l[j][k])
                {
                     c[l[i][k]][k] = 0;
                     break;
                }

            }
        }
        mx = l[0][0];
        fi(n)
        fj(m)
            if(l[i][j]>mx)
                mx = l[i][j];
        fi(n)
        {
            fj(m)
            {
                if(l[i][j]!=mx)
                    if(r[l[i][j]][i]!=1 && c[l[i][j]][j]!=1)
                    {
                        cout<<"NO"<<endl;
                        goto YES;
                    }

            }
        }

        cout<<"YES"<<endl;
        YES:
        init();
    }
}
