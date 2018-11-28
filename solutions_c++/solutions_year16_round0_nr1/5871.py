#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <map>
using namespace std;
typedef unsigned long long ULL;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	freopen("A-large.out", "w", stdout);
	int T;
	std::map<int,int> numCount;
	cin >> T;

	for(int i = 1; i <= T; ++i){
		int N;
		cin >> N;
		if(N == 0){
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}else{
			bool end = false;
			ULL result,temp,n = 1;
			do{
				result = N * n;
				temp = result;
				while(temp){
					int d = temp % 10;
					temp /= 10;
					numCount[d] = 0;
					if(numCount.size() == 10){
						end = true;
					}
				}
				n++;
			}while(!end);
			cout << "Case #" << i << ": " << result <<endl;
			numCount.clear();
		}
	}
	fclose (stdout);
	return 0;
}
