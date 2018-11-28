#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>

#include <fstream>

using namespace std;



int main()
{
	string line;
	int testcases;
	ifstream infile;
	infile.open ("Tictactoe.txt");
	getline(infile,line);
	stringstream st;
	st << line;
	st >>testcases;
	ofstream outfile;
	outfile.open ("Ticsolution.txt");
	for(int i=0;i<testcases;i++)
	{
		char result=0;
		bool notcompleted = false;
		char input[4][4];
		for(int j=0;j<4;j++)
		{
			getline(infile,line);
			stringstream st;
			st << line;
			st >>input[j][0]>>input[j][1]>>input[j][2]>>input[j][3];
			if(input[j][0]=='.' ||input[j][1]=='.' ||input[j][2]=='.'|| input[j][3]=='.')
				notcompleted = true;
		}
		getline(infile,line);
		//Horizontal
		char a=input[0][0],b=input[0][1],c=input[0][2],d=input[0][3];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.')//Horizontal
			result = a;
		
		a=input[1][0],b=input[1][1],c=input[1][2],d=input[1][3];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.')//Horizontal
			result = a;

		a=input[2][0],b=input[2][1],c=input[2][2],d=input[2][3];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.')//Horizontal
			result = a;

		a=input[3][0],b=input[3][1],c=input[3][2],d=input[3][3];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.')//Horizontal
			result = a;
		
	//******************************************************************************//
		//vertical
		a=input[0][0],b=input[1][0],c=input[2][0],d=input[3][0];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.' )//Horizontal
			result = a;

		a=input[0][1],b=input[1][1],c=input[2][1],d=input[3][1];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.')//Horizontal
			result = a;

		a=input[0][2],b=input[1][2],c=input[2][2],d=input[3][2];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.')//Horizontal
			result = a;

		a=input[0][3],b=input[1][3],c=input[2][3],d=input[3][0];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.')//Horizontal
			result = a;

		///***************************************************************************88//

		a=input[0][0],b=input[1][1],c=input[2][2],d=input[3][3];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.')//Horizontal
			result = a;

		a=input[3][0],b=input[2][1],c=input[1][2],d=input[0][3];
		if(a =='T')a=b;
		else if(b=='T') b=c;
		else if(c=='T') c= d;
		else if(d =='T') d =a;
		if(a==b && b==c && c==d && a!='.' )//Horizontal
			result = a;

		if(result == 0 )
		{
			if(notcompleted)
				outfile <<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
			else
				outfile<<"Case #"<<i+1<<": "<<"Draw"<<endl;
		}
		else
			outfile <<"Case #"<<i+1<<": "<<result<<" won"<<endl;
}


	return 0;
}
 