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

#define cin fin
#define cout fout

using namespace std;


int main()
{
	//ios_base::sync_with_stdio(false);
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("4.txt");
	int t=1;
	int test_case;
	cin>>test_case;
	while(test_case--)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double curr,next;
		int i=0,j=0;
		double temp;
		curr = x/2;
		next = c/2 + x/(2+f);
		i++;
		while(next<curr)
		{
			curr = next;
			next = next - x/(2+f*i);
			next = next + c/(2+f*i) + x/(2+f*(++i));
		}
		cout<<"Case #"<<t<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<curr<<"\n";
		t++;
	}
	return 0;
}
