#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;
int A[130];
int T;
vector<int> v;
int slen;
void solve()
{
		if(A['Z']){
			A['E']-=A['Z'];
			A['R']-=A['Z'];
			A['O']-=A['Z'];
			while(A['Z']--)
				v.push_back(0);
		}
		if(A['X']){
			A['S']-=A['X'];
			A['I']-=A['X'];
			while(A['X']--)
				v.push_back(6);
		}
		if(A['W']){
			A['T']-=A['W'];
			A['O']-=A['W'];
			while(A['W']--)
				v.push_back(2);
		}
		if(A['U']){
			A['F']-=A['U'];
			A['O']-=A['U'];
			A['R']-=A['U'];
			while(A['U']--)
				v.push_back(4);
		}
		if(A['G']){
			A['E']-=A['G'];
			A['I']-=A['G'];
			A['H']-=A['G'];
			A['T']-=A['G'];
			while(A['G']--)
				v.push_back(8);
		}
		if(A['S']){
			A['E']-=A['S'];
			A['V']-=A['S'];
			A['E']-=A['S'];
			A['N']-=A['S'];
			while(A['S']--)
				v.push_back(7);
		}
		if(A['F']){
			A['I']-=A['F'];
			A['V']-=A['F'];
			A['E']-=A['F'];
			while(A['F']--)
				v.push_back(5);
		}
		if(A['O']){
			A['N']-=A['O'];
			A['E']-=A['O'];
			while(A['O']--)
				v.push_back(1);
		}
		if(A['T']){
			A['H']-=A['T'];
			A['R']-=A['T'];
			A['E']-=A['T'];
			A['E']-=A['T'];
			while(A['T']--)
				v.push_back(3);
		}
		if(A['E']){
			A['N']-=A['E'];
			A['I']-=A['E'];
			A['N']-=A['E'];
			while(A['E']--)
				v.push_back(9);
		}		
	sort(v.begin(), v.end());
	for (int i = 0; i < v.size(); ++i)
	{
		cout<<v[i];
	}
	cout<<endl;
}
int main()
{
	string str;
	ifstream in("A-large.in");
	in>>T;
	for (int i = 0; i < T; ++i)
	{
		in>>str;
		slen = str.length();
		for(int j=0;j<slen;j++)
			A[str[j]]++;
		cout<<"Case #"<<i+1<<": ";
		solve();
		for(int j = 'A'; j <= 'Z'; ++j)
			A[j]=0;
		v.clear();
	}
	return 0;
}