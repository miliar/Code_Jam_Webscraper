#include <stdio.h>
#include <string>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <map>
#include <list>
#include <cstdlib>
#include <time.h>
using namespace std;

//Google Code Jam 2014 Qualification Round, Problem C code.google.com/codejam
//Disable warning messages C4996.
#pragma warning(disable:4996)

#define INPUT_FROM 0
#if INPUT_FROM
#define fromc from
#else
#define fromc cin
#endif

//long long fr(vector<long long>&, long long);
string lltostr(long long);

int main(int argc, char **argv)
{
	//ifstream from;
	const int nmin=1, nmax=5;
	int test, cases, n, m, mt, res, i, j, k, t, rt, ax, bx;
	int i0, i1, t0, t1, r, c;
	char ch, ch0, ch1;
	//string sres[2]={"YES", "NO"};
	//string s, st, sr, s0, s1, s2;
	//long double dt;

	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	//static long long v[nmax+1], v10[pmax], vt[pmax];
	//vector<long long> v;
	vector<vector<char> > vv;
	//static long long vr[qmax];
	//deque<int> dq, dq0, dq1, dq2;
	//map<string, long long> ms;
	//map<long long, vector<long long> > mi;
	//map<long long, vector<long long> >::iterator it;
	//typedef map<string, long long>::const_iterator CI;
	//time_t ltime0, ltime1;

	//time(&ltime0);


	//scanf("%lld\n", &cases);
	fromc>>cases;
	for(int test=1;test<=cases;++test){
		//scanf("%lld %lld %lld %lld %lld\n", &a, &b, &c, &d, &k);
		fromc>>r>>c>>m;

		bx=0;
		if(r>c) swap(r,c), bx=1;

		vv.resize(r);
		for(int i=0;i<r;i++) vv[i].resize(c,'.');

		//m < r*c
		ax = 1;
		if(r==1){
			vv[0][c-1]='c';
			for(int j=0;j<m;j++) vv[0][j]='*';
		}else if(r==2){
			if(m%r==0){
				if(m<r*c-2){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
				}else ax=0;
			}else{
				if(m==r*c-1){
					vv[0][c-1]='c';
					vv[1][c-1]='*';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
				}else ax=0;
			}
		}else if(r==3){
			if(m%r==0){
				if(m<r*c-3){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
				}else ax=0;
			}else if(m%r==1){
				if(m<r*c-5){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-1][m/r]='*';
				}else ax=0;
			}else{
				if(m==r*c-1){
					vv[0][c-1]='c';
					vv[1][c-1]='*';
					vv[2][c-1]='*';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
				}else if(m==r*c-4){
					vv[0][c-1]='c';
					for(int i=0;i<2;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					for(int j=0;j<m/r+2;j++) vv[r-1][j]='*';
				//}else if(m==r*c-7){
					/*if(c<=3) ax=0;
					else if(c==5){
						vv[0][c-1]='c';
						vv[0][0]='*';
						vv[1][0]='*';
						for(int j=0;j<c;j++) vv[r-1][j]='*';
					}*/
				}else if(m<r*c-7){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-1][m/r]='*';
					vv[r-1][m/r+1]='*';
				}else ax=0;
			}
		}else if(r==4){
			if(m%r==0){
				if(m==r*c-4){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r-1;j++) vv[i][j]='*';
					for(int i=r-2;i<r;i++)
						for(int j=m/r-1;j<m/r+1;j++) vv[i][j]='*';
				}else{
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
				}
			}else if(m%r==1){
				if(m<r*c-7){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-1][m/r]='*';
				}else ax=0;
			}else if(m%r==2){
				if(m==r*c-6){
					//t = (r*c-m)/2; t = t%2;
					vv[0][c-1]='c';
					for(int i=0;i<2;i++)
						for(int j=0;j<m/r-1;j++) vv[i][j]='*';
					for(int i=2;i<r;i++)
						for(int j=0;j<m/r+2;j++) vv[i][j]='*';
				}else if(m<r*c-6){
					vv[0][c-1]='c';
					for(int i=0;i<2;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					for(int i=2;i<r;i++)
						for(int j=0;j<m/r+1;j++) vv[i][j]='*';
				}else ax=0;
			}else{
				if(m==r*c-1){
					vv[0][c-1]='c';
					vv[1][c-1]='*';
					vv[2][c-1]='*';
					vv[3][c-1]='*';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
				}else if(m==r*c-9){
					vv[0][c-1]='c';
					for(int i=0;i<3;i++)
						for(int j=0;j<c-3;j++) vv[i][j]='*';
					for(int j=0;j<c;j++) vv[r-1][j]='*';
				}else if(m < r*c-9){
					vv[0][c-1]='c';
					for(int i=0;i<r-1;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-2][m/r]='*';
					for(int j=0;j<m/r+2;j++) vv[r-1][j]='*';
				}else ax=0;
			}
		}else if(r==5){//5x5
			if(m%r==0){
				if(m<r*c-5){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
				}else ax=0;
			}else if(m%r==1){
				if(m==r*c-4){
					vv[0][c-1]='c';
					for(int i=0;i<2;i++)
						for(int j=0;j<c-2;j++) vv[i][j]='*';
					for(int i=2;i<r;i++)
						for(int j=0;j<c;j++) vv[i][j]='*';
				}else if(m==r*c-9){
					vv[0][c-1]='c';
					for(int i=0;i<3;i++)
						for(int j=0;j<c-3;j++) vv[i][j]='*';
					for(int i=3;i<r;i++)
						for(int j=0;j<c;j++) vv[i][j]='*';
				}else if(m<r*c-9){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-1][m/r]='*';
				}else ax=0;
			}else if(m%r==2){
				if(m==r*c-8){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-1][m/r]='*';
					vv[r-1][m/r+1]='*';
				}else if(m<r*c-8){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-2][m/r]='*';
					vv[r-1][m/r]='*';
				}else ax=0;
			}else if(m%r==3){
				if(m<r*c-7){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-3][m/r]='*';
					vv[r-2][m/r]='*';
					vv[r-1][m/r]='*';
				}else ax=0;
			}else{
				if(m==r*c-1){
					vv[0][c-1]='c';
					vv[1][c-1]='*';
					vv[2][c-1]='*';
					vv[3][c-1]='*';
					vv[4][c-1]='*';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
				}else if(m==r*c-6){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					for(int i=r-2;i<r;i++)
						for(int j=m/r;j<m/r+2;j++) vv[i][j]='*';
				}else if(m == r*c-11){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					vv[r-2][m/r]='*';
					for(int j=m/r;j<m/r+3;j++) vv[r-1][j]='*';
				}else if(m < r*c-11){
					vv[0][c-1]='c';
					for(int i=0;i<r;i++)
						for(int j=0;j<m/r;j++) vv[i][j]='*';
					for(int i=r-2;i<r;i++)
						for(int j=m/r;j<m/r+2;j++) vv[i][j]='*';
				}else ax=0;
			}
		}


		if(ax==0) cout<<"Case #"<<test<<": "<<"\nImpossible"<<endl;
		else{
			cout<<"Case #"<<test<<": "<<endl;
			if(bx==0){
				for(int i=0;i<r;i++){
					for(int j=0;j<c;j++) cout<<vv[i][j];
					cout<<endl;
				}
			}else{
				for(int j=0;j<c;j++){
					for(int i=0;i<r;i++) cout<<vv[i][j];
					cout<<endl;
				}
			}
		}

		//printf("%lld\n", res);
		//cout<<"Case #"<<test<<": "<<res<<endl;
		vv.clear();
	}

	//time(&ltime1);

	//printf("Runtime in seconds:\t%ld\n", ltime1 - ltime0);

	return 0;
}

