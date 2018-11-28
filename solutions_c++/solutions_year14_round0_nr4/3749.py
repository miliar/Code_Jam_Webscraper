#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
#define MAX(x,y) (x > y ? x : y)
#define MIN(x,y) (x > y ? y : x)
double a[1010];
double b[1010];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int idx = 1; idx <= T; idx++) {
		int n;
		cin >> n;
		for (int i = 0; i < n; i ++) cin>>a[i];
		for (int i = 0; i < n; i ++) cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		cout << "Case #"<< idx<< ": ";
		int l = 0, r = n-1, count = 0;
		for (int i = 0; i < n; i ++)
		{
			if ( a[i] > b[l])
			{
				count ++;
				l++;
			} else r--;
		}
		cout << count << " ";

		l = 0, r = 0, count = 0;
		for (int i = 0; i < n; i ++)
		{
			while(l < n && b[l] < a[i])l++;
			if(l>=n)count++;
			l++;
		}
		cout << count << endl;
	}
	return 0;
}