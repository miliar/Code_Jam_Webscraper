// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include <string>
#include <vector>
#include <cstring>
#include <fstream>
using namespace std;

int checkstring(string s1);

int main()
{
	string str1[450];
	ifstream file;
    file.open ("A-small-attempt0.in");
    string word;
    char x ;
    word.clear();

    int i1=0;
    while(file >> word)
    {
            str1[i1]=word;
            i1++;
      
    }
    
   
	int t,s_max;
	string str;
	ofstream ofile;
	ofile.open("Output file.txt");

	
	t=stoi(str1[0],nullptr,10);
	int answer;
	int x1=1,y=2;
	
	for(int i=1;i<=t;i++)
	{
		
		str=str1[y];
		y=y+2;
		ofile << "Case #"<< i << ": ";
		cout << "Case #"<< i << ": ";
		answer = checkstring(str);
		ofile << answer << endl;
		cout << answer << endl;
	}	
	cin.get();
	ofile.close();
	return 0;
}

int checkstring(string s1)
{
	int temp=0;
	int c=0;
	for(int i=0;i <=s1.size(); i++)
	{
		if(s1.at(i) != '0') break;
		c++;
	}
	
	int i_hex = stoi (s1,nullptr,10);
	
	vector<int> vec1;
	vec1.reserve(s1.size());
	
	while(i_hex>0)
	{
		vec1.push_back(i_hex%10);
		i_hex/=10;
	}
	for(int i=0;i<c;i++)
	{
		vec1.push_back(0);
	}
	reverse(vec1.begin(), vec1.end());
	
	
	int i=0;
    int total=0;
	total=total+vec1.at(0);
    
	int p=0;

    
	for(i=1;i !=vec1.size();i++)
    {
        if(vec1.at(i)==0) continue;
    
        if(total >= i)
        {
			total = total + vec1.at(i);
    
        }
        else
        {
            p=p+(i-total);
            total = total + p;
			total = total + vec1.at(i);
    
        }
    }
	
	return p;
}