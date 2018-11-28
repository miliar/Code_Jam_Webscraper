
#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <iomanip>
#include <locale>
#include <sstream>
#include <bitset>

using namespace std;

int checkString(string str)
{
	for(int i=0;i<str.size();i++)
	{
		if(str[i] == '-')
			return 0;
	}
	return 1;
}

int main()
{
	int t =0;
	cin>>t;
	vector<string> input;
	string str;
	for(int i=0;i<t;i++)
	{
		cin>>str;
		input.push_back(str);
	}
	for(int i=0;i<t;i++)
	{
		int answer = 0;
		
			char currentChar;
			
			while(!checkString(input[i]))
			{
				//answer++;
				//cout<<input[i]<<endl;
				int diffStrLength = 0;
				int index =0;
				currentChar = input[i][0];
				while(currentChar== input[i][index] && input[i].size()>index)
				{
					diffStrLength++;
					index++;
				}
				//cout<<"diff length is: "<<diffStrLength<<endl;
				/*if(diffStrLength == input[i].size())
				{
					cout<<"string is "<<input[i]<<endl;
					cout<<"answer is "<<answer<<endl;
					break;
				}
				else
				{*/
					if(currentChar == '+')
					{
						answer++;
						input[i].replace(0,diffStrLength,diffStrLength,'-');
						//cout<<"after conversion str is "<<input[i]<<endl;
					}
					else
					{
						answer++;
						input[i].replace(0,diffStrLength,diffStrLength,'+');
						//cout<<"after conversion str is "<<input[i]<<endl;
					}
				//}

			}
		if(checkString(input[i]))
			{
				cout<<"Case #"<<i+1;
				cout<< ": "<<answer<<endl;
			}
	}
	
}
