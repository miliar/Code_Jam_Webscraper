#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>
#include <cstdlib>
#include <string>

using namespace std;

int main()
{
	int cases,limit[2];
	string line,temp;

	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
	cin>>cases;
	getline(cin,line);
	for (int i=0; i < cases ; i++)
	{
		int count =0;
		int j=0;
		getline(cin,line);
		istringstream strstr(line);
		while(strstr >> temp)
		{
			limit[j]=atoi(temp.c_str());
			j++;
		}

		int start=limit[0];
		int end=limit[1];
		while (start<=end)
		{
			double root;
			string input=to_string(start);
			if (input == string(input.rbegin(), input.rend())) 
			{
				root=sqrt(start);
				if (floor(root)==ceil(root))
				{
					string inp=to_string(int(root));
					if (inp ==string(inp.rbegin(),inp.rend() ))
					{
						count++;
					}
				}
			}
			start++;
		}
		
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;

}