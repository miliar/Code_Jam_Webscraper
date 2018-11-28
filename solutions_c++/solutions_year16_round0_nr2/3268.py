#include<iostream>
#include<stdafx.h>
#include <iostream>
#include <fstream>
#include<string>
#include <vector>
#include<algorithm>
#define  LL long long
using namespace std;



string num;
LL finalcnt =0;

bool checkAllPstv(string num1)
{
	LL i =0;
	LL cnt =0;
	LL strlength = num1.length();
	while(strlength--)
	{
		if(num[i]=='+')
			cnt++;
		i++;
	}
	if(cnt == num1.length())
		return true;
	return false;
}
 
void startsWithNegative()
{
	LL strlength = num.length();
	LL negativecnt = 0;
	for(LL i =0; i<strlength; i++)
	{
		if(num[i]!='+')
		{
			negativecnt++;
		}
		else{
			break;
		}
	}
	for(LL j =0; j<negativecnt; j++)
	{
		num[j] = '+';
	}


}
void startWithPstv()
{
	LL strlength = num.length();
	LL pstvcnt = 0;
	for(LL i =0; i<strlength; i++)
	{
		if(num[i]!='-')
		{
			pstvcnt++;
		}
		else{
			break;
		}
	}
	for(LL j =0; j<pstvcnt; j++)
	{
		num[j] = '-';
	}
}
void AllNegative()
{
	LL i =0;
	LL cnt =0;
	LL strlength = num.length();
	while(strlength--)
	{
		if(num[i]=='-')
			cnt++;
		i++;
	}
	if(cnt == num.length())
	{
		for(LL j =0; j<num.length(); j++)
		{
			num[j] = '+';
		}
		finalcnt++;
	}
}

int main(){
	
	ifstream fin("input.in");
    ofstream fout("output.out");

	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;

	LL t;
	fin >> t;
	
	
	//while(t--)
	for(LL i = 0; i<t; i++)
	{
		
		fin>>num;
		LL cnt=0;

		/*for(int j =0; j<num.length(); j++)
		{			
			if(checkAllPstv(num))
			{
				fout << "Case #" << (i+1) << ": " << "0" << endl;
			}
			if(num[j]== '-')
			{
				startsWithNegative();

			}
			if(num[j]== '+'){
				startWithPstv();
			}
		}*/
		while(checkAllPstv(num)!=true)
		{
			if(num[0]== '-')
			{
				startsWithNegative();
				finalcnt++;

			}
			if(checkAllPstv(num)== true)
				break;
			if(num[0]== '+'){
				startWithPstv();
				finalcnt++;
				
			}
			if(num[0]=='-')
			{
				AllNegative();
				
			}
		}
	
		fout << "Case #" << (i+1) << ": " << finalcnt << endl;
		finalcnt=0;
		

	}
		//fout << "Case #" << (i+1) << ": " << need << endl;		
	//}
	return 0;
}