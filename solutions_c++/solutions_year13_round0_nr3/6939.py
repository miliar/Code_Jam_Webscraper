#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <ctype.h>
#include <bitset>
#include <sstream> 
using namespace std;
string x;
int xs , h ;
int  y ;
bool palindrome ()
{
	for (int i=0 , j= xs-1 ; i<=h ; ++i , --j)
		if(x[i]!=x[j])
			return false;
	return true;
}

bool squares (int x)
{
	y = int ( sqrt( double (x)));
	if (y*y != x )
		return false;
	return true;
}

int main ()
{
		//freopen("myDearInput.in", "r", stdin);

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("2.out", "w", stdout);
	bool p , m;
	int t , a , r , i  , count , c=1 ;
	cin >> t ;
	while ( t-- )
	{
		count = 0 ;
		cin >> a >> r ;
		for (i=a ; i<= r ; ++i)
		{
			stringstream ss;
			ss << i ;
			ss >> x ;
			xs=x.size();h=xs/2;
			if(xs!=1 && xs%2!=0)
				++h;
			if (palindrome())
			{
				if (squares(i) )
				{
					stringstream ss;
					ss << y ;
					ss >> x ;
					xs=x.size() ;  h=xs/2;
					if(xs!=1 && xs%2!=0)
						++h;
					if (palindrome() )
						++ count;
				}
			}


		}
		cout<<"Case #"<<c++<<": "<<count<<endl;

	}
	return 0;
}