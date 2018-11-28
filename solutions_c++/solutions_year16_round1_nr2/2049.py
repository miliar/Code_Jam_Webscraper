#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
using namespace std;

ifstream in;
ofstream out;
int test;
int g[51][51];
bool check[51];
vector<vector<int> > a;
int mn, temp;
int n;
int cnt[2505];

//bool HasRow(int i);
//bool HasCol(int j);

int main()
{
	in.open("B-large.in");
	out.open("output.txt");

	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		mn = 99999999;
		for (int i = 0; i < 51; ++i)
			check[i] = false;
		a.clear();

		for (int i = 0; i <= 2500; ++i)
			cnt[i] = 0;


		in >> n;
		//cout << n << endl;
		for (int i = 0; i < 2*n - 1; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				in >> temp;
				//cout << temp << " ";
				cnt[temp]++;
			}
			//cout << endl;
		}

		vector<int> result;
		for (int i = 1; i <= 2500; ++i)
		{
			if (cnt[i] <= 0)
				continue;

			if (cnt[i] % 2 == 1)
				result.push_back(i);
		}

		sort(result.begin(), result.end());

		out << "Case #" << t << ": ";
		for (int i =0 ; i< result.size(); ++i)
			out << result[i] << " ";
		out << endl;
	}
		in.close();
	out.close();
	return 0;
}

//		// input
//		in >> n;
//		for (int i = 0; i < 2*n + 1; ++i)
//		{
//			vector<int> t;
//			for (int j = 0; j < n; ++j)
//			{
//				in >> temp;
//				t.push_back(temp);
//			}
//			a.push_back(t);
//			if (t[0] < mn)
//				mn = t[0];
//		}
//
//		// find first row
//		for (int i = 0; i < 2*n + 1; ++i)
//		{
//			if (a[i][0] == mn)
//			{
//				for (int j = 0 ;j < n; ++j)
//				{
//					g[0][j] = a[i][j];
//					g[j][0] = a[i][j];
//				}
//				break;
//			}
//		}
//
//
//		for (int k = 1; k < n; ++k)
//		{
//			int start = g[0][k];
//			for (int i = 0; i < 2*n + 1; ++i)
//			{
//				if (a[i][0] == start)
//				{
//					for (int j = 0 ;j < n; ++j)
//					{
//						g[k][j] = a[i][j];
//						g[j][k] = a[i][j];
//					}
//				}
//			}
//		}
//
//		for (int i = 0; i < n; ++i) {
//			for (int j = 0; j < n; ++j)
//				cout << g[i][j] << " ";
//			cout << endl;
//		}
//
//		out << "Case #" << t << ": ";
//
//		bool ans = false;
//
//		for (int i = 0; i < n; ++i)
//		{
//			if (!HasRow(i))
//			{
//				for (int j = 0; j < n; ++j)
//					out << g[i][j] << " ";
//				out << endl;
//				ans = true;
//				break;
//			}
//		}
//
//		if (ans)
//			continue;
//
//		for (int j = 0; j < n; ++j)
//		{
//			if (!HasCol(j))
//			{
//				for (int i = 0; i < n; ++i)
//					out << g[i][j] << " ";
//				out << endl;
//				ans = true;
//				break;
//			}
//		}
//	}
//
//	in.close();
//	out.close();
//	return 0;
//}
//
//bool HasRow(int i)
//{
//	bool f;
//	for (int k = 0; k < 2*n + 1; ++k)
//	{
//		f = true;
//		for (int j = 0; j < n; ++j)
//		{
//			if (g[i][j] != a[k][j])
//			{
//				f = false;
//				break;
//			}
//		}
//		if (f)
//			return true;
//	}
//	return false;
//}
//
//bool HasCol(int j)
//{
//	bool f;
//	for (int k = 0; k < 2*n + 1; ++k)
//	{
//		f = true;
//		for (int i = 0; i < n; ++i)
//		{
//			if (g[i][j] != a[k][j])
//			{
//				f = false;
//				break;
//			}
//		}
//		if (f)
//			return true;
//	}
//	return false;
//}