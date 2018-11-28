#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
bool isPalindrome(long long);
long long isSquare(long long);
using namespace std;

int main()
{
	ifstream in("C-small-attempt0.in");
	//ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	long long A,B;
	long long count = 0;
	in>>T;
	for(int t = 1;t<=T;t++)
	{
		in>>A>>B;
		count = 0;
		for(long long i = A;i<=B;i++)
		{
			if(isPalindrome(i)&&isPalindrome(isSquare(i)))
				count ++;
		}
		out<<"Case #"<<t<<": "<<count<<endl;
	}
	return 0;
}

bool isPalindrome(long long a)
{
	if(a==-1)
		return false;
	string s;
	stringstream ss;
	ss<<a;
	s = ss.str();
	int size = s.size();
	if(size==1)
		return true;
	for(int i = 0,j = size-1;i<j;i++,j--)
	{
		if(s[i] != s[j]) return false;
	}
	return true;
}

long long isSquare(long long a)
{
	long long left = 0;
	long long right = a;
	long long mid;
	
	while(left<=right)
	{
		mid = left+(right-left)/2;
		if(mid*mid == a)
			return mid;
		else if(mid*mid<a)
			left = mid+1;
		else 
			right = mid-1;
	}
	return -1;
}
