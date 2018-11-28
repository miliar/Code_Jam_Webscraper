#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int num[256];

inline void dec(string s,int k){
	for (int i=0;i<s.length();i++) num[s[i]] -= k;
	return;
}

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	string s;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
	
		memset(num,0,sizeof(num));

		cin >> s;
		for (int i=0;i<s.length();i++) num[s[i]]++;

		string res;

		int k = num['Z'];
		for (int i=0;i<k;i++){
			res.push_back('0');
		}
		dec("ZERO",k);
		
		k = num['W'];
		for (int i=0;i<k;i++){
			res.push_back('2');
		}
		dec("TWO",k);

		k = num['G'];
		for (int i=0;i<k;i++){
			res.push_back('8');
		}
		dec("EIGHT",k);

		k = num['X'];
		for (int i=0;i<k;i++){
			res.push_back('6');
		}
		dec("SIX",k);

		k = num['S'];
		for (int i=0;i<k;i++){
			res.push_back('7');
		}
		dec("SEVEN",k);

		k = num['T'];
		for (int i=0;i<k;i++){
			res.push_back('3');
		}
		dec("THREE",k);

		k = num['U'];
		for (int i=0;i<k;i++){
			res.push_back('4');
		}
		dec("FOUR",k);

		k = num['V'];
		for (int i=0;i<k;i++){
			res.push_back('5');
		}
		dec("FIVE",k);

		k = num['O'];
		for (int i=0;i<k;i++){
			res.push_back('1');
		}
		dec("ONE",k);

		k = num['I'];
		for (int i=0;i<k;i++){
			res.push_back('9');
		}
		dec("NINE",k);

		sort(res.begin(),res.end());

		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}