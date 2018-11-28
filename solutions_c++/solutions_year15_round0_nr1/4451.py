//============================================================================
// Name        : first.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream ifs;
	ifs.open("A-large.in");
	ofstream ofs;
	ofs.open("output.out");
	if(ifs.is_open())
	{
	int x;
	ifs >> x;

	for(int y=0;y<x;y++)
	{
		if(ifs.good())
		{
		int value;
		string aud;
		int z=y;
		ifs>>value>>aud;
		char *narr = const_cast<char*>(aud.c_str());
		int count=0;
		int fr=0;
		int sindex=0;
		bool result=true;
		int occur = 0;
		int start = 0;
		int end = 0;
		int nid=0;

		while ((end = aud.find('0', start)) != string::npos)
		{
			sindex=end;
		    ++occur;
		    nid=sindex+1;
		    for(int j=start;j<sindex;j++)
		    {
		    	count+=(narr[j]-'0');
		    }
		    if(start==sindex)
		    {
		    	count+=(narr[start]-'0');
		    }
		    if(count>=sindex)
		    		{
		    			if(count>=value)
		    			{
		    				ofs <<"Case #"<<z+1<<": "<<fr <<endl;
		    				result=false;
		    				break;
		    			}
		    			else if(count >= nid)
		    			{

		    			}
		    			else{
		    				fr++;
		    				count++;
		    			}
		    		}
		    start =end + 1 ;
		}
		if(occur==0)
		{
			ofs <<"Case #"<<z+1<<": "<<fr <<endl;
		}
		if(result&&occur!=0)
		{

			ofs <<"Case #"<<z+1<<": "<<fr <<endl;
		}
		}
	}
	}
	else
		cout<<"error";
	return 0;
}
