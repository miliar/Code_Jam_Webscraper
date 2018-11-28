#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		string str;
		cin >> str;
		string now="";
		int len=str.size();
		string s1,s2;
		for(int i=0;i<len;i++)
		{
			s1=now+str[i];
			s2=str[i]+now;
			now=max(s1,s2);
		}
		printf("Case #%d: ",cc);
		cout << now << endl;
	}
    return 0;
}
/*
7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE

 */
