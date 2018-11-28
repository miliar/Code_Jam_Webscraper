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
	fin.open("B-small-attempt0.in");
	fout.open("b.txt");
	cin>>test_case;
	while(test_case--)
	{
		lol n,m,k,count=0;;
		cin>>n>>m>>k;
		for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
		{
			if((i&j) < k) count++;
		}
		cout<<"Case #"<<t<<": "<<count<<"\n";
		t++;
	}
	return 0;
}
