#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <stdlib.h>
using namespace std;
int main()
{
	char input[] ="A-large.in";
	char output[]="A-large-output.in";
	int T,n;
	string s;
	ifstream infile;
    ofstream outfile;
    infile.open(input, ios::in);
    infile>>T;
    int S=T;
    outfile.open(output, ios::out);
    while(T--)
    {   int c;
    	infile>>n>>s;
    	c=int(s[0])-48;
    	int sum=c;
    	int ans=0;
    	for(int i=1;i<=n;i++)
    	{
    		if(sum<i)
    		{   ans+=i-sum;
    			sum += (i-sum); 
    		}
    		c=s[i]-48;
    		sum+=(c);
    	}
    	outfile<<"Case #"<<S-T<<": "<<ans<<endl;
    }
    infile.close();
    outfile.close();
}