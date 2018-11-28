//#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main(){
	//ios::sync_with_stdio(0);
	//cin.tie(0);
	ifstream cin("A-large.in.txt");
	ofstream cout("output.txt");
	int t, maxs, s, sum, ans;
	string str;
	cin >> t;
	for(int i=1;i<=t;i++){
		cin >> maxs;
		sum = 0;
		ans = 0;
		cin >> str;
		for(int i=0;i<=maxs;i++){
			s = str[i]-'0';
			if(!s||i<=sum)sum+=s;
			else {
				ans+=(i-sum);
				sum=i+s;
			}
		}
		cout << "Case #" << i << ": " << ans << "\n";
	}
}