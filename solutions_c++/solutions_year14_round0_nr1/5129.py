#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <sstream>
#include <fstream>//for writing in files
#include <cctype>
#include <stdlib.h>

using namespace std;


string NumberToString (int Number)
{
	stringstream ss;
	ss << Number;
	return ss.str();
}
int StringToNumber (string Text)
{                              
	stringstream ss(Text);
	int result;
	return ss >> result ? result : 0;
}
bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}
bool isPalindrom(unsigned long long n)
{
	string number=NumberToString(n);
	int lenght=number.size();
	bool check=true;
	for(int i=0;i<lenght;i++)
	{
		if(number[i]==number[lenght-i-1] && check==true)
		{
			check=true;
		}
		else
		{
			check=false;
		}
	}
	return check;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin); // For reading input
    freopen("solution.out","w",stdout);
	int n;
	int ans,t;
	int chk=0;
	int cnt=0;int value=0;;
	vector<int> cards,answer,prob1,prob2;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		value=0;cnt=0;
		prob1.clear();prob2.clear();cards.clear();answer.clear();
		for(int r=0;r<2;r++)
		{
			cin>>ans;
			answer.push_back(ans);
			for(int c=0;c<16;c++)
			{
				cin>>t;
				cards.push_back(t);
			}
		}
		for(int z=(answer[0]-1)*4;z<(answer[0]-1)*(4)+4;z++)
		{
			
			prob1.push_back(cards[z]);
		}
		
		for(int x=16+((answer[1]-1)*4);x<20+((answer[1]-1)*4);x++)
		{
			
			prob2.push_back(cards[x]);
		}
		
		for(int z=0;z<prob1.size();z++)
		{
			for(int w=0;w<prob2.size();w++)
			{
				if(prob1[z]==prob2[w])
				{
					chk=1;
					cnt++;
					value=prob1[z];
				}
			}
		}
		if(cnt==1 && value!=0){cout<<"Case #"<<i+1<<": "<<value<<endl;}
		if(cnt>1 && value!=0){cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;}
		if(cnt==0){cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;}
	}
	
	return 0;
}
