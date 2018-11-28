#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
vector<string> ans;

void fun(int length,string tmp) {
	if(length <= 0) {
		ans.push_back("1"+tmp+"1");
		return;
	}
	fun(length-1,tmp+"0");
	fun(length-1,tmp+"1");
}

int main()
{
	int t,cas=1;
	cin >> t;
	while(t--) {
		int n,j;
		ans.clear();
		cin >> n >> j;
		int i;
		for(i = n-1; i >= 3; i --) {
			if(n%i == 0) {
				fun(i-2,"");
			}
		}
		printf("Case #1:\n");
		for(int i = 0 ; i < j && i < ans.size(); i ++) {
			int len = ans[i].size();
			for(int ii = 0 ; ii < n/len; ii ++) {
				cout << ans[i];
			}
			for(int ii = 2; ii <= 10 ;ii ++) {
				long long tmp = 0;
				for(int jj = 0; jj < len ; jj ++) {
					tmp = tmp * ii + ans[i][jj] - '0';
				}
				printf(" %lld",tmp);
			}
			cout << endl;
		}

	}
	return 0;
}

