#include<string>
#include<iostream>

using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	string s;
	int ntc,n,c,res;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		res = 0;
		cin >> n >> s;
		c = 0;
		for (int i=0;i<s.length();i++){
			n = s[i]-'0';
			if (n && i>c+res) res += i-(c+res);
			c += n;
		}

		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}