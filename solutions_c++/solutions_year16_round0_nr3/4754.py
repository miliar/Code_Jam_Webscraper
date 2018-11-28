#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <unordered_map>
using namespace std;
typedef unsigned long long int ULL;
string bin(unsigned int n, int N)
{
	unsigned int i;
	string s = "";
	for (i = 1 << (N-3); i > 0; i = i / 2)
		(n & i) ? s+="1" : s+="0";
	return s;
}
ULL to_base(string s,int base)
{
	ULL res = 0;
	int power = 0;
	int i;
	for (i=s.length()-1;i>=0;i--)
	{
		if (s[i] == '1')
			res += pow(base,power);
		power++; 
	}	
	return res;
}

ULL isprime(ULL n)
{
    if (n == 2 || n == 3)
        return -1;
    if (n % 2 == 0)
        return 2;
    if (n % 3 == 0)
        return 3;
    ULL i = 5;
    ULL w = 2;
    
	while (i * i <= n) {
        if (n % i == 0)
            return i;
        i += w;
        w = 6 - w;
	}
    return -1;
}

int main()
{
	int T, N, J;
	cin >> T >> N >> J;
	unsigned int start = 0;
	cout << "Case #1: " << endl;
	int count = 0;
	while(start < 1 << (N-2))
	{
		string num = "1" + bin(start, N) + "1";
		int base;
		vector <ULL> v;
		v.resize(0);
		for (base=2;base<=10;base++)
		{
			ULL res = to_base(num, base);
			ULL val = isprime(res);
			if (val == -1)
				break;
			else
				v.push_back(val);
		}
		if (v.size() == 9)
		{	
			cout << num << " ";
			for (int sz = 0; sz < 9; sz++) cout << v[sz] << " ";
			cout << endl;
			count++;
		}
		if (count == J) break;
		start++;
	}
	return 0;
}
