// GCJ13.cpp : Defines the entry point for the console application.
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
#include <iomanip>
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
#define VD vector<long double>
#define VLD vector<long long double>
#define VS vector<string>
#define LI list<int>
#define LL list<I>
#define LD list<long double>
#define LLD list<long long double>
#define LS list<string>
#define SI set<int>
#define SL set<I>
#define SD set<long double>
#define SLD set<long long double>
#define SS set<string>
#define MII map<int,int>
#define MIL map<int,I>
#define MID map<int,long double>
#define MIS map<int,string>
#define MLL map<I,I>
#define MLI map<I, int>
#define MLD map<I,long double>
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

/* Tic-Tac-Toe-Tomek */
/*
int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\A-large.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\A-large.out",ios::out);
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
	char b[4][416];
	FRE(e,1,casecnt)
	{
		MMS(b);
		FR(i,0,4) {
			FR(j,0,4) {
				fin>>b[i][j];
			}
		}
		bool xwins[4]={true, true, true, true};
		bool owins[4]={true, true, true, true};
		bool complete=true;
		FR(i,0,4) {
			xwins[0]=xwins[1]=true;
			owins[0]=owins[1]=true;

			if(b[i][i]!='X' && b[i][i]!='T') xwins[2] = false;
			if(b[i][i]!='O' && b[i][i]!='T') owins[2] = false;

			if(b[i][3-i]!='X' && b[i][3-i]!='T') xwins[3] = false;
			if(b[i][3-i]!='O' && b[i][3-i]!='T') owins[3] = false;

			FR(j,0,4) {

				if(b[i][j]!='X' && b[i][j]!='T') xwins[0] = false;
				if(b[i][j]!='O' && b[i][j]!='T') owins[0] = false;

				if(b[j][i]!='X' && b[j][i]!='T') xwins[1] = false;
				if(b[j][i]!='O' && b[j][i]!='T') owins[1] = false;

				if(b[i][j] == '.') complete = false;
			}
			if(xwins[0] || xwins[1] || owins[0] || owins[1]) {
				xwins[2]=xwins[3]=false;
				owins[2]=owins[3]=false;
				break;
			}
		}
		string result;
		if(xwins[0] || xwins[1] || xwins[2] || xwins[3])
			result = "X won";
		else if(owins[0] || owins[1] || owins[2] || owins[3])
			result = "O won";
		else if(!complete) 
			result = "Game has not completed";
		else 
			result = "Draw";
		fout<<"Case #"<<e<<": "<<result;
		cout<<"Case #"<<e<<": "<<result;
		fout<<endl;
		cout<<endl;
	}
	return 0;
}
*/

/* Lawnmower */
/*
int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\B-large.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\B-large.out",ios::out);
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
	FRE(e,1,casecnt)
	{
		vector<pair<int, int> > v[101];
		int allowed[101][2];
		int n, m;
		MMS(allowed);

		fin>>n>>m;
		FR(i,0,n) {
			FR(j,0,m) {
				int x;
				fin>>x;
				v[x].push_back(pair<int,int>(i,j));
			}
		}

		bool possible = true;
		for(int i=100; i>0 && possible; i--) {
			for(int j=0; j<v[i].size() && possible; j++) {
				if(allowed[v[i][j].first][0] <= i || allowed[v[i][j].second][1] <= i) {
					if(allowed[v[i][j].first][0]<i) allowed[v[i][j].first][0] = i;
					if(allowed[v[i][j].second][1]<i) allowed[v[i][j].second][1] = i;
				} else {
					possible = false;
				}
			}
		}
		fout<<"Case #"<<e<<": "<<(possible ? "YES" : "NO");
		cout<<"Case #"<<e<<": "<<(possible ? "YES" : "NO");
		fout<<endl;
		cout<<endl;
	}
	return 0;
}
*/

