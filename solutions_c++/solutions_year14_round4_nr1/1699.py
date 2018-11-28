#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <direct.h>
#include <assert.h>
#include <time.h>

#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <set>
#include <bitset>
#include <exception>
#include <memory>
#include <numeric>
#include <limits>
#include <functional>
#include <stack>
#include <iterator>
#include <random>
#include <unordered_map>
#include <unordered_set>

#include <cctype>
#include <cstddef>
#include <cstring>
#include <ctime>

#define NOMINMAX
#include <windows.h>

#define	SAFE_DELETE(ptr) if(ptr){delete ptr; ptr=NULL;}
#define	SAFE_DELETE_ARRAY(ptr) if(ptr){delete [] ptr; ptr=NULL;}

using namespace std;

int run(vector<int>& S, int X)
{
	std::sort(S.begin(), S.end(), std::greater<int>());

	vector<int> R(S.size());
	vector<int> num(S.size(), 0);
	vector<bool> Put(S.size(), false);

	int idx = 0;
	for (int i=0; i<S.size(); i++)
	{
		if (Put[i] == true)
			continue;

		R[idx] = S[i];
		Put[i] = true;
		num[idx]++;
		for (int j=i+1; j<S.size(); j++)
		{
			if (Put[j] == true)
				continue;
			if (S[j] + R[idx] <= X)
			{
				R[idx] += S[j];
				Put[j] = true;
				num[idx]++;
				break;
			}
		}
		idx++;
	}

	return idx;
}

int main()
{
	freopen("datain.txt","r",stdin);
	freopen("dataout.txt","w",stdout);

	int T; cin >> T;

	for (int i = 1; i <= T; ++i)
	{
		int N, X;
		cin >> N >> X;
		vector<int> S(N);

		for (int j=0; j<N; j++)
			cin >> S[j];

		int rst = run(S, X);
		
		cout << "Case #" << i << ": " << rst << endl;
	}
	
	fclose(stdout);
	fclose(stdin);
	return 1;
}
