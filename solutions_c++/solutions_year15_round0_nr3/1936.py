#include <iostream> 
#include <fstream> 
#include <cmath> 
#include <algorithm> 
#include <cassert> 
#include <string> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <map> 
#include <set> 
#include <stack> 
#include <iomanip> 
#include <queue> 

#define pb push_back 
#define mp make_pair 
#define ll long long 
#define abracadabra next 
#define pii pair<int, int> 

using namespace std; 
const int rules[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};

int sign(int a)
{
	if (a < 0)
		return -1;
	else
		return 1;
}

int mul(int a, int b)
{
	//cerr << a << " " << b << endl;
	return sign(a)*sign(b)*rules[abs(a)-1][abs(b)-1];
}

int main(){ 
	ios_base::sync_with_stdio(false); 
	
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{
		string ans, s;
		long long l, x;
		cin >> l >> x >> s;
		long long x0 = x;
		int t = 1;
		for(int i = 0; i < l; i++)
			t = mul(t, s[i] - 'i' + 2);
			
		int tt = 1;
		while (x0 > 0)
		{
			if (x0 & 1)
				tt = mul(tt, t);
			t = mul(t, t);
			x0 >>= 1;
		}
		ans = "NO";
		if (tt == mul(mul(2, 3), 4))
		{
		
			long long left = -1, right = -1;
			t = 1;
			for(int i = 0; i < l*4; i++)
			{
				t = mul(t, s[i%l] - 'i' + 2);
				if (t == 2)
				{
					left = i;
					break;
				}
			}
			t = 1;
			for(int i = 4*l-1; i >= 0; i--)
			{
				t = mul(s[i%l] - 'i' + 2, t);
				if (t == 4)
				{
					right = i;
					break;
				}
			}//cerr << left << " " << right << endl;
			if (left != -1 && right != -1 && left < l*(x-4) + right)
			{
				ans = "YES";
			}	
		}
		printf("Case #%d: %s\n", test, ans.c_str());
		
		
	}
	
	return 0; 
} 
