#include <bits/stdc++.h>
using namespace std;
vector <string> vec;
vector <int> vec1;
int main()
{
	int tc;
	ios_base::sync_with_stdio(false);
	ifstream cin("A-large.in") ;
	ofstream cout("211.txt") ;
	
	cin>>tc;
	vec.push_back("ZERO");
	vec.push_back("ONE");
	vec.push_back("TWO");
	vec.push_back("THREE");
	vec.push_back("FOUR");
	vec.push_back("FIVE");
	vec.push_back("SIX");
	vec.push_back("SEVEN");
	vec.push_back("EIGHT");
	vec.push_back("NINE");

	int zz=1;
	while(tc--)
	{
		string str;
		cin>>str;
		int JK=0;
		int arry[26],asw[15];
		for(int i=0;i<26;i++)arry[i]=0;
		while(str[JK]!='\0')
		{
			arry[str[JK]-'A']++;
			JK++;
		}
		int x=asw[0]=arry['Z'-'A'];
		for(int i=0;i<vec[0].size();i++)
		arry[vec[0][i]-'A']-=x;
		int y=asw[2]=arry['W'-'A'];
		for(int i=0;i<vec[2].size();i++)
		arry[vec[2][i]-'A']-=y;
		x=asw[4]=arry['U'-'A'];
		for(int i=0;i<vec[4].size();i++)
		arry[vec[4][i]-'A']-=x;
		x=asw[8]=arry['G'-'A'];
		for(int i=0;i<vec[8].size();i++)
		arry[vec[8][i]-'A']-=x;
		x=asw[6]=arry['X'-'A'];
		for(int i=0;i<vec[6].size();i++)
		arry[vec[6][i]-'A']-=x;
		x=asw[5]=arry['F'-'A'];
		for(int i=0;i<vec[5].size();i++)
		arry[vec[5][i]-'A']-=x;
		x=asw[7]=arry['V'-'A'];
		for(int i=0;i<vec[7].size();i++)
		arry[vec[7][i]-'A']-=x;
		x=asw[9]=arry['I'-'A'];
		for(int i=0;i<vec[9].size();i++)
		arry[vec[9][i]-'A']-=x;
		x=asw[1]=arry['O'-'A'];
		for(int i=0;i<vec[1].size();i++)
		arry[vec[1][i]-'A']-=x;
		x=asw[3]=arry['T'-'A'];
		for(int i=0;i<vec[3].size();i++)
		arry[vec[3][i]-'A']-=x;
		cout<<"Case #"<<zz<<": ";
		for(int i=0;i<10;i++)
		{
			for(int JK=0;JK<asw[i];JK++)
			{
				cout<<i;
			}
		}
		cout<<"\n";
		zz++;
		
	}
}
