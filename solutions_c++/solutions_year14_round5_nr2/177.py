/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream> 
#include <fstream> 
#include <sstream> 
#include <cstdio> 
#include <cstring> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 
#include <algorithm> 
#include <vector> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <set> 
#include <map> 
#include <complex> 
#include <bitset> 
#include <iomanip> 
#include <utility> 

using namespace std;

int P,Q,N;
int dp[200][2000][210];
int H[200],G[200];

inline int go (int pos, int tot, int health){
	if (health <= 0){
		health = H[pos+1];
		pos++;
	}
	if (pos == N)
		return 0;
	int &ret = dp[pos][tot][health];
	if (ret != -1)
		return ret;
	ret = 0;
	if (tot > 0)
		ret = max(ret, go(pos, tot-1, health - P) + G[pos] * (health-P <= 0));
	ret = max(ret, go(pos, tot+1, health - Q));
	return ret;
}

void main2(){
	cin >> P >> Q >> N;
	for (int i=0; i<N; i++)
		cin >> H[i] >> G[i];
	memset(dp, -1, sizeof dp);
	cout << go(0,1,H[0]) << endl;
}

int main(){
	int testCase; cin >> testCase;
	for (int o=1; o<=testCase; o++){
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
