#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
using namespace std;
int main(){
	int t, smx;
	string s;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;

	for (int i = 1; i <= t; i++){
		cin >> smx >> s;
		int sum[1005] = {0};
		int total = 0;
		sum[0] = s[0] - 48;
		for (int j = 1; j < s.length(); j++)
			sum[j] += s[j] - 48 + sum[j-1];
		
		for (int j = 1; j <= smx; j++){
			if (s.length()>1){
				if (sum[j-1] < j && s[j]!='0'){
					int dis= j - sum[j-1];
					total += dis;
					int tmp = j;
					while (tmp<smx)
					{
						sum[tmp++] += dis;
					}
				//	cout << total << " " << sum[j - 1] << " " << j<< endl;
				}
			}
		}
		cout << "Case #"<<i<<": " << total << endl;
	}
	return 0;
}