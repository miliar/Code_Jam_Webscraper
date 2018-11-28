
#include<iostream>
#include<iomanip>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
using namespace std;


int main()
{
	errno_t err1;
	errno_t err2;
	FILE *fin, *fout;
	err1 = freopen_s(&fin, "in.txt", "r", stdin);
	err2 = freopen_s(&fout, "out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int z = 1; z <= T; ++z)
	{
		cout << "Case #" << z << ": ";
		int n;
		cin >> n;
		double a[1001], b[1001];
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		for (int i = 0; i < n; ++i)
			cin >> b[i];
		sort(a, a + n);
		sort(b, b + n);
		int count = 0;
		int pt = 0;
		for (int i = 0; i < n; ++i)
		{
			if (a[i]>b[count])
				count++;
		}
		cout <<count << " ";
		for (int i = 0; i < n; ++i)
		{
			if (b[i]>a[pt])
			{
				pt++;
			}
		}
		cout <<n- pt << endl;
		
	}

}
