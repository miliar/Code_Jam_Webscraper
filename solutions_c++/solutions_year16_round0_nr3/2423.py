#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ull;

vector < ull > liczby;
vector < ull > dzielniki;

ull pierwsza(ull x)
{
	for(ull i=9; i*i <= x; i++)
		if (x%i == 0)
			return i;
	return 0;
}

string dectobin(ull x)
{
	string s;
	while(x > 0)
	{
		if (x&1)
			s +='1';
		else
			s+='0';
		x/=2;
	}
	reverse(s.begin(), s.end());
	return s;
}

int bin2dec(const char* binary)
{
    ull len,dec=0,i,exp;

    len = strlen(binary);
    exp = len-1;

    for(i=0;i<len;i++,exp--)
        dec += binary[i]=='1'?pow(2,exp):0;
    return dec;
}

ull bin2hex(ull bin)
{
	ull res = 0, pom = 1;
	while(bin > 0)
	{
		if (bin&1)
			res += pom;
		pom*=6;
		bin/=2;
	} 
	return res;
}

int main()
{
	ull pom1 = bin2dec("1010101010101010"), pom2 = bin2dec("101010101010101");
	ull dl = 16, ile = 50;
	ull pomm = dl-1;
	for(int i=(1<<pomm)+1; liczby.size() < ile; i+=2)
	{
		int z1 = __builtin_popcount(pom1&i), z2 = __builtin_popcount(pom2&i);
		if (__builtin_popcount (i) % 2 == 1 || z1 % 3 != 0 || z2 % 3 != 0)
			continue;
		ull pom = pierwsza(bin2hex(i));
		if (pom == 0)
			continue;
		liczby.push_back(i);
		dzielniki.push_back(pom);
	}
	cout <<"Case #1:\n";
	for(int i=0; i<ile; i++)
	{
		cout << dectobin(liczby[i])<<" 3 2 3 2 ";
		cout << dzielniki[i] << " ";
		cout <<"2 3 2 3";
		cout << endl;
		
	}
}
