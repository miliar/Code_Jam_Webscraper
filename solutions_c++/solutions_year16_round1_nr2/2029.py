#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
using namespace std;

typedef long long ll;



int main()
{
	ll T = 0;
	cin >> T;
	for (int _t = 1; _t <= T; ++_t){
		int N;
		cin >> N;
		vector<vector<int> > in;
		in.resize(N - 1);
		vector<int> count(2600);
		for (int i = 0; i < 2*N - 1; ++i){
			for (int j = 0; j < N; ++j){
				int tmp;
				cin >> tmp;
				count[tmp]++;
			}
		}
		vector<int> result;
		cout << "Case #" << _t << ": ";
		for (int i = 0; i < 2600; ++i){
			if (count[i] % 2)cout << i << " ";
		}
		cout<<endl;


#if 0
		int top = findK(in, mini);
		result[0] = in[top];
		used[top] = true;
		int left = findK(in, mini);
		if(left==-1){
			//ans is 12345
		}
		else{
			used[left] = true;
			for (int i = 0; i < N; ++i){
				result[i][0]=in[i][0];
			}

			for(int i=1;i<N-1;++i){
			}
		}
		for (int i = 0; i < N; ++i){
			int col = findK(in, result[0][i]);
			if (col == -1)continue;
			for (int j = 0; j < N; ++j){
				result[j][i] = in[col][j];
			}
			used[col] = true;
		}
#endif
		//cerr << "Case #" << _t << ": " << result << endl;
		
	}
}