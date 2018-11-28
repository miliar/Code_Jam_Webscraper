// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>
#include<utility>
#include<functional>
#include <deque>
#include <numeric>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <assert.h>
#include<cmath>
#include<math.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>



using namespace std;
vector<unsigned long long>palindrome;
string s1;
string s2;
int l;

bool check_palindrome(unsigned long long num)
{

	s2="";
	stringstream ss;//create a stringstream
	ss << num;
	s1=ss.str();
	l=s1.length();
	for(int i=l-1;i>=0;i--)
		s2+=s1[i];

	if(s1 == s2)
		return true;

	
	return false;

}

void UpdatePalindromeVector()
{
	unsigned long long temp;
	for(unsigned long long i=1;i<=34;i++)
		if(true == check_palindrome(i))
		{
			temp = i*i;
			if(true == check_palindrome(temp))
				palindrome.push_back(temp);
		}

		
		
}



int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.txt","w",stdout);
	int T,sz,start,end;
	cin>>T;

	int n = 0;
	UpdatePalindromeVector();
	sz = palindrome.size();
	int counter;


	while(T--)
	{


		
		cin>>start>>end;
		
		counter = 0;
		for(int i=0;i<sz;i++)
			if(palindrome[i]>=start && palindrome[i]<=end)
				counter++;

		cout<<"Case #"<<++n<<": ";
		cout<<counter<<endl;

	}


	return 0;
}


