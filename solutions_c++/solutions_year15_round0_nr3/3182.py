#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>

#define OUT out
#define GETC ;

#ifndef OUT
#define OUT cout
#endif

#ifndef GETC
#define GETC getchar();
#endif

using namespace std;

int getindex(char ch);
char charoperate(int i, int j);
char signoperate(char sign1, char sign2);

int main()
{
    ifstream in("files/file.in");
    ofstream out("files/file.out");

    int cases=0;
    string line;
	const string table[]={" 1ijk", "11ijk", "ii1kj", "jjk1i", "kkji1"};
	const string sign[]={"+++++", "+++++", "++-+-", "++--+", "+++--"};

    in >> cases;
    getline(in, line);

    for(int nc=1; nc<= cases; ++nc)
    {
        OUT << "Case #" << nc << ": ";
        getline(in, line);
        stringstream ss;
        ss << line;
		long long l, x, len;
		ss >> l >> x;
		len = l * x;

		getline(in, line);
		ss.clear();
		ss << line;

		string tmp, str="";
		ss >> tmp;

		bool goti=false, gotj=false, gotk=false;

		for(long long i=0; i < x; ++i)
			str.append(tmp);

		char result, resultsign, c1, c2, c1sign;
		int c1index, c2index;

		c1 = str[0];
		c1index = getindex(c1);
		c1sign = '+';

		//long long lasti=0, lastj=0, lastk=0;

		for(long long i=1; i < len; ++i)
		{
			if(!goti && c1 == 'i' && c1sign == '+' && i < len-1)
			{
				goti = true;
				gotj = false;
				gotk = false;
				//lasti = i-1;
				c1 = str[i];
				c1index = getindex(c1);
				c1sign = '+';
				++i;
			}
			if(goti && !gotj && c1 == 'j' && c1sign == '+' && i < len)
			{
				gotj = true;
				gotk = false;
				//lastj = i-1;
				c1 = str[i];
				c1index = getindex(c1);
				c1sign = '+';
				++i;
			}
			if (i >= len) break;
			c2 = str[i];
			c2index = getindex(c2);

			result =  table[c1index][c2index];
			resultsign = signoperate(c1sign, sign[c1index][c2index]);

			c1 = result;
			c1index = getindex(c1);
			c1sign = resultsign;
		}

		if(goti && gotj && !gotk && c1 == 'k' && c1sign == '+')
			gotk = true;

		OUT << ((goti && gotj && gotk) ? "YES" : "NO") ;

        OUT << endl;
    }
    in.close();
    out.close();
    
    GETC
    return 0;
}
int getindex(char ch)
{
	switch(ch)
	{
	case '1':
		return 1;
	case 'i':
		return 2;
	case 'j':
		return 3;
	case 'k':
		return 4;
	}
	return 0;
}

char signoperate(char sign1, char sign2)
{
	if(sign1 == '+') return sign2;
	if(sign2 == '+') return '-';
	return '+';
}