#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <list>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <stack>
#include <map>
#include <iostream>
#include <string>
#include <set>

using namespace std;

//map<int, vector<int> > mapper;
//list<type> lister;
//set<type> seter;
#define ll long long

ll arr[200];
ll a,n;

ll get(ll now_step, ll now_num, ll level)
{
    if (level >= n)
        return now_step;

    ll s1;
    if (now_num == 1)
        return get(now_step+1, now_num, level+1);
    
    if (arr[level] < now_num)
        s1 = get(now_step, now_num+arr[level], level+1);
    else
        s1 = get(now_step+1, now_num+now_num-1, level);
    ll s2 = get(now_step+1, now_num, level+1);
    return min(s1, s2);
}

void func()
{
    cin >> a >>n;
    memset(arr,0,sizeof(arr));
    for (ll i=0; i<n;++i)
        cin >> arr[i];
    sort(arr, arr+n);

    ll step;
    ll s1;
    if (a == 1)
    {
        cout << get(1, a, 1) << endl;
        return;
    }

    if (arr[0] < a)
        s1 = get(0, a+arr[0], 1); 
    else
        s1 = get(1, a+a-1, 0);

    ll s2 = get(1, a, 1);
    cout << min(s1, s2) << endl;
}


//////////////////////////////

char in_file[] = "testa.in";
char out_file[] = "testa.out";

int main()
{
    int case_count, t;

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    cin >> case_count;
    for (t = 1; t <= case_count; t++)
    {
        cerr << "\nDealing Case #" << t << endl;
        cout << "Case #" << t << ": ";
        func();
    }

	return 0;    
}
