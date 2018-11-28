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
#include <cstring>
using namespace std;

//Google Code Jam 2017 Qualification Round, Problem A code.google.com/codejam
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
	const int nmin = 1, nmax = 1000;
	int test, cases, n, m, mt, res, rt, i, j, k, t, ax, bx, a;
	int i0, i1, i2;
	int r, r0, r1;
	char ch;
	//string sres[2]={"YES", "NO"};
	//string sres[2]={"Bad magician!", "Volunteer cheated!"};
	string s, st, sr;
	//long double dt;

	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//static int vv0[nmax][nmax], vv1[nmax][nmax];
	static int w[nmax];
	//vector<int> vr;
	//deque<int> dq;
	//map<char, char> mc;
	//map<long long, long long>::iterator it;
	//typedef map<string, long long>::const_iterator CI;


	scanf("%d\n", &cases);
	//cin >> cases;
	for(int test = 1;test <= cases;++test){
		//scanf("%d ", &n);
		//memset(w, 0, sizeof(w));
		cin >> s;
		scanf(" %d\n", &k);

		n = s.size();
		memset(w, 0, n*sizeof(int));

		r = 0;
		ax = 0;

		i0 = 0;
		while((i0 < n)&&(r >= 0)){
			bx = 0;
			if((ax == 0)&&(s[i0] == '-')){
				bx = 1;
			}else if((ax == 1)&&(s[i0] == '+')){
				bx = 1;
			}
			if(bx){// a new flip
				if(i0 + k - 1 < n){
					w[i0 + k - 1] = 1; // end of this flip
					++r;
					ax = 1 - ax;
				}else r = -1;
			}
			if(w[i0]) ax = 1 - ax; // end of a flip
			++i0;
		}

		if(r == -1) printf("Case #%d: IMPOSSIBLE\n", test);
		else printf("Case #%d: %d\n", test, r);

		//cout<<"Case #"<<test<<": "<<r<<endl;
		//else if(t==0) cout<<"Case #"<<test<<": "<<sres[1]<<endl;
		//else cout<<"Case #"<<test<<": "<<sres[0]<<endl;

		//cout<<"Case #"<<test<<": "<<sres[ax]<<endl;
	}

	return 0;
}

