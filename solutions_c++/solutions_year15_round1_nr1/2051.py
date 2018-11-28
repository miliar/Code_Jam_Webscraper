#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <fstream>   
using namespace std;


int main(void)
{
	freopen("d:\\output.txt", "w", stdout);
	freopen("d:\\input.txt", "r", stdin);

	int T;
	cin >> T;
	
	int N;
	for (int c = 0; c < T; c++)
	{
		cin >> N;
		vector<int> v(N);

		for (int i = 0; i < N; i++)
			cin >> v[i];
		
		int A = 0;
		
		for (int i = 0; i < N - 1; i++)
		{
			if (v[i] <= v[i + 1])continue;
			else
			{
				A += v[i] - v[i+1];
			}
		}

		int B = 0;

		int M = 0;
		for (int i = 0; i < N - 1; i++)
		{
			M = max(M, v[i] - v[i + 1]);
		}

		for (int i = 0; i < N - 1; i++)
		{
			if (v[i] < M)
				B += v[i];
			else
				B += M;
		}

		cout << "Case #"<<c+1<<": " << A <<" "<<B<<endl;
	}
}