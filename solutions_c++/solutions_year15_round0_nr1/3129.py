#include<iostream>
#include<vector>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int t = 1 ; t <= T ; t ++){
		string s;
		int s_max ;
		cin >> s_max;
		cin >> s;
		vector<int> V(s_max + 1);;
		for(int i =  0 ; i < s.length() ; i++){
			V[i] = s[i] - '0';
		}
		long long sum = V[0];
		long long ans = 0;
		for(int i = 1 ; i < s.length() ; i ++){
			long dif = 0;
			if(i > sum){
				dif = i - sum;
				ans += dif;
			}
			sum += V[i] + dif;
		}
		cout << "Case #"<<t<<": "<<ans<<endl;
	
	}
	return 0;
}
