//test case is weak saying NO for ijkiiiiiiii but it should be yes.
#include <iostream>
#include <fstream>
using namespace std;
#define lld long long 
char s[100005];
int a[5][5];
int hash(char c)
{
	return (c-'g');
}

void fill_arr()
{
	a[1][1]=1;
	a[1][2]=2;
	a[1][3]=3;
	a[1][4]=4;

	a[2][1]=2;
	a[2][2]=-1;
	a[2][3]=4;
	a[2][4]=-3;

	a[3][1]=3;
	a[3][2]=-4;
	a[3][3]=-1;
	a[3][4]=2;

	a[4][1]=4;
	a[4][2]=3;
	a[4][3]=-2;
	a[4][4]=-1;
}
int main()
{

	int t,flgi,flgj,flgk,tc,sign,ti;
	lld l,x,j,i;
	fstream fin,fout;
	
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);
	fill_arr();
	fin>>t;
	
	for(ti=1;ti<=t;ti++)
	{
		fin>>l>>x;

		fin>>s;

		 tc=1;
		 sign=0;

		flgi=0;
		flgj=0;
		flgk=0;

		for(j=1;j<=x;j++)
		{

			for(i=0;i<l;i++)
			{
				if(tc<0)
				{
					sign=(sign+1)%2;
					tc=-tc;
				}

				tc=a[tc][hash(s[i])];

				if(sign)
				{
					tc=-tc;
					sign=0;
				}


				if(tc==2&&!flgi)
				{
					flgi=1;
					tc=1;
					sign=0;
				}
				else if(flgi&&tc==3&&!flgj)
				{
					flgj=1;
					tc=1;
					sign=0;
				}

			}
		}
		if(flgi&&flgj&&tc==4)
		{

			fout<<"Case #"<<ti<<": "<<"YES\n";

		}
		else
		{
			fout<<"Case #"<<ti<<": "<<"NO\n";
		}
		
	}
	


}