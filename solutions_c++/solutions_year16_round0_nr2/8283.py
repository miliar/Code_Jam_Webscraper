#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
int main(){
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc){
		string s;
		cin>>s;
		int len = s.size();
		string temp = s;
		printf("Case #%d: ", tc);
		int cnt = 0;
		while(1){
			bool udah = true;
			for(int i = 0; i < len && udah; ++i){
				if(temp[i] == '-') udah = false;
			}
			if(udah) break;
			cnt++;
			if(temp[0] == '-'){
				int lastminus = 0;
				for(int i = 0; i < len; ++i) if(temp[i] == '-') lastminus = i;
				reverse(temp.begin(), temp.begin() + lastminus + 1);
				for(int i = 0; i <= lastminus; ++i) {
					if(temp[i] == '-') temp[i] = '+';
					else temp[i] = '-';
				}
			}
			else {
				int lastplusbeforeminus = 0;
				int lastplus = 0;
				for(int i = 0;i < len; ++i){
					if(temp[i] == '+') lastplus = i;
					else lastplusbeforeminus = lastplus;
				}
				reverse(temp.begin(), temp.begin() + lastplusbeforeminus + 1);
				for(int i = 0; i <= lastplusbeforeminus; ++i) {
					if(temp[i] == '-') temp[i] = '+';
					else temp[i] = '-';
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}