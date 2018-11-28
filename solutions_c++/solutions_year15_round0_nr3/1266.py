#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <bitset>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <list>
#include <climits>
#include <assert.h>

//#include <gmpxx.h>

#ifdef _WIN32
#include <time.h>
#else
#include <sys/time.h>
#endif

using namespace std;
#define ll long long

int table[5][5]=
{
	0,0,0,0,0,
	0, 1, 2, 3, 4,
	0, 2, -1, 4, -3,
	0, 3, -4, -1, 2,
	0, 4, 3, -2, -1
};

int main()
{
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;

		ll L,X;
		cin>>L>>X;

		string s;
		cin>>s;

		for(int i=0;i<s.length();++i)
		{
			if(s[i]=='1')
			{
				s[i]=1;
			}
			else if(s[i]=='i'){
				s[i]=2;
			}else if(s[i]=='j'){
				s[i]=3;}
			else if(s[i]=='k')
			{s[i]=4;}
		}

		string in;
		for(int i=0;i<X;++i)
		{
			in += s;
		}

		int c = in[0];
		bool ok = false;
		for(int i=1;i<in.length();++i)
		{
			if(c==2)
			{
				int c2 = in[i];
				for(int j = i + 1; j < in.length(); ++j)
				{
					if(c2==3)
					{
						int c3 = in[j];
						for(int k=j+1; k< in.length(); ++k)
						{
							int sgn3 = c3 < 0 ? -1 : 1;
							c3 = table[sgn3*c3][in[k]];
							c3*=sgn3;
						}

						if(c3 == 4)
						{
							ok = true;
							break;
						}
					}
					if(ok)
						break;
					
					int sgn1= c2 < 0 ? -1 : 1;
					c2 = sgn1*table[sgn1*c2][in[j]];
				}
				if(ok)
					break;
			}
			int sgn0 = c < 0 ? -1 : 1;
			c = sgn0*table[sgn0*c][in[i]];
		}
		
		string result = "NO";
		if(ok)
			result = "YES";
		cout<<"Case #"<<_t+1<<": "<<result<<endl;
	}
}
