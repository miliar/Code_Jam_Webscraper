#include <bits/stdc++.h>
using namespace std;


int main() {

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	long long t;
	cin >> t;
	for (int tc = 0; tc < t; ++tc) {
		string str ;
		cin >> str ;
		while(true){
			if(str.size()==0) break;
			if(str[str.size()-1]=='+')
				str.erase(str.size()-1);
			else
				break;
		}
//		cout << str;
		int ans = 1;
		for (int i = 0; i < str.size(); ++i) {

			if(i==0){

//				if(str[i]=='-')
//					ans++;
				continue;
			}
			if(str[i-1]==str[i])
					continue;
			ans++;
//			cout << i << " ";
		}


		cout << "Case #" << tc+1 <<": " << (str.size()==0?0:ans) << endl;

	}
	return 0;
}
