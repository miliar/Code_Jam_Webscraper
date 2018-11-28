#include <bits/stdc++.h>
using namespace std;
#define int long long 
#define vi vector<int>
#undef int
int main(){
	#define int long long
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int cases,i,j,k,n;
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> cases >> std::ws;
	for (i = 0; i < cases; i++){
		string line, answer = " ";
		cin >> line;
		answer[0] = line[0];
		char leftMost = line[0], rightMost = line[0];
		for (j = 1; j < line.size(); j++){
			if (line[j] >= leftMost){
				answer = line[j] + answer;
				leftMost = line[j];
			}else{
				answer = answer + line[j];
				rightMost = line[j];
			}
		}
		cout << "Case #" << (i+1) << ": " << answer << "\n";
	}
	return 0;
}