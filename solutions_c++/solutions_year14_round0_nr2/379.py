// GCJ14.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

#define SWAP(a,b,t) (t)=(a);(a)=(b);(b)=(t);
#define MAX(a,b)	((a)>(b))?(a):(b)
#define MIN(a,b)	((a)<(b))?(a):(b)
#define FR(i,a,b)	for(int ( i)=(a); ( i)<(b); ++( i))
#define FRE(i,a,b)	for(int ( i)=(a); ( i)<=(b); ++( i))
#define FRD(i,a,b)	for(( i)=(a); ( i)<(b); ++( i))
#define FRI(i,a)	for(( i)=(a).begin(); ( i)!=(a).end(); ++( i))
#define SWAP(a,b,t) (t)=(a);(a)=(b);(b)=(t);

#define I __int64
#define VI vector<int>
#define VL vector<I>
#define VD vector<double>
#define VLD vector<long double>
#define VS vector<string>
#define LI list<int>
#define LL list<I>
#define LD list<double>
#define LLD list<long double>
#define LS list<string>
#define SI set<int>
#define SL set<I>
#define SD set<double>
#define SLD set<long double>
#define SS set<string>
#define MII map<int,int>
#define MIL map<int,I>
#define MID map<int,double>
#define MIS map<int,string>
#define MLL map<I,I>
#define MLI map<I, int>
#define MLD map<I,double>
#define IT iterator

#define MMS(a) memset(a,0,sizeof(a))

fstream fin, fout;

void parseInt(VI &v)
{
	char s[500];
	fin.getline(s,500);
	memset(s,0,sizeof(char)*500);
	fin.getline(s,500);
	string str(s);
	for(int i=0; i != string::npos;)
	{
		string sub;
		int pos = str.find_first_of(' ',i);
		if(pos!=string::npos)
		{
			sub = str.substr(i, pos-i);
			i = pos+1;
			int val;
			sscanf(sub.c_str(),"%d ",&val);
			v.push_back(val);
		}
		else
		{
			sub = str.substr(i, str.length()-i);
			i = string::npos;
			int val;
			sscanf(sub.c_str(),"%d ",&val);
			v.push_back(val);
		}
	}
}
void parseString(VS &v,string str)
{
	for(int i=0; i != string::npos;)
	{
		string sub;
		int pos = str.find_first_of('/',i);
		if(pos!=string::npos)
		{
			sub = str.substr(i, pos-i);
			i = pos+1;
			v.push_back(sub);
		}
		else
		{
			sub = str.substr(i, str.length()-i);
			i = string::npos;
			v.push_back(sub);
		}
	}
}

I gcd(I a, I b)
{
	if(a<2 || b<2)
		return 1;
	if(a>b)
	{
		I t=a;
		a=b;
		b=t;
	}
	while(b%a)
	{
		I t=a;
		a=b%a;
		b=t;
	}
	return a;
}

class Counting
{
	I arr[67][67];
public:
	Counting()
	{
		memset(arr,0,sizeof(I)*67*67);
		FR(i,0,67)
		{
			arr[i][0]=1;
			arr[i][i]=1;
		}
		FRE(i,1,66)
			FRE(j,1,i-1)
				arr[i][j] = arr[i-1][j]+arr[i-1][j-1];
	}
	I ncr(int n, int r)
	{
		return arr[n][r];
	}
};
/*
int _tmain(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("F:\\Preparation\\GCJ\\A-small-attempt0.in",ios::in);
	fout.open("F:\\Preparation\\GCJ\\A-small-attempt0.out",ios::out);
	if(!fin.good())
	{
		cout<<"Input file not opened"<<endl;
		exit(-1);
	}
	if(!fout.good())
	{
		cout<<"Output file not opened"<<endl;
		exit(-1);
	}

	fin>>casecnt;
	FRE(e,1,casecnt) {
		int n,num;
		set<int> s,r;
		fin>>n;
		FRE(i,1,4) {
			FRE(j,1,4) {
				fin>>num;
				if (i==n) {
					s.insert(num);
				}
			}
		}
		fin>>n;
		FRE(i,1,4) {
			FRE(j,1,4) {
				fin>>num;
				if (i==n && s.find(num) != s.end()) {
					r.insert(num);
				}
			}
		}
		fout<<"Case #"<<e<<": ";
		cout<<"Case #"<<e<<": ";
		if (r.size() == 1) {
			fout<<*(r.begin())<<endl;
			cout<<*(r.begin())<<endl;
		} else if (r.size() > 1) {
			fout<<"Bad magician!"<<endl;
			cout<<"Bad magician!"<<endl;
		} else {
			fout<<"Volunteer cheated!"<<endl;
			cout<<"Volunteer cheated!"<<endl;
		}
	}
	
	return 0;
}
*/

int _tmain(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("F:\\Preparation\\GCJ\\B-large.in",ios::in);
	fout.open("F:\\Preparation\\GCJ\\B-large.out",ios::out);
	if(!fin.good())
	{
		cout<<"Input file not opened"<<endl;
		exit(-1);
	}
	if(!fout.good())
	{
		cout<<"Output file not opened"<<endl;
		exit(-1);
	}

	fin>>casecnt;
	FRE(e,1,casecnt) {
		long double C,F,X;
		fin>>C>>F>>X;
		long double mn=50001,res=50001,r=2.0,prevTime=0.0;
		for (int i=0;;i++) {
			long double res = prevTime+X/r;
			prevTime = prevTime + C/r;
			r = r+F;
			if (res > mn)
				break;
			mn = res;
		}
		fout.precision(15);
		cout.precision(15);
		fout<<"Case #"<<e<<": "<<mn<<endl;
		cout<<"Case #"<<e<<": "<<mn<<endl;
	}
	
	return 0;
}

