#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stack>
using namespace std;
bool increseStr(string& str) {
	int len = str.length();
	int upper = 1;
	int index = len - 2;
	while (index > 0 && upper == 1) {
		if (str[index] == '0') {
			str[index] = '1';
			upper = 0;
		}
		else {
			str[index] = '0';
		}
		index--;
	}
	if (index == 0 || upper == 1)return false;
	return true;
}
bool isBigger(string& str1, string& str2,int base) {
	if (str1.length() > str2.length())return true;
	else if (str1.length() < str2.length())return false;
	long long num1=0, num2=0;
	int len1 = str1.length(), len2 = str2.length();
	int index = len1 - 1;
	long long multiplier = 1;
	while (index >= 0) {
		num1 += (str1[index] - '0')*multiplier;
		index--;
		multiplier *= base;
	}
	index = len2 - 1;
	multiplier = 1;
	while (index >= 0) {
		num2 += (str2[index] - '0')*multiplier;
		index--;
		multiplier *= base;
	}
	return num1 > num2;
}
string subtract(string& str1, string& str2, int base) {
	int len1 = str1.length(), len2 = str2.length();
	int upper = 0;
	int index1 = len1 - 1, index2 = len2 - 1;
	stack<int>resstack;
	while (index1 >= 0 && index2 >= 0) {
		if (str1[index1] - upper < str2[index2]) {
			resstack.push(str1[index1] - upper + base - str2[index2]);
			upper = 1;
		}
		else {
			resstack.push(str1[index1] - upper - str2[index2]);
			upper = 0;
		}
		index1--; index2--;
	}
	while (index1 >= 0) {
		if (str1[index1] - upper < '0') {
			resstack.push(str1[index1] - upper + base - '0');
			upper = 1;
		}
		else {
			resstack.push(str1[index1] - upper - '0');
			upper = 0;
		}
		index1--;
	}
	ostringstream ostr;
	bool zeroBegin = true;
	while (!resstack.empty()) {
		if (!zeroBegin)ostr << resstack.top();
		else {
			if (resstack.top() != 0) {
				ostr << resstack.top();
				zeroBegin = false;
			}
		}
		resstack.pop();
	}
	return ostr.str();
}
string multiply(string str, int multiplier, int base) {
	int len = str.length();
	int index = len - 1;
	int upper = 0;
	stack<char>resstack;
	while (index >= 0) {
		int cur = (str[index] - '0')*multiplier + upper;
		resstack.push(cur%base + '0');
		upper = cur / base;
		index--;
	}
	if (upper > 0)resstack.push(upper+'0');
	ostringstream ostr;
	while (!resstack.empty()) {
		ostr << resstack.top();
		resstack.pop();
	}
	return ostr.str();
}
string divide(string& origin, string& divisor,int base,string& tail) {
	ostringstream ostr,resstream;
	int len = origin.length();
	int index = 0;
	bool zeroBegin = true;
	while (index < len) {
		ostr << origin[index++];
		while (index<len&&isBigger(divisor, ostr.str(), base)) {
			if (!zeroBegin)resstream << 0;
			ostr << origin[index++];
		}
		if (!isBigger(divisor, ostr.str(), base)) {
			for (int i = 1; i < base; i++) {
				string multiplyStr = multiply(divisor, i, base);
				string left = subtract(ostr.str(), multiplyStr, base);
				if (isBigger(divisor, left, base)) {
					ostr.str("");
					ostr << left;
					resstream << i;
					zeroBegin = false;
					break;
				}
			}
		}
	}
	tail = ostr.str();
	return resstream.str();
}
void increaseDivisor(string& str,int base) {
	int upper = 1;
	int len = str.length();
	int index = len - 1;
	while (index >= 0&&upper==1) {
		if (str[index]-'0'<base-1) {
			upper = 0;
			str[index]++;
			break;
		}
		else {
			str[index] = '0';
			upper = 1;
		}
		index--;
	}
	if (upper == 1) {
		ostringstream ostr;
		ostr << '1' << str;
		str = ostr.str();
	}
}

long long translate(string str, int base) {
	long long res = 0;
	int len = str.length(), index = len - 1;
	long long multiplier = 1;
	while (index >= 0) {
		res += (str[index] - '0')*multiplier;
		multiplier *= base;
		index--;
	}
	return res;
}
long long isPrime(long long num) {
	long long limit = sqrt(num);
	long long index = 2;
	while (index <= limit) {
		if (num%index == 0)return index;
		index++;
	}
	return -1;
}
bool isJamCoin(string& str, vector<long long>& factors) {
	/*for (int i = 2; i <= 10; i++) {
		string tail = "";
		string divisor = "1";
		increaseDivisor(divisor, i);
		string dealer = divide(str, divisor, i, tail);
		while (tail.length() != 0 && !isBigger(divisor, dealer, i)) {
			increaseDivisor(divisor, i);
			dealer = divide(str, divisor, i, tail);
		}
		if (isBigger(divisor, dealer, i))return false;
		else factors[i - 2] = dealer;
	}
	return true;*/
	for (int i = 2; i <= 10; i++) {
		int factor = isPrime(translate(str, i));
		if (factor != -1) {
			factors[i - 2] = factor;
		}
		else {
			return false;
		}
	}
	return true;
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int caseCount = 0;
	scanf("%d", &caseCount);
	for (int i = 0; i < caseCount; i++) {
		int N = 0, J = 0;
		scanf("%d %d", &N, &J);
		cout << "Case #" << i + 1 << ": " << endl;
		ostringstream ostr;
		ostr << "1";
		for (int j = 0; j < N - 2; j++)ostr << "0";
		ostr << "1";
		string initStr = ostr.str();
		for (int j = 0; j < J; j++) {
			vector<long long>factors(9);
			while (!isJamCoin(initStr, factors)) {
				increseStr(initStr);
			}
			cout << initStr;
			for (long long f : factors) {
				cout << " " << f;
			}
			cout << endl;
			increseStr(initStr);
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}