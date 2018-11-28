#include <cstdio>
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;

bool flag=false;
int t, n;
string str1, str2;

int solution()
{
	int p1=0, p2=0, sol=0;
	if(str1[p1]!=str2[p2]) return -1;

	while(1)
	{
		if(p1==str1.length() && p2==str2.length()) break;

		if(str1[p1]==str2[p2]) p1++, p2++;
		else
		{
			if(str1[p1]==str1[p1-1]) p1++, sol++;
			else if(str2[p2]==str2[p2-1]) p2++, sol++;
			else return -1;
		}
	}

	return sol;
}

int main(void)
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif

	cin>>t;
	for(int pr=1 ; pr<=t ; pr++)
	{
		cin>>n;
		cin>>str1>>str2;
		int sol=solution();
		cout<<"Case #"<<pr<<": ";
		if(sol==-1) cout<<"Fegla Won"<<endl;
		else cout<<sol<<endl;
	}
}