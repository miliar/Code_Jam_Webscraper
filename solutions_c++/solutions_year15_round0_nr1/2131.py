#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
typedef long long Long;
typedef pair<Long,Long> PII;


int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
		
	int TC;
	cin >> TC;
	for (int tc = 1; tc <= TC; ++tc) {
		int S;
		string A;
		cin >> S >> A;
		int f = 0, c = 0;
		for(int i = 0; i < A.size(); ++i){
			if(A[i] == 0)continue;
			if(c < i){
				f += i-c;
				c = i;
			}
			c += A[i]-'0';
		}
		cout << "Case #" << tc << ": " << f << endl;	
	}
	

	

	
	
}
