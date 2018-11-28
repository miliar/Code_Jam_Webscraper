#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>

#define sqr(a) ((a)*(a))
#define ABS(A) ((a)>0 ? (a) : -(a))
#define MIN(a,b) ((a)>(b) ? (b) : (a))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define fi first
#define se second

typedef long long ll;

using namespace std;

int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    ll t, i;
    cin>> t;
    map < pair<char, char>, char> ms;
    map < pair<char, char>, int> mas;


    ms[mp('1', '1')] = '1';
    ms[mp('1', 'i')] = 'i';
    ms[mp('1', 'j')] = 'j';
    ms[mp('1', 'k')] = 'k';

    ms[mp('i', '1')] = 'i';
    ms[mp('i', 'i')] = '1';
    ms[mp('i', 'j')] = 'k';
    ms[mp('i', 'k')] = 'j';

    ms[mp('j', '1')] = 'j';
    ms[mp('j', 'i')] = 'k';
    ms[mp('j', 'j')] = '1';
    ms[mp('j', 'k')] = 'i';

    ms[mp('k', '1')] = 'k';
    ms[mp('k', 'i')] = 'j';
    ms[mp('k', 'j')] = 'i';
    ms[mp('k', 'k')] = '1';

    mas[mp('i', 'k')] = 1;
    mas[mp('j', 'i')] = 1;
    mas[mp('k', 'j')] = 1;
    mas[mp('i', 'i')] = 1;
    mas[mp('j', 'j')] = 1;
    mas[mp('k', 'k')] = 1;

    for(i = 1;  i <= t; i++)
    {
        ll n, j, x, k, zn = 1, f1 = 1, f2 = 1, f3 = 1;
        char c[50005], t[50005];
        cin>> n >> x;

        for(j = 1; j <= n; j++)
            cin>>c[j];

        for(k = 0; k < x; k++)
            for(j = 1; j <= n; j++)
                t[n * k + j] = c[j];

        for(j = 1; j <= n * x; j++)
        {

            char q = '1';
            if(f1) t[1] = t[j], f1 = 0;
                else
                    if(t[1] != 'i')
                    {
                        q = ms[mp(t[1], t[j])];
                        if(mas[mp(t[1], t[j])]) zn *=(-1);
                        t[1] = q;
                    }
                else
            if(f2) t[2] = t[j], f2 = 0;
                else
                    if(t[2] != 'j')
                {
                        q = ms[mp(t[2], t[j])];
                        if(mas[mp(t[2], t[j])]) zn *=(-1);
                        t[2] = q;
                }
                else
           if(f3) t[3] = t[j], f3 = 0;
                else
                    {
                            q = ms[mp(t[3], t[j])];
                            if(mas[mp(t[3], t[j])]) zn *=(-1);
                            t[3] = q;
                    }
            if(q == '-1') zn *=(-1);
            if(q == '-i') zn *=(-1);
            if(q == '-j') zn *=(-1);
            if(q == '-k') zn *=(-1);

        }

        cout<<"Case #"<<i<<": ";

        if(n * x >= 3 && t[1] == 'i' && t[2] == 'j' && t[3] == 'k' && zn == 1)
            cout<<"YES"<<endl; else
                cout<<"NO"<<endl;

    }
    return 0;
}