/* Treasure */
/*
#define KEY_TYPE_MAX 201
#define CHEST_MAX 201

bool possible(vector<int> keyTypeToChest[], vector<int> chestWithKeys[], int chestToKeyType[],  bool chestStatus[], list<int> initKeysTypes, bool typesStatus[], bool finalState[]) {
	bool t[KEY_TYPE_MAX], c[CHEST_MAX];
	memcpy(t, typesStatus, KEY_TYPE_MAX);
	memcpy(c, chestStatus, CHEST_MAX);
	while(!initKeysTypes.empty()) {
		int type = initKeysTypes.front();
		t[type] = true;
		initKeysTypes.pop_front();
		for(int i=0; i<keyTypeToChest[type].size(); i++) {
			int chest = keyTypeToChest[type][i];
			if(!c[chest]) {
				c[chest] = true;
				for(int j=0; j<chestWithKeys[chest].size(); j++) {
					if(!t[chestWithKeys[chest][j]]) {
						t[chestWithKeys[chest][j]] = true;
						initKeysTypes.push_back(chestWithKeys[chest][j]);
					}
				}
			}
		}
	}

	FRE(i,1,KEY_TYPE_MAX) {
		if(finalState[i] && !t[i])
			return false;
	}
	return true;
}

int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\D-large-practice.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\D-large-practice.out",ios::out);
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
	FRE(e,1,casecnt)
	{
		int K, N;
		fin>>K>>N;
		list<int> keyType;
		vector<int> keyTypeToChest[KEY_TYPE_MAX];
		int chestToKeyType[CHEST_MAX];
		vector<int> chestWithKeys[CHEST_MAX];
		bool finalState[KEY_TYPE_MAX];
		int verifyCount[KEY_TYPE_MAX];
		bool chestStatus[CHEST_MAX];
		vector<int> ret;

		MMS(finalState);
		MMS(chestToKeyType);
		MMS(verifyCount);
		MMS(chestStatus);
		FR(i,0,K) {
			int x;
			fin>>x;
			keyType.push_back(x);
			verifyCount[x]++;
		}
		FRE(i,1,N) {
			int Ti, Ki, val;
			fin>>Ti>>Ki;
			chestToKeyType[i]=Ti;
			keyTypeToChest[Ti].push_back(i);
			finalState[Ti] = true;
			FR(j,0,Ki) {
				fin>>val;
				chestWithKeys[i].push_back(val);
				verifyCount[val]++;
			}
		}

		bool typesStatus[KEY_TYPE_MAX];
		MMS(typesStatus);
		// Verify possibility
		bool poss = true;
		FRE(i,1,KEY_TYPE_MAX) {
			if(finalState[i]) {
				if(verifyCount[i] < keyTypeToChest[i].size()) {
					poss = false;
					break;
				}
			}
		}
		if(poss) {
			poss = possible(keyTypeToChest, chestWithKeys, chestToKeyType, chestStatus, keyType, typesStatus, finalState);
		}
		if(!poss) {
			fout<<"Case #"<<e<<": IMPOSSIBLE";
			cout<<"Case #"<<e<<": IMPOSSIBLE";
			fout<<endl;
			cout<<endl;
			continue;
		}

		FRE(i,1,N) {
			FRE(j,1,N) {
				if(!chestStatus[j]) {
					// Use the keyType to open, and add the keys inside it.
					list<int> tKeyType = keyType;
					bool found = false;
					for(list<int>::iterator it = tKeyType.begin(); it != tKeyType.end(); ++it) {
						if((*it) == chestToKeyType[j]) {
							tKeyType.erase(it);
							FR(k,0,chestWithKeys[j].size()) {
								tKeyType.push_back(chestWithKeys[j][k]);
							}
							found = true;
							break;
						}
					}
					if(!found) {
						continue;
					}

					// Reduce the key verifyCount once a keyType is used
					// Once it is 0, its connectedness is not required.
					verifyCount[chestToKeyType[j]]--;
					if(verifyCount[chestToKeyType[j]] == 0) {
						typesStatus[chestToKeyType[j]] = true;
					}
					chestStatus[j] = true;
						
					if(poss = possible(keyTypeToChest, chestWithKeys, chestToKeyType, chestStatus, tKeyType, typesStatus, finalState)) {
						keyType = tKeyType;
					} else {
						verifyCount[chestToKeyType[j]]++;
						typesStatus[chestToKeyType[j]] = false;
						chestStatus[j] = false;
					}
					if(chestStatus[j]) {
						ret.push_back(j);
						break;
					}
				}
			}
		}
		fout<<"Case #"<<e<<": ";
		cout<<"Case #"<<e<<": ";
		FR(i,0,ret.size()) {
			fout<<ret[i]<<" ";
			cout<<ret[i]<<" ";
		}
		fout<<endl;
		cout<<endl;
	}
	return 0;
}
*/

int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\A-large.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\A-large.out",ios::out);
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
	long long res=0;
	FRE(e,1,casecnt)
	{
		long long r,t;
		fin>>r>>t;
		
		long long low=1, high=t;
		while(low<=high) {
			long long mid=(low+high)/2;
			long long val = mid + (2*r-1);
			if(val<=(2*t/mid)) {
				res=mid/2;
				low=mid+1;
			} else {
				high=mid-1;
			}
		}

		fout<<"Case #"<<e<<": "<<res<<endl;
		cout<<"Case #"<<e<<": "<<res<<endl;
	}
}