#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
int main() {
	int t, j;
	long long n, x;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> n;
		unordered_map<int, bool>dic;
		int visited[10] = {0};
		int count = 0;
		for(j = 1; ; j++) {
			x = n * j;
			//cout << x << endl;
			if(dic.find(x) != dic.end())
				break;
			dic[x] = true;
			long long tmp, num = x;
			while(num != 0) {
				tmp = num % 10;
				num = num / 10;
				if(visited[tmp] == 0) {
					visited[tmp]++;
					count++;
				}
			}
			if(count == 10)
				break;
		}
		if(count == 10) {
			cout << "Case #" << i << ": " << x << endl;
		} else {
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
	}
	return 0;
}
