
#include <iostream>
#include <cstring>
using namespace std;

int vowel[300]={0};
char str[1000005];
int  prev = -1;
int  len;
int  k;

inline int isVowel(char c){
	return vowel[c];
}


int cal(int cur){
	if((cur+k) > len)
		return 0;

	char *p = str + cur;
	int ok = true;
	for(int i=0;i<k;i++, p++)
		if(vowel[*p] == 1){
			ok = false;
			break;
		}

//	cout << endl << "cur " << cur << ' ' << len << ' ' << ok ;

	if(ok){
		int a = cur - prev + 1;
		int b = (len+1) - (cur+k);
		prev = cur+1;
		int r = cal(cur+1);
//		cout << cur << '=' << a << ' ' << b << ' ' << r << endl;
		return a*b + r;
	}else{
		int r = cal(cur+1);
//		cout << cur << '=' << r << endl;
		return r;
	}
}

int solve(){
	cin >> str;
	cin >> k;
	len = strlen(str);
	prev=0;
	cout << cal(0);
}

int main() {
	int tc,z;
	vowel['a'] = vowel['e'] = vowel['i'] = vowel['o'] = vowel['u'] = 1;
	cin >> tc;
	z = tc;
	while(tc--){
		cout << "Case #"<< (z-tc) << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
