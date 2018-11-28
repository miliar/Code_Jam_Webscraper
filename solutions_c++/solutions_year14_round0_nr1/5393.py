#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <cstdlib>
using namespace std;

//Google Code Jam 2014 Qualification Round, Problem A code.google.com/codejam
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
	const int nmin=1, nmax=4;
	int test, cases, n, m, mt, res, rt, i, j, k, t, ax, a;
	int i0, i1, i2;
	int r;
	//char ch;
	//string sres[2]={"YES", "NO"};
	string sres[2]={"Bad magician!", "Volunteer cheated!"};
	//string s, st, sr;
	//long double dt;

	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	static int vv0[nmax][nmax], vv1[nmax][nmax];
	vector<int> vr;
	//deque<long long> dq;
	//map<char, char> mc;
	//map<long long, long long>::iterator it;
	//typedef map<string, long long>::const_iterator CI;


	//scanf("%ld\n", &cases);
	fromc>>cases;
	for(int test=1;test<=cases;test++){
		scanf("%d", &i0); i0--;
		for(int i=0;i<nmax;++i){
			for(int j=0;j<nmax;++j){
				scanf("%d", &vv0[i][j]);
				//fromc>>ch;
				//vv[i][j]=ch;
				//if(ch=='.') ax=3;
			}
		}

		scanf("%d", &i1); i1--;
		for(int i=0;i<nmax;++i){
			for(int j=0;j<nmax;++j) scanf("%d", &vv1[i][j]);
		}

		t = 0;
		for(int i=0;i<nmax;++i){
			for(int j=0;j<nmax;++j){
				if(vv0[i0][i]==vv1[i1][j]){
					t++;
					r = vv0[i0][i];
				}
			}
		}

		if(t==1) cout<<"Case #"<<test<<": "<<r<<endl;
		else if(t==0) cout<<"Case #"<<test<<": "<<sres[1]<<endl;
		else cout<<"Case #"<<test<<": "<<sres[0]<<endl;

		//cout<<"Case #"<<test<<": "<<sres[ax]<<endl;
	}

	return 0;
}

