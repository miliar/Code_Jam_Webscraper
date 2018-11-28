#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <iostream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <iomanip>

#define rep(i,m) for(unsigned long long i = 0;i < (unsigned long long)m ;i++)
#define rep2(i,n,m) for(unsigned long long i = (unsigned long long)n;i < (unsigned long long)m ;i++)
#define ui unsigned int
#define ull  unsigned long long
#define pb  push_back

using namespace std;

int dat[100][100];
int mcol[100];
int mrow[100];

int main() {
	int cases, N, M;
	bool flag; 
	cin >> cases;
	rep(casei, cases){
		cin >> N >> M;
		rep(i, N)
			rep(j, M)
				cin >> dat[i][j];
		if(N == 1 || M == 1){
			cout << "Case #"<< (int)casei + 1 <<": YES"<< endl;
			continue;
		}
		
		rep(i, N){
			mrow[i] = -1;
			rep(j,M)
				mrow[i] = max(mrow[i], dat[i][j]);
		}
		
		rep(i, M){
			mcol[i] = -1;
			rep(j,N)
				mcol[i] = max(mcol[i], dat[j][i]);
		}
		
		flag = true;
		
		rep(i, N){
			rep(j, M)
				if(dat[i][j] != mrow[i] && dat[i][j] < mcol[j]){
					flag = false;
					break;
				}
			if(!flag)
				break;
		}
		if(!flag){
			cout << "Case #"<< (int)casei + 1 <<": NO"<< endl;
			continue;
		}
		
		rep(i, M){
			rep(j, N)
				if(dat[j][i] != mcol[i] && dat[j][i] < mrow[j]){
					flag = false;
					break;
				}
			if(!flag)
				break;
		}
		if(!flag){
			cout << "Case #"<< (int)casei + 1 <<": NO"<< endl;
			continue;
		}
		cout << "Case #"<< (int)casei + 1 <<": YES"<< endl;
    }
    return 0;
}