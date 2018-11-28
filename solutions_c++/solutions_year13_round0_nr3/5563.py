#include <iostream>
#include <fstream>
#include <cmath>
#define FILENAME_IN "C-small-attempt0.in"
#define FILENAME_OUT "C-small-attempt0.out"
using namespace std;
typedef long long int LLInt;
LLInt divLen = 0;
bool oddEvenFlag = false; // false is È¦¼ö true is Â¦¼ö
LLInt getNumberLength(LLInt v)
{
	LLInt len=1, rep=10;
	while( 1 )
	{
		if( v/rep == 0 )
			break;
		rep*=10;
		++len;
	}
	return len;
}
void makeStringToInt(LLInt* v, char str[])
{
	LLInt mul=1;
	for( LLInt rep=strlen(str)-1; rep >= 0; --rep )
	{
		*v = *v%mul + (str[rep]-'0')*mul;
		mul *= 10;
	}
}
LLInt makeIntToString(LLInt v, char str[])
{
	LLInt mul = 1, idx=0, tmp;
	while(1)
	{
		tmp = v/mul;
		if( tmp == 0 )
			break;
		str[idx] = tmp%10 + '0';
		mul *= 10;
		++idx;
	}
	str[idx] = 0;
	return idx;
}
void InitMakePalindromes(char str[], LLInt numLen)
{
	LLInt rep=0;
	for( rep=0; rep < numLen; ++rep )
		str[rep] = '1';
	str[rep] = 0;
}
LLInt makePalindromes(char str[], LLInt* numLen)
{
	LLInt rtv=0, rep, copyRep;
	bool upperFlag = true;
	if( oddEvenFlag ) // Â¦¼ö
		rep = divLen-1, copyRep = divLen;
	else
		rep = divLen, copyRep = divLen+1;
	for(; rep >= 0; --rep )
	{
		if( str[rep] != '9' ) {
			upperFlag = false;
			++str[rep];
			break;
		}
		else {
			if( (rep == divLen-1 && oddEvenFlag) ||
				(rep == divLen && !oddEvenFlag ) )
				str[rep] = '0';
		}
	}
	if( upperFlag ) {
		if( !oddEvenFlag ) // È¦¼ö¸é 
			*numLen += 1, divLen += 1;
		else
			*numLen += 1;
		oddEvenFlag = !oddEvenFlag;
		InitMakePalindromes(str, *numLen);
	}
	else {
		for( rep=divLen-1; rep >= 0; --rep )
			str[copyRep++] = str[rep];
	}
	makeStringToInt(&rtv, str);
	return rtv;
}
bool isPalindromes(LLInt v)
{
	bool rtv = true;
	char tmp[102];
	LLInt rep, cmpRep, numLen;
	numLen = makeIntToString(v,  tmp);
	numLen%2 == 0 ? cmpRep = numLen/2 : cmpRep = numLen/2+1;
	for( rep = numLen/2-1; rep >= 0; --rep, ++cmpRep )
	{
		if( tmp[rep] != tmp[cmpRep] ) {
			rtv = false;
			break;
		}
	}
	return rtv;
}
int main(void)
{
	ifstream in;
	ofstream out;
	in.open( FILENAME_IN, ios::in);
	out.open( FILENAME_OUT, ios::out);
	int testCase;
	LLInt A,B;
	in >> testCase;
	for( int testCount=0; testCount < testCase; ++testCount )
	{
		LLInt answer = 0;
		char valueStr[102];
		in >> A >> B;
		LLInt numLen = getNumberLength(sqrt((float)A)+0.9f);
		divLen  = numLen/2;
		LLInt curPal = 0, mulPal=0;
		oddEvenFlag = numLen%2 == 0 ? true : false; // Â¦¼ö¸é true
		InitMakePalindromes(valueStr, numLen);
		makeStringToInt(&curPal, valueStr);
		mulPal = curPal*curPal;
		while( mulPal <= B )
		{
			if( isPalindromes(mulPal) && mulPal >= A) {
				++answer;
			}
			curPal = makePalindromes( valueStr, &numLen);
			mulPal = curPal * curPal;
		}
		out << "Case #" << testCount+1 <<": " << answer << endl;
	}
	in.close();
	out.close();
	return 0;
}