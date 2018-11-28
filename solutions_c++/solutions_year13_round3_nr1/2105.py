#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

#include <vector>
#include <set>
#include <map>

#include <math.h>
#include <stdlib.h>

using namespace std;

void LevenshteinDistance()
{

}

int main()
{
	fstream cin("A.in",ios::in);
	fstream cout("A.out",ios::out);
	int tc;
	int caseNum = 0;
	cin>>tc;

	while(caseNum<tc)
	{
		caseNum++;

		string str;
		int n;
		cin>>str>>n;

		int count;
		string temp="";
		char ch;
		int strcount = 0;
		for(int i=0; i<str.length(); i++)
		{
			count = 0;
			for(int j=i ; j <str.length(); j++)
			{
				ch = str[j];
				if(ch!='a' && ch!='e' && ch!='u' && ch!='i'&& ch!='o')
				{
					count++;
				}
				else
				{
					count=0;
				}
				if(count >= n)
				{
					strcount+=str.length()-j;
					break;
				}

			}
		}


		cout<<"Case #"<<caseNum<<": "<< strcount<<endl;
	}

	return 0;
}
