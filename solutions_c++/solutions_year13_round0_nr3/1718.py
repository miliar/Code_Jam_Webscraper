#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class RBigInt {
private:
	string rbi;
	
public:
	RBigInt (void) {	rbi = "0"; }
	RBigInt (string c)	{	rbi = c;	}
	
	void set (string c)	{	rbi = c;	}
	void setr (string c) {
		reverse(c.begin(), c.end());	
		rbi = c;
	}
	string get (void)	{	return rbi; }
	string getr (void) {
		string c = rbi;
		reverse(c.begin(), c.end());	
		return c;	
	}
	
	int length (void) {
		return rbi.length();
	}
	
	bool isPalindrome (void) {
		int len = rbi.length(), i;
		for (i = 0; i < len/2; i++)	
			if (rbi[i] != rbi[len-1-i])	return false;
		return true;
	}
	
	void next (void) {
		int i, j, len, carry;
		len = rbi.length();
		carry = 1;
		/*mudanca na segunda metade dos nros*/
		for (i = 0, j = len-1; i < j; i++, j--) {
			if (rbi[i] <= rbi[j])	carry = 0;
			else	carry = 1;
			rbi[j] = rbi[i];
		}
		/*mudanca comecando pelo meio*/
		if (len == 1 || !carry) {
			carry = 0;
			for (i = (len-1)/2, j = len/2; i>= 0 && !carry; i--, j++) {
				if (rbi[i] != '9') {
					rbi[j] = ++rbi[i];
					carry = 1;
				} else
					rbi[j] = rbi[i] = '0';
			}
		}
		/*mudanca quando eh 9*/
		if (!carry) {
			rbi[len-1] = '1';
			string ans = "1";
			ans+=rbi;
			rbi = ans;
		}
	}

	RBigInt operator + (RBigInt b) {
		string s = b.get();
		int n, carry = 0, i;
		string ans;
		for (i = 0; i < rbi.length(); i++) {
			n = rbi[i]-'0'+carry;
			if (i < s.length())	n += s[i]-'0';
			if (n >= 10) {
				carry = 1;
				n -= 10;
			} else	carry = 0;
			ans += n+'0';
		}
		for (; i < s.length(); i++) {
			n = s[i]-'0'+carry;
			if (n >= 10) {
				carry = 1;
				n -= 10;
			} else	carry = 0;
			ans += n+'0';
		}
		if (carry)	ans += '1';
		return RBigInt (ans);
	}

	RBigInt operator + (const string& s) {
		int n, carry = 0, i;
		string ans;
		for (i = 0; i < rbi.length(); i++) {
			n = rbi[i]-'0'+carry;
			if (i < s.length())	n += s[i]-'0';
			if (n >= 10) {
				carry = 1;
				n -= 10;
			} else	carry = 0;
			ans += n+'0';
		}
		for (; i < s.length(); i++) {
			n = s[i]-'0'+carry;
			if (n >= 10) {
				carry = 1;
				n -= 10;
			} else	carry = 0;
			ans += n+'0';
		}
		if (carry)	ans += '1';
		return RBigInt (ans);
	}
	
	RBigInt operator * (RBigInt b) {
		string s = b.get(), tmp;
		RBigInt ans, curr;
		int i, j, len1 = rbi.length(), len2 = s.length(), cur1, cur2, carry = 0, out;
		for (i = 0; i < len1; i++) {
			tmp.clear();
			for (j = 0; j < i; j++)	tmp += '0';
			cur1 = rbi[i]-'0';
			for (j = 0; j < len2; j++) {
				cur2 = s[j]-'0';
				out = cur1*cur2+carry;
				if (out/10) {
					carry = out/10; 
					out %= 10;
				}	else	carry = 0;
				tmp += '0'+out;
			}
			while (carry)	{
				tmp += carry%10+'0';
				carry /= 10;
			}
			ans = ans + tmp;
		}
		return ans;
	}
};

int cmp (string a, string b) {
	int i = 0;
	if (a.length() != b.length())	return a.length() - b.length();
	while (i < a.length() && a[i] == b[i])	i++;
	if (i == a.length())	return 0;
	return a[i]-b[i];
}

vector <string> v;
int bb (string A) {
	int beg = 0, end = v.size()-1, h, x;
	while (beg <= end) {
		h = (beg+end)/2;
		x = cmp(v[h], A);
		if (!x)	break;
		else if (x > 0)	end = h-1;
		else	beg = h+1;
	}
	return h;
}

int main (void) {
	int T, c, a, b;
	RBigInt sq, curr;
	string A, B;
	int clen = 0;
	while (curr.length() < 8) {
		/*if (curr.length() > clen) {
			clen++;
			cout << clen << endl;
		}*/
		curr.next();
		sq = curr*curr;
		if (sq.isPalindrome())	v.push_back (sq.get());
	}
	//for (int i = 0; i < v.size(); i++)	cout << v[i] << endl;
	//return 0;
	cin >> T;
	for (c = 1; c <= T; c++) {
		cout << "Case #" << c << ": ";
		cin >> A >> B;
		a = bb(A);
		b = bb(B);
		if (cmp(B, v[b]) < 0)	b--;
		if (cmp(v[a], A) < 0)	a++;
		cout << b-a+1 << endl;
	}
	return 0;
}
