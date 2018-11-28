#include <iostream>
#include <string>

using namespace std;

int solve(int smax, string str){
	int count = (int)(str[0]-'0');
	int ret = 0;
	for(int i = 1; i <= smax; i++){
		int num = (int)(str[i]-'0');
		if(count < i){
			ret += (i-count);
			count = i;
		}
		count += num;
	}
	return ret;
}


int main(){
	int casenum = 0;
	cin >> casenum;

	for(int  i = 0; i < casenum; i++){
		int smax = 0;
		string str = "";
		cin >> smax >> str;
		int result = solve(smax,str);
		cout << "Case #" << (i+1) << ": " << result << endl;
	}
	return 0;
}

