#include<stdio.h>
#include <iostream> 
#include <fstream>
#include <stdlib.h>
using namespace std;

main()
{
	ifstream in ("input.in");         // The file we want to read in.
  	ofstream out("output.out");        // The file we want to output to.
  	if (!in.is_open() || in.eof())               // Error checking just slows us down.
	{
	    cerr << "ERROR: invalid input file" << endl;
	    return (-1);
	}
	if(!out.is_open())                            // So for code jam you shouldn't bother with these!
	{
	    cerr << "ERROR: couldn't create ouput file" << endl;
	    return (-1);
	}
	string line; 
	getline(in, line, '\n');            // |   then need to read in each line, and then have the great
  
	int test = atoi(line.c_str());
	int j;
	//scanf("%d", &test);
	for(j=1;j<=test;j++)
	{
		int smax, i;
		if(in.eof())  { return (-1); } 
		
		//scanf("%d", &smax);
		in>>smax;
		char s_arr[smax+1];
		//scanf("%s", s_arr);
		in>>s_arr;
		
		int arr[smax+1];
		
		for(i=0;i<smax+1;i++)
		{
			arr[i] = s_arr[i] - '0';
			//printf("%d*\n", arr[i]);
		}
		
		int ans=0;
		int need=0;
		int avail=0;
		
		if(arr[0]  == 0 && smax>=1)
		{
			if(arr[1] > 0)
			{
				need=1;
				avail=1;
			}
		}
		else if(arr[0]  == 0 && smax==0)
		{
			need = 0;
		}
		else
		{
			avail = arr[0];
		}
		for(i=1;i<smax+1;i++)
		{
			if(arr[i]!=0)
			{
				if(avail>=i)
				{
					avail+=arr[i];
				}
				else
				{
					need+=(i-avail);
					avail+=(arr[i]+need);
				}
			}
		}
		
		//printf("%d\n", need);
		out << "Case #" << j << ": " << need << endl;
		
	}
}
