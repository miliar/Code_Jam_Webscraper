#include <iostream>
#include <cstring>
#include <string.h>
#include <stdexcept>
#include <sstream>
#define FOR(m,c) for(int m = 0 ; m < c ; m++)
#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()
using namespace std;
bool CheckSequence(string arr)
{
	int sum = 0 , s = 0;
	//bool ret = false;
	for(int ln = 0 ; ln < arr.length() ; ln++) 
	{
		for(char n = '0'; n <= '9' , s != 1; n++)
		{
			if(arr.at(ln) == n)
			{
			++sum;
			s = 1;
		}
		}
		s= 0;
		
		}
	return (sum==10?true:false);
}
bool Check(string a , string b , int d)
{
	int goon2 = 0;
	for(int c = 0; c < a.length() ; c++)
		{
			if(a.at(c) == b.at(d))
			{
				++goon2;
			}
		}
	return (goon2 == 0 ? true:false);
}
main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int nt = 0 , nav;
	int nfs[100];
	int test ;
	scanf("%d",&test);
	FOR(nav,test)
	{
		scanf("%d",&nt);
		nfs[nav] = nt;
	}
	nt = 0;
	int n= 0;
	int i = 1;
	string number =" ";
	string arr = "";
	int goon2 = 0;
	bool goon = true;
	for(int tcase = 0 ;  tcase < test ; tcase++)
	{
		nt = nfs[tcase];
		goon = true;
		i = 1;
		 number =" ";
			arr = "";
			goon2 = 0;
	while(goon && nt != 0)
	{
		n = nt * i;
		number = SSTR(n);
		for(int d = 0; d < number.length() ; d++)
		{
		if(Check(arr,number,d))
		{
		arr.append(1,number.at(d));
		}
		}
				if(CheckSequence(arr))
		{
			goon = false;
			}
	i++;			
	}
	if(nt == 0) 
	cout <<  "Case #" << tcase+1 << ": INSOMNIA\n";
	else
	cout <<  "Case #" << tcase+1 << ": " << number <<"\n";
}
exit(0);
}

