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

int main()
{
	
	freopen("adi.txt", "r", stdin);
	freopen("maa.txt", "w", stdout);
	int test;
	sd(test);
	for(int tt = 1; tt <= test; tt++)
	{
		int n, soldier;
		cin >> n;
		int hash[50000] = {0}, list[n + 5];
		memset(hash, 0, sizeof hash);
		for(int i = 0; i < 2 * n - 1; i++)
		{
			for(int j = 0; j < n; j++)
			{
	
				sd(soldier);
				hash[soldier]++;
			}
		}
		int li = 0;
		for(int i = 1; i <= 2500; i++)
		{
			if(hash[i] & 1)
			{
				list[li++] = i;
			}
		}
		printf("Case #%d: ", tt);
		for(int i = 0; i < li; i++)
		{
			cout << list[i] << " ";
		}
		cout << "\n";
	}
	return 0;
}
