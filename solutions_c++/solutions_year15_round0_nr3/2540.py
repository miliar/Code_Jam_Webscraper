#include <bits/stdc++.h>
using namespace std;

#define maxsiz 1000000
#define mod 1000000007
#define F first
#define S second
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%llu",&a)
#define pi(a) printf("%d",a)
#define pl(a) printf("%llu",a)
#define fr(i,k,n) for(int i = k ; i < n ; i++ )
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define printvect(a,n) fr(i,0,n) cout << a[i] << " " ;
typedef unsigned long long int ull;

int mul(int a,int b)
{
	if(a == 1)
		return b;
	if(b==1)
		return a;
	if(a==b)
		return -1;
	if(a == 3 && b == 2)
		return -4 ;
	if(a == 2 && b == 3)
		return 4 ;
	if(a == 4 && b == 2)
		return 3 ;
	if(a == 2 && b == 4)
		return -3 ;
	if(a == 4 && b == 3)
		return -2 ;
	if(a == 3 && b == 4)
		return 2 ;
}

int main()
{
	int test,l,x;
	cin >> test ;
	fr(t,0,test)
	{
		cin >> l >> x ;
		char c ;
		vector<int> s(l);
		fr(i,0,l) 
		{
			cin >> c ;
			s[i] = (int)(c-'i') +  2  ; 
		}
		if(l == 1)
		{
			cout << "Case #" << t+1 << ": NO" << endl;
			continue; 
		}

		bool flag = false;
		bool notavai = true;
		int current = 1 ;
		int found = 2 ; 
		int len2 = 0 ;
		int len3 = 0 ;
		int a[5];
		while(len2 < l*x-1)
		{
			len3 = len2 ;
			while(len3 < l*x -2)
			{
				fr(i,len3,l*x)
				{
					if(current > 0)
						current = mul(current,s[i%l]);
					else
						current = -1*mul(-1*current,s[i%l]);
					if(found == current)
					{
						a[found] = i ;
						current = 1 ;
						found++;
					}
				}
				if(current == 1 && found == 5)
				{
					flag = true;
					break;
				}
				else if(found  < 5)
				{
					notavai = false;
					break;
				}
				else
				{
					len3 = a[3] + 1 ;
					found = 3 ;
					current = 3 ;
				}
			}
			if(flag)
				break;
			else if(!notavai)
				break;
			else
			{
				len2 = a[2] + 1 ;
				found = 2 ;
				current = 2 ;
			}
		}
		if(flag)
			cout << "Case #" << t+1 << ": YES" << endl;
		else
			cout << "Case #" << t+1 << ": NO" << endl;
	}
	return 0 ;
}