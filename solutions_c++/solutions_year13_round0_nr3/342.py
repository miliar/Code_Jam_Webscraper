#include <iostream>
#include <string>
#include <memory.h>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;

string A,B;
vector <string> gen;

bool is_palindrome(long long x) {
	long long temp = x;
	long long res = 0;
	while (temp > 0){
		res = res*10 + temp%10;
		temp/=10;
	}
	return (res == x);
}

void get_palindrom(string s,int k) {
	string s1 = "";
	for (int i = 0; i < s.length(); i++)
		s1 = s[i] + s1;
	gen.push_back(s+s1);
	string temp = s;
	gen.push_back(s+'0'+s1);
	if (k <= 4) gen.push_back(s+'1'+s1);
	if (k <= 2) gen.push_back(s+'2'+s1);
}

void generator() {
	for (int i = 1; i <= 26; i++) {
		string s = "1";
		for (int j = 1; j < i; j++) s += "0";
		get_palindrom(s,1);
		for (int j = 1; j < i; j++) {
			s[j] = '1';
			get_palindrom(s,2);
			for (int k = j + 1; k < i; k++) {
				s[k] = '1';
				get_palindrom(s,3);
					for (int m = k + 1; m < i; m++) {
						s[m] = '1';
						get_palindrom(s,4);
						s[m] = '0';
					}
				s[k] = '0';
			}
			s[j] = '0';
		}
		s="2";
		for (int j = 1; j < i; j++) s += "0";
		get_palindrom(s,4);
	}
}

bool comp(string b,string a) {
	if (a.length() > b.length()) return true;
	else if (b.length() > a.length()) return false;
	else {
		int i = 0;
		while ( i < a.length() && a[i] == b[i]) i++;
		if (i == a.length()) return true;
		else if (a[i] > b[i]) return true;
		else return false;
	}
}
	
int binary_search(string a, int l, int r) {
	int mid  = (l + r) / 2;
	if (gen[mid] == a) return mid;
	if (comp(a,gen[mid])) r = mid;
	else l = mid;
	if (gen[l] == a) return l;
	if (gen[r] == a) return r;
	if (comp(a,gen[l + 1]) && a!=gen[l+1]) return l;
	if (comp(gen[r - 1],a)&& a!=gen[r-1]) return r - 1;
	return binary_search(a,l,r);
}


string multiply(string a, string b) {
	int max_size = a.size() + b.size() - 1;
	string res = "";
	for (int i = 0; i < max_size;i++) res+='0';
	int p = 0;
	for (int i = 0; i < a.length(); i++) {
		for (int j = 0; j < b.length(); j++) {
			int temp = (res[max_size - i - j - 1] -'0') + (a[a.length() - i - 1] - '0') * (b[b.length() - j - 1] - '0') + p;
			res[max_size - i - j - 1] = temp % 10 + '0';
			temp /= 10;
		}
	}
	int i = 0;
	while (res[i] == 0) {
		res.erase(0,1);
	}
	return res;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	gen.clear();
	gen.push_back("1");
	gen.push_back("2");
	gen.push_back("3");
	generator();
	sort(gen.begin(), gen.end(), comp);
	for (int i = 0; i <gen.size(); i++) {
		gen[i] = multiply(gen[i],gen[i]);
	}
	int T;
	cin>>T;
	for (int t = 0; t < T; t++) {
		cout<<"Case #"<<t + 1<<": ";
		cin>>A>>B;
		int a = binary_search(A,0,gen.size()-1);
		int b = binary_search(B,0,gen.size()-1);
		int res = b - a;
		if (A == gen[a]) {
			res++;
		}
		cout<<res<<endl;
	}
	return 0;
}