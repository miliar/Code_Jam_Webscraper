#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int t,smax;
	cin >> t;
	int a = 1;
	while(t --){
		cin >> smax;
		char v[smax + 2]; 
		scanf("%s",v);
		int ans = 0;
		int tt = v[0] - '0';
		for(int i = 1;v[i] != '\0';i ++){
			while(tt < i){
				ans ++;
				tt++;
			}
			tt += (v[i] - '0');
			
		}
		cout << "Case #"<< a++ <<": " << ans << endl;
	}
}
