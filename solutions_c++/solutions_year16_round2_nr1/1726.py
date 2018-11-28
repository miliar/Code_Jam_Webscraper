

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
//#include <forward_list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin

#define cout fout

//----------------------------


#ifdef cin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif


int a[30];
int b[30];

string zero = "ero";
string two = "to";
string six = "si";
string seven = "even";
string five = "fie";
string four = "our";
string eight  = "eiht";
string nine = "nne";
string one = "ne";
int main(){

	int t, z = 1;
	cin>>t;

	while(t--){
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		string s;
		cin>>s;
		for(int i = 0; i < s.size(); i++) a[s[i] - 'A']++;

		b[0] += a['z' - 'a'];
		a['e' - 'a'] -= b[0];
		a['r' - 'a'] -= b[0];
		a['o' - 'a'] -= b[0];

		b[2] += a['w' - 'a'];
		for(int i =0; i < two.size(); i++) a[two[i] - 'a'] -= b[2];

		b[6] += a['x' - 'a'];
		for(int i = 0; i < six.size(); i++) a[six[i] - 'a'] -= b[6];

		b[7] += a['s' - 'a'];
		for(int i = 0; i < seven.size(); i++) a[seven[i] - 'a'] -= b[7];

		b[5] += a['v' - 'a'];
		for(int i=  0; i < five.size(); i++) a[five[i] - 'a'] -= b[5];

		b[4] += a['f' - 'a'];
		for(int i = 0; i < four.size(); i++) a[four[i] - 'a'] -= b[4];

		b[8] += a['g' - 'a'];
		for (int i = 0; i < eight.size(); i++) a[eight[i] - 'a'] -= b[8];

		b[9] += a['i' - 'a'];
		for(int i = 0; i < nine.size(); i++) a[nine[i] - 'a'] -= b[9];

		b[1] += a['o' - 'a'];
		for(int i=  0; i < one.size(); i++) a[one[i] - 'a'] -= b[1];

		b[3] += a['t' - 'a'];


		string ans;
		for(int i = 0; i <= 9; i++){
			for(int j = 0; j < b[i]; j++) ans.push_back('0' + i);
		}
		cout<<"Case #"<<z++<<": "<<ans<<endl;
	}


#undef cin
	int ________________;
	cin >>________________;
	return 0;
}