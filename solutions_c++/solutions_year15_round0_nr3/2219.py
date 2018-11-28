#include <iostream>
#include <vector>
#include <cstring>
#include <sstream>
#include <cctype>
#define ll long long
#define MAX 10005

using namespace std;

char mult[MAX], table[4][4] = {{'o','i','j','k'}, {'i','O','k','J'}, {'j','K','O','i'}, {'k','j','I','O'}};

ll cnt = 0;


string operator*(const string& s, unsigned int n) {
    stringstream out;
    while (n--)
        out << s;
    return out.str();
}

string operator*(unsigned int n, const string& s) { return s * n; }

void tablize(string s);
string partition(string s);
char range_mult(int i, int j);

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		memset(mult,0,MAX);
		ll L, X;
		cin >> L >> X;
		string s;
		cin >> s;
		s = (s * X);
		tablize(s);
		cout << "Case #" << t << ": " << partition(s) << endl;
		//cout << "Count = " << cnt << endl;
	}
	return 0;
}

void tablize(string s)
{
	char result = s[0];
	int r;
	mult[0] = s[0];
//	cout << "Multiplication Tab for " << s << ": " << endl << s[0] << " " ;
	for(int i = 1; i < s.size(); ++i){
		int mul = 1;
		char tmp;
		if(isupper(result)){
			mul *= -1;
			result = tolower(result);
		}
		if(result == 'o')
			r = 0;
		else if(result == 'i')
			r = 1;
		else if(result == 'j')
			r = 2;
		else
			r = 3;
		if(s[i] == 'i')
			tmp = table[r][1];
		else if(s[i] == 'j')
			tmp = table[r][2];
		else
			tmp = table[r][3];
		//cout << "tmp = " << tmp << endl;
		if(mul == -1){
			if(isupper(tmp)){
				result = tolower(tmp);
				//cout << "result = " << result << endl;
			}
			else
				result = toupper(tmp);
		}
		else
			result = tmp;
		mult[i] = result;
	//	cout << result << " ";
	}
//	cout << endl;
}

string partition(string s)
{
	int final_i = s.size() - 2, final_j = s.size() - 1;
	for(int i = 0; i < final_i; ++i){
		for(ll j = i+1; j < final_j; ++j){
			char m1, m2, m3;
			m1 = range_mult(0,i);
			if(m1 != 'i')
				continue;
			m2 = range_mult(i+1,j);
			if(m2 != 'j')
				continue;
			m3 = range_mult(j+1, final_j);
			if(m3 != 'k')
				continue;
			//cout << "i = " << i << " j = " << j << " k = " << j+1 << " m1=" << m1 << " m2=" << m2 << " m3=" << m3 << endl;
			//if(m1 == 'i' && m2 == 'j' && m3 == 'k')
				return "YES";
		}
	}
	return "NO";
}

char range_mult(int i, int j)
{
	//cout << "calculating for range " << i << " " << j << endl;
	char r = mult[j], q , d;
	int c,a, rem=1;
	if(i == 0)
		q = 'o';
	else
		q = mult[i-1];
	if(isupper(q))
		rem *= -1;
	if(tolower(q) == 'o')
		a = 0;
	else if(tolower(q) == 'i')
		a = 1;
	else if(tolower(q) == 'j')
		a = 2;
	else
		a = 3;
	for(int z = 0; z < 4; ++z){
		//++cnt;
		char tab_result = table[a][z];
		if(rem == -1){
			if(isupper(tab_result))
				tab_result = tolower(tab_result);
			else
				tab_result = toupper(tab_result);
		}
		if(tab_result == r){
			if(z == 0)
				return 'o';
			else if(z == 1)
				return 'i';
			else if(z == 2)
				return 'j';
			else
				return 'k';
		}
	}
//	cout << "ERROR for r = " << r << " q = " << q << ", a = " << a << " , rem = " << rem << endl;
	return 'z';
}
