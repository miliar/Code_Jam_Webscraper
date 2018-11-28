#include<iostream>
#include<set>
#include<algorithm>
#include<map>
using namespace std;
double a[1005] , b[1005];
int n;
int calc(set<double> S1 , set<double> S2)
{
	int ans = 0;
	for(set<double>::iterator it = S1.begin();it != S1.end();it ++)
	{
		set<double>::iterator it2 = S2.lower_bound(*it);
		if(it2 == S2.end())
		{
			ans ++;
			S2.erase(S2.begin());
		}
		else
			S2.erase(it2);
	}
	return ans;
}
int calc2(set<double> &S1, set<double> &S2)
{
	int t = 0;
//	int ans = calc(S1 , S2);
	set<double>::iterator it2 = S2.begin();
	for(set<double>::iterator it = S1.begin();it != S1.end();it ++)
	{
	//	cout << "SALAM" << endl;
		if(*it > *it2)
			t ++;
		it2 ++;
	}
//	return max(t , ans);
return t;
}
int main()
{
	int T;
	cin >> T;
	for(int t = 1;t <= T;t ++)
	{
		cin >> n;
		set<double> S1 , S2;
		for(int i = 0;i < n;i ++)
			cin >> a[i], S1.insert(a[i]);
		for(int i = 0;i < n;i ++)
			cin >> b[i] ,S2.insert(b[i]);

		sort(a , a + n);
		sort(b , b + n);
//		for(int i = 0;i < n;i ++)
//			cout << a[i] << " ";
//		cout << endl;
//		for(int i = 0;i < n;i ++)
//			cout << b[i] << " ";
//		cout << endl;
		int ans2 = calc(S1 , S2);
		int ans = calc2(S1 , S2);
	//	int ans3 = BT();
//		cout << "SALAM" << endl;
		for(int i = 0;i < n;i ++)
		{
			S1.erase(S1.begin());
			set<double>::iterator it2 = S2.end();
			it2 --;
			S2.erase(it2);
			ans = max(ans, calc2(S1 , S2));
		}
		cout << "Case #" << t << ": " << ans << " " << ans2 << endl;
	}
	return 0;
}
