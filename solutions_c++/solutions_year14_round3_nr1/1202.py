// GCJ.cpp : Defines the entry point for the console application.
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
	fin.getline(s, 500);
	memset(s, 0, sizeof(char)* 500);
	fin.getline(s, 500);
	string str(s);
	for (int i = 0; i != string::npos;)
	{
		string sub;
		int pos = str.find_first_of(' ', i);
		if (pos != string::npos)
		{
			sub = str.substr(i, pos - i);
			i = pos + 1;
			int val;
			sscanf_s(sub.c_str(), "%d ", &val);
			v.push_back(val);
		}
		else
		{
			sub = str.substr(i, str.length() - i);
			i = string::npos;
			int val;
			sscanf_s(sub.c_str(), "%d ", &val);
			v.push_back(val);
		}
	}
}
void parseString(VS &v, string str)
{
	for (int i = 0; i != string::npos;)
	{
		string sub;
		int pos = str.find_first_of('/', i);
		if (pos != string::npos)
		{
			sub = str.substr(i, pos - i);
			i = pos + 1;
			v.push_back(sub);
		}
		else
		{
			sub = str.substr(i, str.length() - i);
			i = string::npos;
			v.push_back(sub);
		}
	}
}

I gcd(I a, I b)
{
	if (a<2 || b<2)
		return 1;
	if (a>b)
	{
		I t = a;
		a = b;
		b = t;
	}
	while (b%a)
	{
		I t = a;
		a = b%a;
		b = t;
	}
	return a;
}

class Counting
{
	I arr[67][67];
public:
	Counting()
	{
		memset(arr, 0, sizeof(I)* 67 * 67);
		FR(i, 0, 67)
		{
			arr[i][0] = 1;
			arr[i][i] = 1;
		}
		FRE(i, 1, 66)
			FRE(j, 1, i - 1)
			arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1];
	}
	I ncr(int n, int r)
	{
		return arr[n][r];
	}
};

/*
int _tmain(int argc, _TCHAR* argv[]) {
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\C-large-practice.in",ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\C-large-practice.out",ios::out);
	
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
	FRE(e, 1, casecnt) {
		int n, m;
		int c[50], prev[50];
		vector<int> v[50];
		int root = 0;
		int mn;
		fin >> n >> m;
		//if (e == 52)
		//	cout << n << "," << m << endl;
		FR(i, 0, n) {
			fin >> c[i];
			//if (e == 52)
				//cout << c[i] << endl;
			if (c[root] > c[i]) {
				root = i;
			}
		}
		FR(i, 0, m) {
			int x, y;
			fin >> x >> y;
			//if (e == 52)
				//cout << x <<", "<<y<< endl;
			v[x-1].push_back(y-1);
			v[y-1].push_back(x-1);
		}

		//if (e != 52)
			//continue;

		bool vis[50];
		MMS(vis);
		memset(prev, -1, sizeof(prev));
		vector<int> ret;
		ret.push_back(c[root]);
		vis[root] = true;

		FR(i, 1, n) {
			mn = -1;
			int nroot = -1, pr=-1;
			FR(j, 0, v[root].size()) {
				if (vis[v[root][j]] == 0) {
					if (mn==-1 || c[mn] > c[v[root][j]]) {
						mn = v[root][j];
						pr = root;
					}
				}
			}

			nroot = root;
			list<int> newNodes;
			bool vis1[50];
			memcpy(vis1, vis, sizeof(vis));
			vector<pair<int, int> > pt;
			while (prev[nroot] != -1) {
				list<int> l;
				l.push_back(nroot);
				vis1[nroot] = true;
				while (!l.empty()) {
					int node = l.front();
					l.pop_front();
					FR(j, 0, (v[node].size())) {
						if (!vis1[v[node][j]]) {
							l.push_back(v[node][j]);
							vis1[v[node][j]] = true;
							newNodes.push_back(v[node][j]);
						}
					}
				}
				nroot = prev[nroot];
				l.push_back(nroot);
				bool vis2[50];
				memcpy(vis2, vis, sizeof(vis));
				vis2[nroot] = true;
				list<int> newNodes1 = newNodes;
				while (!l.empty()) {
					int node = l.front();
					l.pop_front();
					FR(j, 0, (v[node].size())) {
						if (!vis2[v[node][j]] || prev[node] == v[node][j]) {
							l.push_back(v[node][j]);
							vis2[v[node][j]] = true;
							newNodes1.remove(v[node][j]);
						}
					}
				}

				FR(j, 0, v[nroot].size()) {
					if (vis[v[nroot][j]] == 0) {
						pt.push_back(pair<int, int>(v[nroot][j], nroot));
					}
				}
				if (newNodes1.empty()) {
					FR(j, 0, pt.size()) {
						if (mn == -1 || c[mn] > c[pt[j].first]) {
							mn = pt[j].first;
							pr = pt[j].second;
						}
					}
				}
			}

			ret.push_back(c[mn]);
			vis[mn] = true;
			prev[mn] = pr;
			root = mn;
		}
		fout << "Case #" << e << ": ";
		cout << "Case #" << e << ": ";
		FR(i, 0, ret.size()) {
			cout << ret[i];
			fout << ret[i];
		}
		assert(ret.size() == n);
		cout << endl;
		fout << endl;
	}

	return 0;
}
*/

