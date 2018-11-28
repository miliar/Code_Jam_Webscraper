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
#include <cassert>
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
*/

/*
#define MAX 10000001
long long v[10000001];
int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\B-small-attempt0.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\B-small-attempt0.in.out",ios::out);
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
		long long E,R,N;
		fin>>E>>R>>N;
		MMS(v);
		FR(i,0,N)
			fin>>v[i];
		if(R>E) {
			cout<<E<<":"<<R<<endl;
			FR(i,0,N)
			  cout<<v[i]<<" ";
		}
		long long cur=E;
		long long res=0;
		FR(i,0,N) {
			long long t=cur;
			long long toconsume = cur;
			FR(j,i,N) {
				if(v[j]>v[i]) {
					toconsume = t-E;
					if(toconsume > cur)
						toconsume = cur;
					else if(toconsume<0)
						toconsume=0;
					break;
				}
				t += R;
			}

			res += toconsume*v[i];
			cur = cur - toconsume+R;
			if(cur>E) cur = E;
		}
		
		fout<<"Case #"<<e<<": "<<res<<endl;
		cout<<"Case #"<<e<<": "<<res<<endl;
	}
}
*/
/*
vector<string> generateSets(char a, char b, int N) 
{
	string s(N, a);
	vector<string> res;
	res.push_back(s);
	while(1) {
		int i;
		for(i=N-1; i>=0 && s[i]==b; i--);
		if(i == -1) break;
		s[i]++;
		for(int j=i+1; j<N; j++) s[j]=s[i];
		res.push_back(s);
	}
	return res;
}
int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\C-small-practice-2.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\C-small-practice-2.out",ios::out);
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
	
	int R, N, M, K;
	FRE(e,1,casecnt)
	{
		fout<<"Case #"<<e<<": "<<endl;
		cout<<"Case #"<<e<<": "<<endl;

		fin>>R>>N>>M>>K;
		vector<string> sets = generateSets('2', M+'0', N);

		map<long long, map<int, long long> > m;
		FR(k,0,sets.size()) {
			FR(i,0,(1<<N)) {
				long long prod=1;
				FR(j,0,N) {
					if((1<<j)&i) {
						prod *= sets[k][j]-'0';
					}
				}
				m[prod][k]++;
			}
			cout<<k<<endl;
		}
		
		int cnt=0;
		FR(i,0,R) {
			set<int> res;
			set<long long> prodset;
			FR(j,0,K) {
				long long prod;
				fin>>prod;
				prodset.insert(prod);
				if(j==0) {
					for(map<int, long long>::iterator it=m[prod].begin(); it != m[prod].end(); ++it)
						res.insert(it->first);
				} else {
					for(set<int>::iterator it=res.begin(); it != res.end();) {
						if(m[prod].find(*it) == m[prod].end()) 
							it = res.erase(it);
						else
							++it;
					}
				}
			}

			if(res.size() == 1) {
				fout<<sets[*(res.begin())]<<endl;
				cout<<sets[*(res.begin())]<<endl;
				cnt++;
				continue;
			}

			long double mx=1;
			int result=0;
			for(set<int>::iterator it=res.begin(); it != res.end(); ++it) {
				int x[10];
				MMS(x);
				long double cases=1;
				FR(j,0,N) {
					cases *= (j+1);
					x[sets[*it][j]-'0']++;
					cases /= x[sets[*it][j]-'0'];
				}
				for(set<long long>::iterator it1 = prodset.begin(); it1 != prodset.end(); ++it1) {
					cases *= m[*it1][*it];
				}
				if(mx<cases) {
					mx=cases;
					result = *it;
				}
			}
			fout<<sets[result]<<endl;
			cout<<sets[result]<<endl;
		}
		cout<<cnt<<endl;
	}
}
*/

/*
int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\A-large-practice.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\A-large-practice.out",ios::out);
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
	
	int A,N,s[101];
	FRE(e,1,casecnt)
	{
		MMS(s);
		fin>>A>>N;
		FR(i,0,N) {
			fin>>s[i];
		}
		sort(s,s+N);
		long long val=A;
		int ret=0;
		FR(i,0,N) {
			if(val>s[i]) {
				val += s[i];
				continue;
			}

			int delSteps = N-i;
			int steps=0;
			long long tempVal = val;
			for(; steps < delSteps ;) {
				steps++;
				tempVal += tempVal-1;
				if(tempVal > s[i]) {
					break;
				}
			}
			if(steps>=delSteps) {
				ret += delSteps;
				break;
			}
			ret += steps;
			val = tempVal+s[i];
		}
		fout<<"Case #"<<e<<": "<<min(ret,N)<<endl;
		cout<<"Case #"<<e<<": "<<min(ret,N)<<endl;
	}
	return 0;
}
*/

/*
long double d[2840][2840];
int main(int argc, _TCHAR* argv[])
{
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\B-large-practice.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Visual Studio 2010\\Projects\\Algo\\GCJ\\GCJ13\\testfiles\\B-large-practice.out",ios::out);
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
		int N, X, Y;
		fin>>N>>X>>Y;
		MMS(d);
		X=abs(X), Y=abs(Y);
		int t=N;
		int x=0;
		for(x=0;x<(X+Y) && t>0;x+=2) {
			t -= x*2+1;
		}
		// Not enough diamonds
		if(t<=0) {
			fout<<"Case #"<<e<<": 0.000000000"<<endl;
			cout<<"Case #"<<e<<": 0.000000000"<<endl;
			continue;
		}
		// Too many diamonds
		if(t>=2*x+1) {
			fout<<"Case #"<<e<<": 1.000000000"<<endl;
			cout<<"Case #"<<e<<": 1.000000000"<<endl;
			continue;
		}
		d[0][0]=1.0;
		for(int i=0; i<t; i++) {
			int left = (i-x)<=0 ? 0 : (i-x);
			int right = (i-x)<=0 ? i : x;
			for(int j=left; j<=x && right>=0; j++, right--) {
				if(j<x) {
					d[j+1][right] += 0.5*d[j][right];
				} else {
					d[j][right+1] += 0.5*d[j][right];
				}
				if(right<x) {
					d[j][right+1] += 0.5*d[j][right];
				} else {
					d[j+1][right] += 0.5*d[j][right];
				}
			}
		}

		long double ret=0.0;
		for(int j=Y+1, i=t-Y-1; j<=x+1 && i>=0; j++, i--) 
			ret += d[i][j];

		fout.precision(9);
		cout.precision(9);
		fout<<"Case #"<<e<<": "<<fixed<<ret<<endl;
		cout<<"Case #"<<e<<": "<<fixed<<ret<<endl;
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
	
	char s[1000002];
	FRE(e,1,casecnt)
	{
		fin>>s;
		int len= strlen(s);
		int L;
		fin>>L;
		long long ret=0;
		int prev=0;
		int curlen=0;
		FR(i,0,len) {
			if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u') {
				ret += prev;
				curlen=0;
				continue;
			}
			curlen++;
			if(curlen >= L) {
				ret += i-L+2;
				prev = i-L+2;
			} else {
				ret += prev;
			}
		}
		fout<<"Case #"<<e<<": "<<ret<<endl;
		cout<<"Case #"<<e<<": "<<ret<<endl;
	}
	return 0;
}
