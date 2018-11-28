#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("output.txt");
	int t;
	input>>t;
	for(int i=0;i<t;++i)
	{
	    string s;
        input>>s;
        int length,steps=0;
        length=s.size();
        int j=0;
        if(s[j]=='-')
        {
            steps++;
            while(s[j]=='-')
                ++j;
        }
        while(j<length-1)
        {
            if(s[j]=='+' && s[j+1]=='-')
                steps+=2;
            ++j;
        }

        output<<"Case #"<<(i+1)<<": "<<steps<<endl;

	}
    return 0;
}

