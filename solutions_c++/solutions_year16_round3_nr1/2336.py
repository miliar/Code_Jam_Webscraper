
#include <iostream>
#include<string>
using namespace std;


int main()
{
	int t;
	cin >> t;
	for (int X = 0; X < t; X++)
	{
		int n,sum=0;
		cin >> n;
		int *a=new int[n];
		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
			sum += a[i];
		}
		cout << "Case #" << X + 1 << ":";
		while (sum > 0) {
			string out = "";
			int mx = 0,mxi=-1;
			for (int i = 0; i < n; i++)
			{
				if (a[i] > mx) {
					mx = a[i];
					mxi = i;
				}
			}
			out = out + (char)('A' + mxi);
			sum--;
			a[mxi]--;
			if (sum > 0) {
				int mx = 0, mxi = -1;
				for (int i = 0; i < n; i++)
				{
					if (a[i] > mx) {
						mx = a[i];
						mxi = i;
					}
				}
				bool flg=false;

				sum--;
				a[mxi]--;
				for (int i = 0; i < n; i++)
				{
					if (a[i] > sum / 2.0) {
						flg = true;
						break;
					}
				}
				if (flg) {
					sum++;
					a[mxi]++;
				}
				else {
					out = out + (char)('A' + mxi);
				}
			}
			cout <<" "<<out;
		}
		cout << endl;
	}
    return 0;
}


