// 09 Apr 2016 Code Jam
// Author: Sridhar Krishnan
#include<iostream>
#include<string>
#include<sstream>
#include <iomanip> // std::setprecision
using namespace std;
typedef unsigned long long ull;

// Number to String
template <typename T>
std::string NumberToString ( T Number )
{
	std::ostringstream ss;
	// Avoiding automatic exponential conversion using [std::fixed and std::setprecision(0) ]
	ss << std::fixed<< std::setprecision(0) << Number; // Number to String Conversion
	return ss.str();
}

int main()
{
	freopen("Input.in", "rt", stdin);
	freopen("Output.out", "wt", stdout);

	int a[10] = {0};
	int f=2;
	ull n = 0, m = 0,ni = 0,tc =0;

	cin>> ni;
	for( tc =0; tc < ni; ++tc)
	{
		cin>>n;
		m = n;
		f = 2;
		for(int i=0; i<10; ++i) a[i] = 0;
		while(1)
		{ 
			if(m == 0) break;
			string str = NumberToString(n);
			for(unsigned int i =0; i<str.size(); ++i)
			{
				a[str[i] - '0'] = 1;				
			}

			int sum = 0;
			for(int i =0; i<10; ++i)
			{
				sum += a[i];
			}

			if(sum == 10)
				break;
			else
			{
				n = m * f;
				f++;
			}
		}
		if(m == 0) cout<<"Case #"<<tc+1<<": "<<"INSOMNIA"<<endl;
		else cout<<"Case #"<<tc+1<<": "<<m*(f-1)<<endl;
	}
	return 0;
}