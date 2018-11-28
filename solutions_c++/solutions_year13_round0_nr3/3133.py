#include <cstdio>
#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
#include<sstream>
#include<iterator>
using namespace std;

int AreAll9s (string &num);
void generateNextPalindromeUtil (string &num,int n)
{
	int mid = n/2;
	bool leftsmaller = false;
	int i = mid - 1;
	int j = (n % 2)? mid + 1 : mid;
	while (i >= 0 && num[i] == num[j])
		i--,j++;

	if ( i < 0 || num[i] < num[j])
		leftsmaller = true;

	while (i >= 0)
	{
		num[j] = num[i];
		j++;
		i--;
	}

	if (leftsmaller == true)
	{
		int carry = 1;
		i = mid - 1;
		if (n%2 == 1)
		{
			num[mid] += carry;
			carry = (num[mid]-'0') / 10;
			num[mid] = ((num[mid]-'0')%10)+'0';
			j = mid + 1;
		}
		else
			j = mid;
		while (i >= 0)
		{
			num[i] += carry;
			carry =( num[i]-'0') / 10;
			num[i] = ((num[i]-'0')%10)+'0';
			num[j++] = num[i--]; // copy mirror to right
		}
	}
}
void generateNextPalindrome(string &num)
{
	int i;

	int size=num.size();
	if( AreAll9s(num) )
	{
		num.resize(size+1);
		num[0]='1';
		for( i = 1; i < size; i++ )
			num[i]='0';
		num[i]='1';
		return;
	}
	else
	{
		generateNextPalindromeUtil(num,size);
	}
}

int AreAll9s(string &num)
{
	string::iterator itr;
	for(itr = num.begin(); itr < num.end(); itr++ )
		if( *itr != '9' )
			return 0;
	return 1;
}

template<typename T> bool isPalindrome(T &arr)
{
	int size=arr.size();
	int l=0;
	int r=size-1;
	while(l<r){
		if(arr[l++]!=arr[r--]){
			return false;
		}
	}
	return true;
}
bool is_perfect_square(unsigned long long n,unsigned long long &root) 
{
	if (n < 0)
		return false;
	unsigned long long root1(round(sqrt(n)));
	root=root1;
	return n == root * root;
}

template <typename T> T StringToNumber ( const string &Text )//Text not by const reference so that the function can be used with a 
{                               //character array as argument
	stringstream ss(Text);
	T result;
	return ss >> result ? result : 0;
}
template <typename T> string NumberToString ( T Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}
int main()
{
	int testcases;
	string A,B;
	ifstream fin("fairandsquare.in");
	ofstream fout("fairandsquare.out");
	int count=1;
	fin>>testcases;
	while(testcases--){
		fin>>A;
		fin>>B;
		unsigned long long num1=StringToNumber<unsigned long long>(A);
		unsigned long long num2=StringToNumber<unsigned long long>(B);
		unsigned long long count_ans=0;
		string istr=A;
		unsigned long long i=num1;
		while(1){
			int len=istr.length();
			if(isPalindrome<string >(istr)){
				unsigned long long root;
				bool isPerfect;
				if(is_perfect_square(i,root)){
					string root_str=NumberToString<unsigned long long>(root);
					if(isPalindrome<string >(root_str))
						count_ans++;
				}
			}
			
			generateNextPalindrome(istr);
			i=StringToNumber<unsigned long long>(istr);
			if(i>num2)
				break;
		}
		fout<<"Case #"<<count<<": "<<count_ans<<endl;
		count=count+1;
	}
}