/*
int _tmain(int argc, _TCHAR* argv[]) {
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\C-small-practice.in", ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\C-small-practice.out", ios::out);

	if (!fin.good())
	{
		cout << "Input file not opened" << endl;
		exit(-1);
	}
	if (!fout.good())
	{
		cout << "Output file not opened" << endl;
		exit(-1);
	}

	fin >> casecnt;
	FRE(e, 1, casecnt) {
		int n, m;
		int c[50], prev[50];
		vector<int> v[50];
		int root = 0;
		int mn;
		fin >> n >> m;
		FR(i, 0, n) {
			fin >> c[i];
			if (c[root] > c[i]) {
				root = i;
			}
		}
		FR(i, 0, m) {
			int x, y;
			fin >> x >> y;
			v[x - 1].push_back(y - 1);
			v[y - 1].push_back(x - 1);
		}

		bool vis[50];
		MMS(vis);
		memset(prev, -1, sizeof(prev));
		vector<int> ret;
		ret.push_back(c[root]);
		vis[root] = true;

		FR(i, 1, n) {
			mn = -1;
			int nroot = -1, pr = -1;
			FR(j, 0, v[root].size()) {
				if (vis[v[root][j]] == 0) {
					if (mn == -1 || c[mn] > c[v[root][j]]) {
						mn = v[root][j];
						pr = root;
					}
				}
			}

			nroot = root;
			list<int> newNodes;
			vector<pair<int, int> > pt;
			while (prev[nroot] != -1) {
				list<int> l;
				nroot = prev[nroot];
				l.push_back(nroot);
				bool vis2[50];
				memcpy(vis2, vis, sizeof(vis));
				vis2[nroot] = true;
				while (!l.empty()) {
					int node = l.front();
					l.pop_front();
					FR(j, 0, (v[node].size())) {
						if (!vis2[v[node][j]] || prev[node] == v[node][j]) {
							l.push_back(v[node][j]);
							vis2[v[node][j]] = true;
						}
					}
				}

				FR(j, 0, v[nroot].size()) {
					if (vis[v[nroot][j]] == 0) {
						pt.push_back(pair<int, int>(v[nroot][j], nroot));
					}
				}
				bool found = true;
				FR(j, 0, n) {
					if (!vis2[j]) {
						found = false;
						break;
					}
				}
				if (found) {
					FR(j, 0, pt.size()) {
						if (mn == -1 || c[mn] > c[pt[j].first]) {
							mn = pt[j].first;
							pr = pt[j].second;
						}
					}
				}
			}

			ret.push_back(c[mn]);
			vis[mn] = true;
			prev[mn] = pr;
			root = mn;
		}
		fout << "Case #" << e << ": ";
		cout << "Case #" << e << ": ";
		FR(i, 0, ret.size()) {
			cout << ret[i];
			fout << ret[i];
		}
		assert(ret.size() == n);
		cout << endl;
		fout << endl;
	}

	return 0;
}
*/

int _tmain(int argc, _TCHAR* argv[]) {
	int casecnt;
	fin.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\A-large.in", ios::in);
	fout.open("C:\\Users\\ravill\\Documents\\Psl\\GCJ\\A-large.out", ios::out);

	if (!fin.good())
	{
		cout << "Input file not opened" << endl;
		exit(-1);
	}
	if (!fout.good())
	{
		cout << "Output file not opened" << endl;
		exit(-1);
	}

	fin >> casecnt;
	FRE(e, 1, casecnt) {
		char s[100];
		I p, q;
		fin >> s;
		sscanf_s(s, "%lld/%lld", &p, &q);
		I g = gcd(p, q);
		p = p / g;
		q = q / g;
		I ret = -1;
		for (int i = 1; i <= 40; i++) {
			if (q == (1LL << i)) {
				I v=-1, j;
				for (j = i-1; j >=0; j--) {
					if ((p - (1LL << j)) >= 0) {
						v = j;
						break;
					}
				}
				ret = i - j;
				break;
			}
		}
		fout << "Case #" << e << ": ";
		cout << "Case #" << e << ": ";
		if (ret == -1) {
			fout << "impossible";
			cout << "impossible";
		}
		else {
			assert(ret <= 40);
			fout << ret;
			cout << ret;
		}
		fout << endl;
		cout << endl;
	}

	return 0;
}