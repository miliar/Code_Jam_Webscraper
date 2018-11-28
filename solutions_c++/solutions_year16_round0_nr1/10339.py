#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <string>
#include <fstream>
#include <istream>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <vector>

using namespace std;


int main(int argc,char* argv[])
{
	ifstream infile;
        infile.open(argv[1]);
	string cases;
	getline(infile,cases);
	int count = atoi(cases.c_str());

	for(int i=0;i<count;i++)
	{
	    	cout<<"Case #"<<i+1<<": ";
		string line;
		char *ptr;
		getline(infile,line);
 		unsigned long int name = strtoul(line.c_str(), &ptr, 10);
		if(name==0)
		{
		    cout<<"INSOMNIA"<<endl;
		    continue;
		}
		else
		{
		    	set<char> lookup;
			int count = 1;
			unsigned long int current;
			while(lookup.size()!=10)
			{
			    current  = name*count;
			    string temp = to_string(current);
			    for(int i=0;i<temp.length();i++)
			    {
				lookup.insert(temp[i]);
			    }
			    count++;
			}
			cout<<current<<endl;
		}
	}
}
