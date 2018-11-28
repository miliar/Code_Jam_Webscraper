#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;

long long get(long long i,long long j)
{
	long long si=1, sj=1;
	if(i<0)
	{
		si=-1;
		i*=-1;
	}
    if(j<0)
	{
		sj=-1;
		j*=-1;
	}
	
	if(i>1){
		i -= 'i';
		i++;
	}
	else{
		i--;
	}
	
	if(j>1){
		j -= 'i' ;
		j++;
	}
	else
	{
		j--;
	}

	long long arr[4][4] = 
	{
		{1    ,  'i'   ,   'j'  ,   'k'},
		{'i'  ,  -1    ,   'k'  ,   -1*'j'},
		{'j'  , -1*'k' ,   -1  ,   'i'},
		{'k'  ,  'j'   ,   -1*'i'  ,   -1},
	};
	return arr[i][j]*si*sj;
}
void add(vector<long long>& vec, string str)
{
	for(long long i=0; i<str.size(); i++)
	{
		vec.push_back(str[i]);
	}
}
void print (vector<long long > vec)
{
	for(long long i=0; i<vec.size(); i++)
	{
		cout << vec[i] << "  ";
	}
	cout << endl;
}
bool check(vector<long long>& vec)
{
	if(vec.size() <= 4 && vec[0] == 'i' &&vec[1] == 'j'  &&vec[2] == 'k' )
	{
		if(vec.size() ==4 )
		{
			if( vec[3] == 1)
			{
				return true;
			}
			return false;
		}
		return true;
	}
	return false;
}
int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.out");
	ofstream f("in2.txt");

	long long t, ta;
	fin >> t;
	f << t << endl;
	for(long long c=1; c<=t; c++)
	{
		long long l, x;
		fin >> l >> x;
		f << l << " " << x << endl;
	 	string str, waste;
		fin >> str;
		f << str << endl;
		getline(fin,waste);

		vector< long long > cur;
		long long cw = 'i';
		add(cur, str);
		x--;

		for(long long i=0; i<cur.size(); i++)
		{	
			if(cur.size() <= i+1)
			{
				if(x>0){
					add(cur, str);
					x--;
				}
			}
			
			if(cur[i] == cw)
			{
				cw++;
			}
		 	else if(cur.size() > i+1){

				long long t = get(cur[i], cur[i+1]);
				cur.erase(i+cur.begin());
				cur.erase(i+cur.begin());
				cur.insert(i+cur.begin(), t);
				i--;
			}

		}

		if(check(cur)){
			fout << "Case #" << c << ": Yes" << endl;
		}
		else{
			fout << "Case #" << c << ": No" << endl;
		}
	}
	system("pause");
}
