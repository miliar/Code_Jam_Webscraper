#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <gmp.h>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

int countChars(int x)
{
	int count = 0;
	while( x >= 1 )
	{
		x = x/10;
		count++;
	}
	return count;
}

bool isPalindrome(int x)
{
	vector<int> characters;
	int count = 0;
	int a;
	while(x >= 1)
	{
		a = x%10;
		x = x/10;
		characters.push_back(a);
		count++;
	}
		
	for(int i = 0; i<(count/2); i++)
	{
		if(characters[i] != characters[count-1-i])
		{
			return false;
		}
	}
	return true;
}

int tophalf(int x)
{
	vector<int> characters;
	int count = 0;
	int num = 0;
	int a;
	while(x >= 1)
	{
		a = x%10;
		x = x/10;
		characters.push_back(a);
		count++;
	}

	if(count%2 == 0)
	{
		num = count/2;
	}
	else
	{
		num = count/2 + 1;
	}

	int output = 0;
	for(int i = 0; i < num; i++)
	{
		output = output*10;
		output = output + characters[count - 1 - i];
	}
	return output;
}

int makePalindrome(int x, int y)
{
	vector<int> characters;
	int count = 0;
	int num = 0;
	int a,b;
	b = x;
	while(b >= 1)
	{
		a = b%10;
		b = b/10;
		characters.push_back(a);
		count++;
	}
	int output = x;
	for(int i = y; i < count; i++)
	{
		output = output*10;
		output = output + characters[i];
	}
	return output;	
}

void eval(){
	int A, B;
	cin>>A;
	cin>>B;

	int asr = (int)ceil(sqrt(A));
	int bsr = (int)floor(sqrt(B));
	
	int top1 = tophalf(asr);
	int top1O = countChars(asr)%2;
	int top2 = tophalf(bsr);
	int top2O = countChars(bsr)%2;
	
	int full1 = makePalindrome(top1, top1O);
	int full2 = makePalindrome(top2, top2O);
	
	int pPalindrome, sqPalindrome;
	int count = 0;
	//cout<<endl;
	//cout<<A<<" "<<B<<" ";
	for(int i = (top1/10); i<=(top2*10); i++)
	{
		for(int j = 0; j<2; j++)
		{
			pPalindrome = makePalindrome(i,j);
			//cout<<pPalindrome<<endl;

			if(pPalindrome<asr || pPalindrome >bsr)
			{
				continue;
			}
			sqPalindrome = pPalindrome*pPalindrome;
			if(isPalindrome(sqPalindrome))
			{
				count++;
				//cout<<sqPalindrome<<" ";
			}
		}
	}
	
	//cout<<endl;	
	//cout<<A<<": "<<asr<<" "<<top1<<" "<<top1O<<" "<<full1<<endl;
	//cout<<B<<": "<<bsr<<" "<<top2<<" "<<top2O<<" "<<full2<<endl;
	cout<<count<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}