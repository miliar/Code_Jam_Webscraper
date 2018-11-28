#include <bits/stdc++.h>
 
using namespace std; 
 
typedef long long ll; 
typedef pair<int, int> pii;
 
#define MOD 1000000007
#define INF 1000000000
#define pb push_back 
#define sz size() 
#define mp make_pair

#define f(i,a,b) for(i=a;i<b;i++)

int main()
{
	
	int t, times;
	long long n, ans;
	char buffer[30];
	set<int> f;
	
	cin >> t;
	
	for(int k = 0; k < t; k++)
	{
		cin >> n;
		times = n;
		
		if (n > 0)
		{
			while (f.sz < 10)
			{
				sprintf (buffer, "%Ld", n);
				for(int i = 0; i < strlen(buffer); i++)
				{
					f.insert(buffer[i]-'0');
					if (f.sz == 10)
					{
						ans = n;
						break;
					}
				}
				n += times;
			}
			cout << "Case #" << k+1 << ": " << ans << endl;
		}
		else
		{
			cout << "Case #" << k+1 << ": INSOMNIA" << endl;
		}
		f.clear();
	}
	
 	return 0;
}