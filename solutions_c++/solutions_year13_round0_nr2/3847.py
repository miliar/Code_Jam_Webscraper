#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <list>
#include <set>
#include <cstdlib>
using namespace std;

//Google Code Jam 2013 Qualification Round, Problem B code.google.com/codejam
//Disable warning messages C4996.
#pragma warning(disable:4996)

#define INPUT_FROM 0
#if INPUT_FROM
#define fromc from
#else
#define fromc cin
#endif

//long long fr(vector<long long>&, long long);

int main(int argc, char **argv)
{
	//ifstream from;
	const int nmin=1, nmax=1000, amax=100;
	int test, cases, n, m, mt, res, rt, i, j, k, t, ax;
	int i0, i1, j0, j1, x0, a, a0, a1;
	//char ch;
	string sres[2]={"YES", "NO"};
	//string s, st, sr;
	//long double dt;


	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	vector<int> vi;
	//deque<long long> dq;
	vector<set< pair<int,int> > > vs0, vs1;
	set< pair<int,int> >::iterator it;
	//map<int, int> mi;
	//typedef map<string, long long>::const_iterator CI;

	//scanf("%lld\n", &cases);
	fromc>>cases;
	for(test=1;test<=cases;test++){
		//scanf("%lld\n", &n);
		fromc>>n>>m;

		vs0.resize(n);
		vs1.resize(m);

		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				fromc>>a;
				vs0[i].insert(make_pair(a, j));
				vs1[j].insert(make_pair(a, i));
			}
		}

		ax=1;
		while((ax==1)&&(n>0)&&(m>0)){
			ax=0;
			a0=amax+1;
			for(i=0;i<n;i++){
				a=vs0[i].begin()->first;
				if(a<a0){
					vi.clear(); mt=0;
					a0=a;
					vi.push_back(i); mt++;
				}else if(a==a0){
					vi.push_back(i); mt++;
				}
			}
			a1=amax+1;
			for(i=0;(i<mt)&&(a0<a1);i++){
				i0=vi[i];
				it=vs0[i0].end(); it--;
				a=it->first;
				if(a<a1) a1=a;
			}
			vi.clear();
			if(a0==a1){
				ax=1;
				swap(vs0[i0],vs0[n-1]);
				vs0.pop_back(); n--;
				for(j=0;j<m;j++) vs1[j].erase(vs1[j].begin());
			}else{
				a0=amax+1;
				for(i=0;i<m;i++){
					a=vs1[i].begin()->first;
					if(a<a0){
						vi.clear(); mt=0;
						a0=a;
						vi.push_back(i); mt++;
					}else if(a==a0){
						vi.push_back(i); mt++;
					}
				}
				a1=amax+1;
				for(i=0;(i<mt)&&(a0<a1);i++){
					i0=vi[i];
					it=vs1[i0].end(); it--;
					a=it->first;
					if(a<a1) a1=a;
				}
				vi.clear();
				if(a0==a1){
					ax=1;
					swap(vs1[i0],vs1[m-1]);
					vs1.pop_back(); m--;
					for(j=0;j<n;j++) vs0[j].erase(vs0[j].begin());
				}
			}
		}

		if((n==0)||(m==0)) ax=1;

		cout<<"Case #"<<test<<": "<<sres[1-ax]<<endl;

		vs0.clear();
		vs1.clear();
	}

	return 0;
}
