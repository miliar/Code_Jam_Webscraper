#include<iostream>
#include<cstring>
using namespace std;
const int mxn = 1001;
int check(int);
int all[mxn];
int D;
inline int min(int a,int b)
{
	return a < b ? a : b;
}
int main()
{
	int Tcase;
	cin >> Tcase;
	for(int casenow = 1;casenow <= Tcase;casenow ++)
	{
		cin >> D;
		for(int i=0;i<D;i++)
			cin >> all[i];
		int ans = 1001;
		for(int ansa=1;ansa < 1001;ansa++)
		{
			ans = min(ans,check(ansa));
		}
		cout << "Case #" << casenow << ": " << ans << endl;
	}
	return 0;
}
int check(int now)
{
	int nowans = 0;
	for(int i=D-1;i>=0;i--)
	{
		if(all[i] % now == 0)
			nowans += all[i] / now - 1;
		else 
			nowans += all[i] / now;
	}
	return nowans + now;
}
