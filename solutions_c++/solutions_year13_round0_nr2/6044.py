#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int b[100][100];
int N,M;
bool solve() {
	for (int row = 0; row < N; row++)
		for (int col = 0; col < M; col++){
			bool lol = true;
			if(b[row][col] == 1){
				for (int i = 0; i < M; i++)
					if(b[row][i] == 2){
						lol = false;
						break;
					}
					if(!lol)
						for(int i = 0; i < N ; i ++)
							if(b[i][col] != 1)
								return false;
			}
		}
		return true;
}

int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for (int t = 1; t <= test; t++)
	{
		cin >> N >> M;
		for (int row = 0; row < N; row++)
			for (int col = 0; col < M; col++)
				cin >> b[row][col];
		cout << "Case #" << t <<": ";
		if(solve())
			cout << "YES" <<endl;
		else
			cout << "NO" <<endl;
	}
	return 0;
}
