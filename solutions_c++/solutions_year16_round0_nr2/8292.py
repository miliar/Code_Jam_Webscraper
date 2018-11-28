#include<fstream>
#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<string>
#include<string.h>
using namespace std;

string s;

int cnt;
int change()
{
	cnt = 0;
	char l = s[0];
	for(int i=1;i<(int)s.length();i++){
		char r = s[i];
		if(l == r)continue;

		bool ok = true;
		for(int j=0;j<i;j++){
			s[j] = r;
			l = r;
			ok = false;
		}
		if(!ok) cnt++;
	}
	
	return s[0] == '-' ? cnt+1 : cnt;
}
int main()
{
	int test;
	cin >> test;

	ofstream fout;
	fout.open("info.txt");
	for(int t=0;t<test;t++){
		cin >> s;

		fout << "Case #" << t+1 <<": "<<change() << endl;
	}
}