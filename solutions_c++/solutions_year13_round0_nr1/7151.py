#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <map>
//cout.precision(0);
//cout.setf(ios_base::fixed)

using namespace std;

int main()
{
      freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int n;
	
	int cunt=1;
	cin>>n;
	while(n--)
	{
		char ch[4][4];

		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>ch[i][j];
		string h;
		bool fx=false,fo=false;
		for(int i=0;i<4;i++)
		{
			h.clear();
			h+=ch[i][0];h+=ch[i][1];h+=ch[i][2];h+=ch[i][3];
			if(h=="XXXX" || h=="XXXT" || h=="TXXX" || h=="XTXX"||h=="XXTX")
				fx=true;

		}
		if(!fx)
		{
			for(int i=0;i<4;i++)
		{
			h.clear();
			h+=ch[0][i];h+=ch[1][i];h+=ch[2][i];h+=ch[3][i];
			if(h=="XXXX" || h=="XXXT" || h=="TXXX" || h=="XTXX"||h=="XXTX")
				fx=true;

		}
		}
		if(!fx)
		{
			
			h.clear();
			h+=ch[0][0];h+=ch[1][1];h+=ch[2][2];h+=ch[3][3];
			if(h=="XXXX" || h=="XXXT" || h=="TXXX" || h=="XTXX"||h=="XXTX")
				fx=true;
			h.clear();
			h+=ch[3][0];h+=ch[2][1];h+=ch[1][2];h+=ch[0][3];
			if(h=="XXXX" || h=="XXXT" || h=="TXXX" || h=="XTXX"||h=="XXTX")
				fx=true;
		}

		///////////////
		for(int i=0;i<4;i++)
		{
			h.clear();
			h+=ch[i][0];h+=ch[i][1];h+=ch[i][2];h+=ch[i][3];
			if(h=="OOOO" || h=="OOOT" || h=="TOOO" || h=="OTOO"||h=="OOTO")
				fo=true;

		}
		if(!fo)
		{
			for(int i=0;i<4;i++)
		{
			h.clear();
			h+=ch[0][i];h+=ch[1][i];h+=ch[2][i];h+=ch[3][i];
			if(h=="OOOO" || h=="OOOT" || h=="TOOO" || h=="OTOO"||h=="OOTO")
				fo=true;

		}
		}
		if(!fo)
		{
			
			h.clear();
			h+=ch[0][0];h+=ch[1][1];h+=ch[2][2];h+=ch[3][3];
			if(h=="OOOO" || h=="OOOT" || h=="TOOO" || h=="OTOO"||h=="OOTO")
				fo=true;
			h.clear();
			h+=ch[3][0];h+=ch[2][1];h+=ch[1][2];h+=ch[0][3];
			if(h=="OOOO" || h=="OOOT" || h=="TOOO" || h=="OTOO"||h=="OOTO")
				fo=true;
		}
		/////////////
		bool fc=false;
		if(!fx&&!fo)
		{
			for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(ch[i][j]!='.')
					continue;
				else
					fc=true;
		}


		if(fx)
		{
			cout<<"Case #"<<cunt<<": "<<"X won"<<endl;
		}
		else if(fo)
		{
				cout<<"Case #"<<cunt<<": "<<"O won"<<endl;
		}
		else if (fc)
		{
			cout<<"Case #"<<cunt<<": "<<"Game has not completed"<<endl;}
		else
				cout<<"Case #"<<cunt<<": "<<"Draw"<<endl;
		cunt++;
	}
	return 0;
}
