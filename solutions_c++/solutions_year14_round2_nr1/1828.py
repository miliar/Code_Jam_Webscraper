/* name of code*/
#include<iostream>
#include<cstring>
#include<iomanip>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<fstream>
#include<set>
#include<bitset>

#define lol long long
#define ull unsigned long long int

using namespace std;

#define cin fin
#define cout fout

int main()
{
	//ios_base::sync_with_stdio(false);
	int test_case,t=1;
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt1.in");
	fout.open("a.txt");
	cin>>test_case;
	while(test_case--)
	{
		int n;
		cin>>n;
		char str1[200],str2[200];
		cin>>str1>>str2;
		int i=0,j=0,cost=0;
		int tag=0;
		int l1=strlen(str1);
		int l2=strlen(str2);
		while(i<l1 && j<l2)
		{
			int count1=0,count2=0;
			char c=str1[i];
			while(str1[i]==c && i<l1) count1++,i++;
			char d=str2[j];
			if(c != d) 
			{
				tag=1;
				break;
			}
			else
			{
				while(str2[j]==d && j<l2) count2++,j++;
			}
			cost = cost + abs(count2-count1);
		}
		if((i==l1 && j!=l2) || (i!=l1 && j==l2)) tag=1;
		cout<<"Case #"<<t<<": ";
		if(tag==1) cout<<"Fegla Won\n";
		else cout<<cost<<"\n";
		t++;
	}
	return 0;
}
