//||||||||||||||||||||||||||||
//----IN THE NAME OF GOD----||
//||||||||||||||||||||||||||||

#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back

typedef long long int lld;
typedef long double ldb;

int main(){
	int t;
	ifstream input;
	input.open("B-large.in");
	ofstream output;
	output.open("out.txt");
	input >> t;
	int j=0;
	string str;
	while(t--){
		j++;
		output << "Case #" <<j <<": ";
		input >> str;
		int len = str.length();
		char seek = '-';
		int ans = 0;
		for(int i=len-1; i>=0; i--){
			if(str[i]==seek){
				ans++;
				if(seek=='-') seek='+';
				else seek='-';
			}
		}
		output << ans << endl;
	}
	return 0;
}
