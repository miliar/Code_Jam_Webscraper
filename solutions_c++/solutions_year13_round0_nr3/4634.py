#include<iostream>
#include<string>
#include<vector>
#include<math.h>
#include<sstream>
using namespace std;
int x, y;
long long arr[1000000];

bool chechPal(string s)
{
	int d = s.size();
	for(int i = 0; i < d/2; i++)
		if(s[i] != s[d-i-1])
			return false;
	return true;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	stringstream ss;
	string str;
	int j = 0;
	arr[0] = 1;
	arr[1] = 4;
	arr[2] = 9;
	arr[3] = 121;
	arr[4] = 484;
	arr[5] = 10201;
	arr[6] = 12321;
	arr[7] = 14641;
	arr[8] = 40804;
	arr[9] = 44944;
	arr[10] = 1002001;
	arr[11] = 1234321;
	arr[12] = 4008004;
	arr[13] = 100020001;
	arr[14] = 102030201;
	arr[15] = 104060401;
	arr[16] = 121242121;
	arr[17] = 123454321;
	arr[18] = 125686521;
	arr[19] = 400080004;
	arr[20] = 404090404;
	arr[21] = 10000200001;
	arr[22] = 10221412201;
	arr[23] = 12102420121;
	arr[24] = 12345654321;
	arr[25] = 40000800004;

	/*for(long long i = 1; i <= 10000001; i++)
	{
		ss << i;
		ss >> str;
		ss.clear();
		if(chechPal(str) == true)
		{
			ss << (i*i);
			ss >> str;
			if(chechPal(str) == true)
			{			
				arr[j++] = i*i;
				cout << "arr[" << j-1 << "] = " << i*i << endl; 
			}

			ss.clear();
		}
	}*/
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> x >> y;
		int res = 0;
		for(int j = 0; j <= 25; j++)
		{
			if(arr[j] >= x && arr[j] <= y)
				res++;
		}
		cout << "Case #" << i+1 << ": " << res << endl;

	}
}
