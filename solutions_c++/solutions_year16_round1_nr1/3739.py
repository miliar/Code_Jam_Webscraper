#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	 int T;
	ifstream infile;
	infile.open("input.txt");
	ofstream outfile;
	outfile.open("output.txt");
	string S,ans_S;
	infile>>T;
	for( int i=1;i<=T;i++) 
	{
		infile>>S;
		int len= S.length();
		ans_S = S[0];
		for( int j=1;j<len;j++)
	{
		if( (S[j]-'A')>=(ans_S[0]-'A')) 
		{
		ans_S = S[j] + ans_S;
		}
		else ans_S = ans_S + S[j];
	}
	outfile<<"Case #"<<i<<": "<<ans_S<<endl;
	}
}
		
	
