#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

#define frl(a, b, c) for( (a) = (b);( a) < (c); (a++))
#define fru(a, b, c) for( (a) = (b); (a) <= (c); (a++))
#define frd(a, b, c) for( (a) = (b); (a) >= (c); (a--))
#define mst(a, b) memset(a, b, sizeof(a))
#define si(a) scanf("%d", &a)
#define ss(a) scanf("%s", a)
#define sc(a) scanf("%c", &a)

#define pb(a) push_back(a)
#define mp make_pair
#define nwl puts("");
#define sp << " " <<

#define sz size()
#define bg begin()
#define en end()
#define X first
#define Y second

#define vi vector <int>
#define vs vector <string>
#define ll long long int
#define dec int i = 0, j= 0, k = 0;

#define i(n) cin >> n;
#define p(s) cout << s;
#define pau system("pause");
int a[10004];
int taken[10004];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){

        int n, x;
        cin >> n>> x;
        for(int j = 0; j < n; j++)
            cin >> a[j];
        sort(a, a+n);
//        for(int j = 0; j < n; j++)
//            cout <<  a[j] << " ";
        mst(taken, 0);
        int cnt = 0;
        while(1){
            bool flag = false;
            int cap = x;
            int j = n-1;
            int no = 0;
            while(cap > 0 && j >= 0 && no < 2){
                if(!taken[j] && cap >= a[j]){
                    taken[j] = 1, cap = cap-a[j], flag = true, no++;
//                    cout << a[j] << " ";

                }
                j--;
            }
            if(flag == false)
                break;
            cnt++;
//            cout << endl;
        }
        cout << "Case #" << i << ": " << cnt << endl;
    }
}
