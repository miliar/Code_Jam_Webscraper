/*
 * Gary Ferrao
 * https://plus.google.com/u/0/110619450313015458698
 * 00:25:17 14 April 2013 IST
 * Fair and Square

Problem
Little John likes palindromes, and thinks them to be fair (which is a fancy word
for nice). A palindrome is just an integer that reads the same backwards and
forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and 2244 are
not (even though 010=10, we don't consider leading zeroes when determining
whether a number is a palindrome).
He recently became interested in squares as well, and formed the definition of a
fair and square number - it is a number that is a palindrome and the square of a
palindrome at the same time. For instance, 1, 9 and 121 are fair and square
(being palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and
676 are not fair and square: 16 is not a palindrome, 22 is not a square, and
while 676 is a palindrome and a square number, it is the square of 26, which is
not a palindrome.
Now he wants to search for bigger fair and square numbers. Your task is, given
an interval Little John is searching through, to tell him how many fair and
square numbers are there in the interval, so he knows when he has found them
all.

Solving this problem
Usually, Google Code Jam problems have 1 Small input and 1 Large input. This
problem has 1 Small input and 2 Large inputs. Once you have solved the Small
input, you will be able to download any of the two Large inputs. As usual, you
will be able to retry the Small input (with a time penalty), while you will get
only one chance at each of the Large inputs.

Input
The first line of the input gives the number of test cases, T. T lines follow.
Each line contains two integers, A and B - the endpoints of the interval Little
John is looking at.

Output
For each test case, output one line containing "Case #x: y", where x is the case
number (starting from 1) and y is the number of fair and square numbers greater
than or equal to A and smaller than or equal to B.

Limits

Small dataset
1 ≤ T ≤ 100.
1 ≤ A ≤ B ≤ 1000.

First large dataset
1 ≤ T ≤ 10000.
1 ≤ A ≤ B ≤ 10^14.

Second large dataset
1 ≤ T ≤ 1000.
1 ≤ A ≤ B ≤ 10^100.
 */
#include <iostream>
#include <fstream>
#include <string>
#include <climits>
#define MAX 100
using namespace std;

class FairSquareInt
{
	private:
	short number[MAX];
	int length;
	
	public:
	FairSquareInt(): length(0)
	{
		number[MAX];
		for(int i=0; i<MAX; i++)
			number[i]=0;
	}
	FairSquareInt(const string str)
	{
		int i;
		length = int(str.size());
		for(i=MAX-1; i>=length; i--)
			number[i] = 0;
		for(int x=0; x<length && i>=0; x++, i--)
			number[i] = char(str[x]) - '0';
		
	}
	~FairSquareInt(){}
	FairSquareInt operator + (FairSquareInt& param)
	{
		short carry = 0;
		FairSquareInt result("0");
		for(int i=0; i<MAX; i++)
		{
			result.number[i] = number[i] + param.number[i] + carry;
			if(0<(carry=result.number[i]/10))
				result.number[i] %= 10;
		}
		int i;
		for(i=MAX-1; 0==result.number[i] && i>=0; i--);
		result.length = i+2;
		return result;
	}
	FairSquareInt operator * (FairSquareInt& param)
	{
		FairSquareInt result("0");
		for(int i=0; i<MAX; i++)
		{
			FairSquareInt temp("0");
			int tindex=i;
			short carry=0;
			for(int j=0; j<MAX; j++,tindex++)
			{
				if(MAX < tindex)
					break;
				temp.number[tindex] = number[i]*param.number[j] + carry;
				if( 0 < (carry=temp.number[tindex]/10) )
					temp.number[tindex] %= 10;
			}
			result = result + temp;
		}
		int i;
		for(i=MAX-1; 0==result.number[i] && i>=0; i--);
		result.length = i+2;
		return result;
	}
	bool operator == (FairSquareInt& param)
	{
		for(int i=0; i<MAX; i++)
			if(number[i] != param.number[i])
				return false;
		return true;
	}
	bool operator != (FairSquareInt& param)
	{
		for(int i=0; i<MAX; i++)
			if(number[i] != param.number[i])
				return true;
		return false;
	}
	bool operator < (const FairSquareInt& param)
	{
		for(int i=MAX-1; i>=0; i--)
		{
			while(i>=0 && number[i]==param.number[i])
				i--;
			return (number[i] < param.number[i]);
		}
	}
	friend ostream& operator << (ostream& out, FairSquareInt param)
	{
		for(int i=MAX-1; i>=0; i--)
				out << param.number[i];
		return out;
	}
	friend istream& operator >> (istream& in, FairSquareInt& param)
	{
		string str;
		in >> str;
		FairSquareInt result(str);
		param=result;
		return in;
	}
	bool isPalindrome()
	{
		int start=0, end=length-2;
		while(start<end)
			if(number[start++]!=number[end--])
				return false;
		return true;
	}
	void display()
	{
		for(int i=MAX-1; i>=0; i--)
			cout << number[i];
		cout << endl;
	}
};

int main()
{
	ifstream ipfile;
	ofstream opfile;
	ipfile.open("C-large-1.in");
	opfile.open("C-large-1.op");
	if(! ipfile.is_open())
	{
  		cout << "Input file not found. Exiting..." << endl;
		ipfile.close();
		opfile.close();
		return -1;
	}
	unsigned long list[48];
	list[0] = 1;
	list[1] = 4;
	list[2] = 9;
	list[3] = 121;
	list[4] = 484;
	list[5] = 10201;
	list[6] = 12321;
	list[7] = 14641;
	list[8] = 40804;
	list[9] = 44944;
	list[10] = 1002001;
	list[11] = 1234321;
	list[12] = 4008004;
	list[13] = 100020001;
	list[14] = 102030201;
	list[15] = 104060401;
	list[16] = 121242121;
	list[17] = 123454321;
	list[18] = 125686521;
	list[19] = 400080004;
	list[20] = 404090404;
	list[21] = 10000200001;
	list[22] = 10221412201;
	list[23] = 12102420121;
	list[24] = 12345654321;
	list[25] = 40000800004;
	list[26] = 1000002000001;
	list[27] = 1002003002001;
	list[28] = 1004006004001;
	list[29] = 1020304030201;
	list[30] = 1022325232201;
	list[31] = 1024348434201;
	list[32] = 1210024200121;
	list[33] = 1212225222121;
	list[34] = 1214428244121;
	list[35] = 1232346432321;
	list[36] = 1234567654321;
	list[37] = 4000008000004;
	list[38] = 4004009004004;
	list[39] = 100000020000001;
	list[40] = 100220141022001;
	list[41] = 102012040210201;
	list[42] = 102234363432201;
	list[43] = 121000242000121;
	list[44] = 121242363242121;
	list[45] = 123212464212321;
	list[46] = 123456787654321;
	list[47] = 400000080000004;
	//int index=0;
	/* //To generate FairSquareInts
	for(long l=0; l<10000000000; l++)
	{
		count = count + one;
		if(!count.isPalindrome())
			continue;
		FairSquareInt sq = count * count;
		if(sq.isPalindrome())
			cout << "list["<< index++ << "] = new FairSquareInt(\"" << sq << "\");" << endl;
	}
	*/
	int countt, t=0;
	ipfile >> countt;
	while(++t <= countt)
	{
		int keepcount = 0;
		unsigned long a, b;
		ipfile >> a >> b;
		int lowerindex=0, upperindex=47;
		while(list[lowerindex++]<a);
		lowerindex--;
		while(list[upperindex--]>b);
		upperindex++;
		opfile << "Case #" << t <<": " << (upperindex-lowerindex+1) << endl;
	}
	return 0;
}
