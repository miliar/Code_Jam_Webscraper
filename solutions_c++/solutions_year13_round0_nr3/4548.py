#include <fstream>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

bool IsPalindrom(unsigned long long a);

int main()
{
	fstream ifs("Google.in");
	ofstream ofs("Google.out");
	unsigned  long long N,A,B,count=0;
	ifs>>N;
	for(int i=1;i<=N;i++)
	{
		count=0;
		ifs>>A>>B;
		for(unsigned  long long j=1;j<=(unsigned long long)sqrt(B);j++)
		{
			if(IsPalindrom(j)==true)
			{
				if(IsPalindrom(j*j)==true && j*j>=A)
				{
						count++;
				}
			}
		}
		ofs<<"Case #"<<i<<":"<<" "<<count<<endl;
	}
}


bool IsPalindrom(unsigned long long a)
{
	ostringstream ss;
	ss<<a;
	string str=ss.str();
	for(int i=0;i<str.size();i++)
	{
		if(str[i]!=str[str.size()-1-i]) return false;
	}
	return true;
}
