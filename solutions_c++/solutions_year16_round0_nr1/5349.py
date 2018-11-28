#include <iostream>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <string>

using namespace std;
typedef long long LL;

int main(){
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		int n;
		cin >> n;
		set<int> digits;
		if(n == n*2){
			cout << "Case #" << t << ": ";
			cout << "INSOMNIA" << endl;
		}
		else{
			int num = n;
			while(digits.size() < 10){
				int t = num;
				while(t > 0){
					digits.insert(t%10);
					t /= 10;
				}
				num += n;
			}
			cout << "Case #" << t << ": ";
			cout << num - n << endl;
		}
	}
	return 0;
}