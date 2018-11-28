#include <bits/stdc++.h>
using namespace std;
int main() 
{
	ifstream input;
    ofstream output;
    input.open("D-small-attempt0.in");
    output.open("output.txt");
	int t,j=1;
	input>>t;
	while(t--)
	{
		int i,k,c,s;
		input>>k>>c>>s;
		output<<"Case #"<<j<<":";
		j++;
		for(i=1;i<=k;++i)
		output<<" "<<i;
		output<<endl;
	}
	output.close();
	input.close();
	//sakshamsinghnsit
	return 0;
}
