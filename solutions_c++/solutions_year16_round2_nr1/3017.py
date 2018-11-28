#include <iostream>
#include<vector>
#include<string.h>
#include<algorithm>
using namespace std;

int cToInt(char c)
{
	return (int)c - 65;
}

int main() 
{
	string s;
	int t, len, count[26], flag, ans=0, temp;
	cin>>t;
	vector<int> vec;

	for(int i=0; i<t; i++)
	{
		flag = 1;
		for(int a=0; a<26; a++)
		{
			count[a] = 0;
		}

		cin>>s;
		len = s.size();
		for(int j=0; j<len; j++)
		{
			count[cToInt(s[j])]++;
		}
/*	
		cout<<"Got the String \n";
		for(int a=0; a<26; a++)
		{
			cout<<(char)(a+65)<<":"<<count[a]<<"\t\t";
		}
		cout<<endl;
*/	
		if(count[cToInt('G')] != 0)
		{
			temp = count[cToInt('G')];
			count[cToInt('E')]-= temp;
			count[cToInt('I')]-= temp;
			count[cToInt('G')]-= temp;
			count[cToInt('H')]-= temp;
			count[cToInt('T')]-= temp;
			while(temp--)
			vec.push_back(8);
/*			
					cout<<"After 8 \n";
					for(int a=0; a<26; a++)
					{
						cout<<(char)(a+65)<<":"<<count[a]<<"\t\t";
					}
					cout<<endl;
*/
		}
		
		if(count[cToInt('U')] != 0)
		{
			temp = count[cToInt('U')];
			count[cToInt('F')]-= temp;
			count[cToInt('O')]-= temp;
			count[cToInt('U')]-= temp;
			count[cToInt('R')]-= temp;
			while(temp--)
			vec.push_back(4);
/*
					cout<<"After 4 \n";
					for(int a=0; a<26; a++)
					{
						cout<<(char)(a+65)<<":"<<count[a]<<"\t\t";
					}
					cout<<endl;
*/

		}

		if(count[cToInt('W')] != 0)
		{
			temp = count[cToInt('W')];
			count[cToInt('T')]-= temp;
			count[cToInt('W')]-= temp;
			count[cToInt('O')]-= temp;
			while(temp--)
			vec.push_back(2);
		}
		
		if(count[cToInt('X')] != 0)
		{
			temp = count[cToInt('X')];
			count[cToInt('S')]-= temp;
			count[cToInt('I')]-= temp;
			count[cToInt('X')]-= temp;
			while(temp--)
			vec.push_back(6);
		}
		
		if(count[cToInt('Z')] != 0)
		{
			temp = count[cToInt('Z')];
			count[cToInt('Z')]-= temp;
			count[cToInt('E')]-= temp;
			count[cToInt('R')]-= temp;
			count[cToInt('O')]-= temp;
			while(temp--)
			vec.push_back(0);
/*			
					cout<<"After 0 \n";
					for(int a=0; a<26; a++)
					{
						cout<<(char)(a+65)<<":"<<count[a]<<"\t\t";
					}
					cout<<endl;
*/			
		}

		if(count[cToInt('O')] != 0 && count[cToInt('N')] != 0 && count[cToInt('E')] != 0)
		{
			temp = min(min(count[cToInt('O')], count[cToInt('N')]), count[cToInt('E')]);
			count[cToInt('O')]-= temp;
			count[cToInt('N')]-= temp;
			count[cToInt('E')]-= temp;
			while(temp--)
			vec.push_back(1);
/*
					cout<<"After 1 \n";
					for(int a=0; a<26; a++)
					{
						cout<<(char)(a+65)<<":"<<count[a]<<"\t\t";
					}
					cout<<endl;
*/			
		}

		if(count[cToInt('T')] != 0 && count[cToInt('H')] != 0 && count[cToInt('R')] != 0 && count[cToInt('E')]/2 != 0)
		{
			temp = min(min(count[cToInt('T')], count[cToInt('H')]), count[cToInt('R')]);
			temp = min(temp, count[cToInt('E')]/2);
			count[cToInt('T')]-= temp;
			count[cToInt('H')]-= temp;
			count[cToInt('R')]-= temp;
			count[cToInt('E')]-= 2*temp;
			while(temp--)
			vec.push_back(3);
			
		}
		
		if(count[cToInt('S')] != 0 && count[cToInt('V')] != 0 && count[cToInt('N')] != 0 && count[cToInt('E')]/2 != 0)
		{
			temp = min(min(count[cToInt('S')], count[cToInt('V')]), count[cToInt('N')]);
			temp = min(temp, count[cToInt('E')]/2);
			count[cToInt('S')]-= temp;
			count[cToInt('V')]-= temp;
			count[cToInt('N')]-= temp;
			count[cToInt('E')]-= 2*temp;
			while(temp--)
			vec.push_back(7);
			
		}
		
		if(count[cToInt('E')] != 0 && count[cToInt('I')] != 0 && count[cToInt('N')]/2 != 0)
		{
			temp = min(min(count[cToInt('E')], count[cToInt('I')]), count[cToInt('N')]/2);
			count[cToInt('E')]-= temp;
			count[cToInt('I')]-= temp;
			count[cToInt('N')]-= 2*temp;
			while(temp--)
			vec.push_back(9);
/*
					cout<<"After 9 \n";
					for(int a=0; a<26; a++)
					{
						cout<<(char)(a+65)<<":"<<count[a]<<"\t\t";
					}
					cout<<endl;
*/			
		}	
		if(count[cToInt('F')] != 0 && count[cToInt('I')] != 0 && count[cToInt('V')] != 0 && count[cToInt('E')] != 0)
		{
			temp = min(min(count[cToInt('F')], count[cToInt('I')]), count[cToInt('V')]);
			temp = min(temp, count[cToInt('E')]);
			count[cToInt('F')]-= temp;
			count[cToInt('I')]-= temp;
			count[cToInt('V')]-= temp;
			count[cToInt('E')]-= temp;			
			while(temp--)
			vec.push_back(5);
/*
					cout<<"After 5 \n";
					for(int a=0; a<26; a++)
					{
						cout<<(char)(a+65)<<":"<<count[a]<<"\t\t";
					}
					cout<<endl;
*/			
		}
		
		
		sort(vec.begin(), vec.end());
		cout<<"Case #"<<i+1<<": ";
		for(int index=0; index<vec.size(); index++)
		{
			cout<<vec[index]<<"";
		}
		cout<<endl;
		vec.clear();
	}
	return 0;
}