#include <iostream>
#include <string>
using namespace std;
int main(){
	string str;
	bool finish;
	int count;
	int T;
	int l;
	cin >> T;
	for(int t = 1;t <= T;t ++){
		cin >> str;
		l = str.length();
		finish = false;
		count = 0;
		while(!finish){
			finish = true;
			for(int i = 0;i < l;i ++){
				if(str[i] == '-'){
					finish = false;
					break;
				}
			}
			if(finish) break;
			int k = l + 1;
			for(int i = 0;i < l;i ++){
				if(str[0] != str[i]){
					k = i;
					break;
				}
			}
			for(int i = 0;i < k;i ++){
				if(str[i] == '+') str[i] = '-';
				else str[i] = '+';
			}
			count ++;
		}
		cout << "Case #" << t << ": "  << count << endl;
	}
	
	return 0;
}
