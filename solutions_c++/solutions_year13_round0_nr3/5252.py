#include <vector>
#include <iostream>
using namespace std;
vector<int> v;
int isPol(int a)
{
	int t = a;
	int r = 0;
	while (a)
	{
		r *= 10;
		r += a % 10;
		a /= 10;
	}
	return t == r;
}
int main()
{
	freopen ("C-small-attempt0.in","r",stdin);
	freopen ("output2.txt","w",stdout);
	for (int i = 1; i * i <= 1000; i++)
	{
		if (isPol(i) && isPol(i * i))
		{
			v.push_back (i * i);
		}
	}
	int n;
	cin >> n;
	int a,b;
	for (int i = 0; i < n; i++)
	{	
		cin >> a >> b;
		int cnt = 0;
		for (int j = 0; j < v.size(); j++)
		{
			if (v[j] >= a && v[j] <= b)
				cnt++;
		}
		printf ("Case #%d: %d\n",i + 1,cnt);
	}
	return 0;
}