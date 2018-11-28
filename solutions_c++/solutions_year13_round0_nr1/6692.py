#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

int main()
{
ifstream in("in.txt");	
ofstream out("out.txt");	
int T,i=1;
in>>T;
while(i<=T)
{
	string s="";vector<string> v;
	string s1;
	in.ignore();
	for(int p=0;p<4;p++)
	{
		getline(in,s1,'\n');
		v.push_back(s1);
	}
	for(int p=0;p<4;p++)
	{
		for(int q=0;q<4;q++)
		{
			s+=v[q][p];
		}
		v.push_back(s);
		s="";
	}
	for(int p=0;p<4;p++)
	s+=v[p][p];
	v.push_back(s);
	s="";
	for(int p=0;p<4;p++)
	s+=v[p][3-p];
	v.push_back(s);
	s="";
	int pp=0;int r=2;set<char> st;
	for(int p=0;p<v.size();p++)
	{
	  	for(int j=0;j<4;j++)
	  	  {
			if(v[p][j]=='T')continue;
			if(v[p][j]=='.')pp=1;
			st.insert(v[p][j]);  
	      }
		if(st.size()==1){
							if(*st.begin()=='O'){r=0;break;}
							else if(*st.begin()=='X'){r=1;break;}
							else st.erase(st.begin(),st.end());						
						}
        else st.erase(st.begin(),st.end());						
	}
	
	out<<"Case #"<<i<<": ";
	if(r==0)out<<"O won\n";
	else if(r==1)out<<"X won\n";
	else if(pp==0)out<<"Draw\n";
	else if(pp==1)out<<"Game has not completed\n";
	i++;
}
return 0;
}
