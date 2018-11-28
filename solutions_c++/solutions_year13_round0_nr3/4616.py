#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
using namespace std;

bool isPalin(string s)
{
	int right = s.length()-1;
	int left = 0;

	while( left < right)
	{
		if( s[right] != s[left]) return false;
		right--;
		left ++;
	}
	return true;
}
string toString(long long s)
{
	string res;
	stringstream ss;
	ss<<s;
	ss>>res;

	return res;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int nCases;
	int cnt=0;
	cin>>nCases;
	long long begin, end;
	for(int i = 0 ; i < nCases ; i++)
	{
		cnt = 0;
		cin>>begin>>end;

		for(long long j = sqrt(begin) ; j<= end ; j++)
		{
					long long numRoot =j;
					long long dRoot = j*j;
					if(dRoot > end ) break;
					if(dRoot < begin) continue;
					if( isPalin(toString(numRoot)) && isPalin(toString(dRoot)))
					{
					//	cout<<numRoot<<" "<<dRoot<<endl;
						cnt++;
					}

		}
		/*for(long long j = begin ; j<= end ; j++)
		{
			long long numRoot =sqrt(j);
			long double dRoot = sqrt(j);

			if( numRoot == dRoot){
				if( isPalin(toString(numRoot)) && isPalin(toString(j)))
					cnt++;
			}
		}*/
		cout<<"Case #"<<(i+1)<<": "<<cnt<<endl;
	}
	return 0;
}
