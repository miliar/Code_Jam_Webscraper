#include <fstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<string>
#include<limits.h>
#include<map>

using namespace std;

int main (int argc, char const* argv[])
{
	int n,srcBase=10,tarBase=10,decNum=0,inlen=0,reminder=0,numInversions=0,winFlag=0,rowSum[4],colSum[4],diag1=0,diag2=0,notYetFinished=0;
	string inputLine ;
	vector<string> allLines;
	int done =0;
	
	ifstream cin("A-large.in");
	cin>>n;
	ofstream output;
	output.open("output.txt");
	
	for ( long int I = 1; I <= n; I++ )
	{
		done=0;notYetFinished=0,diag1=0,diag2=0;
		allLines.clear();
		for (int j = 0; j < 4; j++)
		{
		    cin>>inputLine;
		    allLines.push_back(inputLine);
		}
		for(int i=0;i<4;i++)
		{
			rowSum[i]=0;
			colSum[i]=0;
		}

		for(int i=0;i<4;i++)
		{
			numInversions = 0;
			for(int j=0;j<4;j++)
			{
				rowSum[i]+=(int)(allLines[i][j]);
				colSum[j]+=(int)(allLines[i][j]);
				if(i==j)	diag1+=(int)(allLines[i][j]);
				if(j+i==3)	diag2+=(int)(allLines[i][j]);
				if(allLines[i][j] == '.')	notYetFinished=1;
			}
		}

		if( (diag1 == 4*(int)'X' || diag1 == 3*'X'+'T') ||  (diag2 == 4*(int)'X' || diag2 == 3*'X'+'T')    )
		{	output<<"Case #"<<I<<": "<<"X won"<<endl;done=1;continue;}
		if( (diag1 == 4*(int)'O' || diag1 == 3*'O'+'T') ||  (diag2 == 4*(int)'O' || diag2 == 3*'O'+'T'))
		{	output<<"Case #"<<I<<": "<<"O won"<<endl;done=1;continue;}

		for(int i=0;i<4;i++)
		{
			if( (rowSum[i] == 4*(int)'X' || rowSum[i] == 3*'X'+'T') ||  (colSum[i] == 4*(int)'X' || colSum[i] == 3*'X'+'T') )
			{	output<<"Case #"<<I<<": "<<"X won"<<endl;done=1;break;}
			if( (rowSum[i] == 4*(int)'O' || rowSum[i] == 3*'O'+'T') ||  (colSum[i] == 4*(int)'O' || colSum[i] == 3*'O'+'T') )
			{	output<<"Case #"<<I<<": "<<"O won"<<endl;done=1;break;}
		}

		if(done==0 && notYetFinished==1 )
		{
			output<<"Case #"<<I<<": "<<"Game has not completed"<<endl;done=1;
		}

		if(done)	continue;
		
		output<<"Case #"<<I<<": "<<"Draw"<<endl;done=1;

		
	}
	output.close();
	return 0;
}
