#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <math.h>
using namespace std;






#define SMALL
//#define LARGE

bool Is_palin(string s)
{
	string temp(s.rbegin(),s.rend());
	if(temp==s)
		return true;
	else
		return false;
}

int main ()
{
	//freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	int T,A,B,count;
	cin>>T;
	
	
	for(int c=0;c<T;c++)
	{
		count=0;
		cin>>A>>B;
		
		for(int i=A;i<=B;i++)
		{
			ostringstream s1,s2;
			s1<<i;
			string temp=s1.str();
			if(Is_palin(temp))
			{
				float x=sqrt((double)i);
				if(x==(int)x)
				{
					s2<<(int)x;
					string temp1=s2.str();
					if(Is_palin(temp1))
						count++;
				}
			}
		}

		printf("Case #%d: ",c+1);
		cout<<count<<endl;
		

	}
		

	
	

	return 0;
}