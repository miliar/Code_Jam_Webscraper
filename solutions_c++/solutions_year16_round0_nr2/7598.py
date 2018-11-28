#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {

int t,g=1;
cin >> t;
while(t--)
{
int result=0;
string s;
cin >> s;

string t;
t[0]=s[0];
int k = 1;
    
for(int i=1;i<s.length();i++)
	if(s[i-1]!=s[i])
	{
		t[k]=s[i];
		k++;
	}

if(k%2==0)
{
	if(t[0]=='+')
		result = k;
	else 
		result = k-1;
}
else
{
	if(t[0]=='+')
		result = k-1;
	else 
		result = k;
}


cout << "Case #"<<g++<<": "<<result<<endl;
}
    return 0;
}