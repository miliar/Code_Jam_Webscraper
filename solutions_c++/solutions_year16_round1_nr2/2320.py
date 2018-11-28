#include<iostream>
#include <assert.h>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define sss(n, size) fgets(n, size, stdin)
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define V(x) vector<x>

ll gcd(ll r0, ll r1)
{
    if(r0==0 || r1==0)
    return 1;

    if(r0<r1)
    return gcd(r1,r0);

    if(r0%r1==0)
    return r1;

    return gcd(r1,r0%r1);
}
ll findInverse(ll a, ll b)
{
    ll x[3];
    ll y[3];
    ll quotient  = a / b;
    ll remainder = a % b;
    x[0] = 0;
    y[0] = 1;
    x[1] = 1;
    y[1] = quotient * -1;

    ll i = 2;
    for (; (b % (a%b)) != 0; i++)
    {
        a = b;
        b = remainder;
        quotient = a / b;
        remainder = a % b;
        x[i % 3] = (quotient * -1 * x[(i - 1) % 3]) + x[(i - 2) % 3];
        y[i % 3] = (quotient * -1 * y[(i - 1) % 3]) + y[(i - 2) % 3];
    }
    //x[i — 1 % 3] is inverse of a
    //y[i — 1 % 3] is inverse of b
    return x[(i - 1) % 3];
}

int t,n, m;

struct list {
  int l[100];
};
bool myfunction(list i,list j)    //use it to sort vectors
{
  return i.l[0] < j.l[0];
}

list a[200], temp[200];
int d[200];

int checkr(int v) {
  int nd[100];
  REP(i, n) {
    nd[i] = 0;
  }
  REP(i, m) {
    if (d[i] == v) {
        int flag = 0;
        REP(j, n) {
          if (nd[j] == 0 && a[i].l[0] == temp[0].l[j]) {
            REP(k, n) {
              if (a[i].l[k] != temp[k].l[j]) {
                return -1;
              }
            }
            nd[j] = 1;
            flag = 1;
          }
        }
        if (!flag) {
          return -1;
        }
    }
  }
  REP(i, n) {
    if (nd[i] == 0) {
      return i;
    }
  }
  return -1;
}

void print() {
  REP(i, n) {
    REP(j, n) {
       cout<<temp[i].l[j]<<" ";
    }
    cout<<endl;
  }
}

int main() {

  si(t);
  REP(prob, t) {
    si(n);
    m = 2*n-1;
    REP(i, m) {
      REP(j, n) {
        si(a[i].l[j]);
      }
    }
    m = 2*n-1;
    int times = 1 << (2*n-1);
    list ans;
    REP(at,times) {
      int cnt = 0;
      int tx = at;
      REP(i, m) {
        d[i] = tx%2;
        tx /= 2;
        if (d[i] == 0) {
          cnt++;
        }
      }
      int tat = 0;
      if (cnt == n) {
        REP(i, m) {
          if (d[i] == 0) {
            temp[tat] = a[i];
            tat++;
          }
        }
        //print();
        sort(temp, temp+n, myfunction);
        //print();
        int c = checkr(1);
        if (c >= 0) {
          REP(i, n) {
            ans.l[i] = temp[i].l[c];
          }
          break;
        }
      } else if (cnt == n-1) {
        REP(i, m) {
          if (d[i] == 1) {
            temp[tat] = a[i];
            tat++;
          }
        }
        sort(temp, temp+n, myfunction);
        //print();
        int c = checkr(0);
        if (c >= 0) {
          REP(i, n) {
            ans.l[i] = temp[i].l[c];
          }
          break;
        }
      }
    }
    printf("Case #%d:", prob+1);
    REP(i, n) {
      printf(" %d", ans.l[i]);
    }
    printf("\n");
  }

  //system("pause");
  return 0;
}
