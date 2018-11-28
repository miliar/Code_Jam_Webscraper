/**************************************************
**  Author:  Aditya Goel                          *
**  NIT, Kurukshetra                              *  
**  INDIA                                         * 
**************************************************/

#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007  //NA
#define N 211111
#define inf 0x3f3f3f3f
#define ll long long int
#define dt ll
#define all(c) c.begin(), c.end()
#define dcl(a) memset(a,0,sizeof(a))
#define rep(i,a,b) for(dt i=a;i<=(dt)(b);i++)
#define tr(container, it) for(vector<dt> ::iterator it= container.begin(); it!=container.end(); it++)
#define trp(container, it) for(vector<pair<dt,dt> >::iterator it = container.begin(); it!=container.end(); it++)
#define tra(container, it) for(typeof(container.begin()) it = container.begin(); it!=container.end(); it++)
#define cc1(a)cout<<#a<<": "<<a<<endl;
#define cc2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<< endl;
#define cc3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<endl;
#define cc4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<endl;
#define pr pair<dt,dt>  //NA
#define mp(a,b) make_pair(a,b)
#define pb push_back  //NA
#define gc getchar  //NA
#define F first
#define S second
#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define print(tt, a) printf("Case #%lld: %lld", a);
#define vi vector<int>
#define vii vector<pair<int,int> >
#define pii pair<int,int>
#define plii pair<pair<ll, int>, int>
#define piii pair<pii, int>
#define viii vector<pair<pii, int> >
#define vl vector<int>
#define vll vector<pair<ll,ll> >
#define pll pair<ll,ll>
#define pli pair<ll,int>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
 
const int mod = 1e9 + 7;
 
int ADD(int a, int b, int m = mod) {
    int s = a;
    s += b;
    if( s >= m )
      s -= m;
    return s;
}
 
int MUL(int a, int b, int m = mod) {
    return (1LL * a * b % m);
}
 
int power(int a, int b, int m = mod) {
    int res = 1;
    while( b ) {
        if( b & 1 ) {
            res = 1LL * res * a % m;
        }
        a = 1LL * a * a % m;
        b /= 2;
    }
    return res;
}
 
ll nC2(ll x) {
    return ( x * ( x - 1 ) / 2 );
}
int main()
{
	freopen("in1.txt", "r", stdin);
	freopen("out1.txt", "w", stdout);
	int test;
	cin >> test;
	for(int tt = 1; tt <= test; tt++)
	{
		string s;
		int arr[100] = {0};
		cin >> s;
		int hash1[1000] = {0};
		rep(i, 0, s.length() - 1)
		{
			hash1[s.at(i) - 'A'] ++;
		}
		int z = hash1['Z' - 'A'];
		hash1['Z' - 'A'] -=z;
		hash1['E' - 'A'] -=z;
		hash1['R' - 'A'] -=z;
		hash1['0' - 'A'] -=z;
		arr[0] = z;
		int w = hash1['W' - 'A'];
		hash1['T' - 'A'] -=w;
		hash1['W' - 'A'] -=w;
		hash1['O' - 'A'] -=w;
		arr[2] = w;
		w = hash1['X' - 'A'];
		hash1['S' - 'A'] -=w;
		hash1['I' - 'A'] -=w;
		hash1['X' - 'A'] -=w;
		arr[6] = w;
		w = hash1['S' - 'A'];
		hash1['S' - 'A'] -=w;
		hash1['E' - 'A'] -=w;
		hash1['V' - 'A'] -=w;
		hash1['E' - 'A'] -=w;
		hash1['N' - 'A'] -=w;
//		hash1['V' - 'A'] -=w;
		arr[7] = w;
		w = hash1['V' - 'A'];
		hash1['F' - 'A'] -=w;
		hash1['I' - 'A'] -=w;
		hash1['V' - 'A'] -=w;
		
		hash1['E' - 'A'] -=w;
		arr[5] = w;
		w = hash1['F' - 'A'];
		hash1['F' - 'A'] -=w;
		hash1['O' - 'A'] -=w;
		hash1['U' - 'A'] -=w;
		hash1['R' - 'A'] -=w;
		arr[4] = w;
		w = hash1['R' - 'A'];
		hash1['T' - 'A'] -=w;
		hash1['H' - 'A'] -=w;
		hash1['R' - 'A'] -=w;
		hash1['E' - 'A'] -=w;
		hash1['E' - 'A'] -=w;
		arr[3] = w;
		w = hash1['T' - 'A'];
		hash1['E' - 'A'] -=w;
		hash1['I' - 'A'] -=w;
		hash1['G' - 'A'] -=w;
		hash1['H' - 'A'] -=w;
		hash1['T' - 'A'] -=w;
		arr[8] = w;
		w = hash1['I' - 'A'];
		hash1['N' - 'A'] -=w;
		hash1['I' - 'A'] -=w;
		hash1['N' - 'A'] -=w;
		hash1['E' - 'A'] -=w;
		arr[9] = w;
		w = hash1['E' - 'A'];
		hash1['O' - 'A'] -=w;
		hash1['N' - 'A'] -=w;
		hash1['E' - 'A'] -=w;
		arr[1] = w;
		printf("Case #%d: ", tt);
//		cout << '\n';
		
		for(int i = 0; i <= 9; i++)
		{
			if(arr[i])
			{
				
				for(int j = 0; j < arr[i]; j++)
				{
					cout << i;
				}
			}
		}
		cout << "\n";
	}
}
