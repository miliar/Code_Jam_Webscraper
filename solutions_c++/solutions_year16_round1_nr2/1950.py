#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int h[2500],ans[50];
int case_i, case_n;

int main()
{
	cin >> case_n;
	int n,p,t;
	for (case_i = 0; case_i < case_n; case_i++)
	{	
		t = 0;
		memset(ans,0,sizeof(ans));
		memset(h,0,sizeof(h));
		cin >> n;
		for (int i = 0; i< 2*n -1; i++)
			for (int j = 0; j < n; j++)
			{
				cin >> p;
				h[p]++; 
			}
		for (int i = 0; i<2500; i++)
		{
			if (h[i] % 2 != 0)
			{
				ans[t] = i;
				t++;
			}
		}
		sort(ans, ans + t);
		printf("Case #%d:",case_i+1);
		for(int i=0; i < t; i++)
			cout << ' ' << ans[i];
		cout << endl;
	}
	return 0;
}