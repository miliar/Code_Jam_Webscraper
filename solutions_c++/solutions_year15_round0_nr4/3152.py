#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;

string find_winner(int X,int R,int C)
{
	string gab = "GABRIEL";
	string rich = "RICHARD";
	switch(X)
	{
	case 1:
		return gab;
		break;
	case 2:
		if(((R*C)%2)==0)
			return gab;
		else
			return rich;
		break;
	case 3:
		if(((R*C)%3)!=0)
			return rich;
		else
		{
			if(R*C == 3)
				return rich;
			else
				return gab;
		}
		break;
	case 4:
		if(C<4 && R<4)
			return rich;
		else
		{
			if(R*C <12)
				return rich;
			else
				return gab;
		}
		break;
	default:
		return rich;
	}
}
int main()
{
	fstream fin("d.in",ios::in);
	fstream fout("d.out",ios::out);
	int max_tc;
	fin>>max_tc;
	int tc = 1;
	while(tc<=max_tc)
	{
		string result = "";
		int X,R,C;
		fin>>X>>R>>C;

		result= find_winner(X,R,C);
		fout<<"Case #"<<tc<<": "<<result<<endl;
		tc++;
	}
	return 0;
}