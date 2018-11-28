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

//Google Code Jam 2013 Qualification Round, Problem C code.google.com/codejam
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
	const long long nmin=1, nmax=10000000, tmax=1000, pmax=14;
	long long test, cases, n, m, mt, res, i, j, k, t, rt, ax, bx;
	long long t0, t1, r, q, a, a2, b, m2;
	//char ch, ch0, ch1;
	//string sres[2]={"YES", "NO"};
	string s, st, sr, s0, s1, s2;
	//long double dt;

	//if(INPUT_FROM) from.open("test.txt");
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	static long long v[nmax+1], v10[pmax], vt[pmax];
	//vector<long long> v;
	//static long long vr[qmax];
	//deque<long long> dq;
	//map<string, long long> ms;
	//map<long long, vector<long long> > mi;
	//map<long long, vector<long long> >::iterator it;
	//typedef map<string, long long>::const_iterator CI;
	//time_t ltime0, ltime1;

	//time(&ltime0);
	v10[0]=1;
	for(i=1;i<pmax;i++) v10[i]=v10[i-1]*10;

	for(t=1;t<=tmax;t++){
		if(t%10==0) continue;
		rt=t;

		s=lltostr(t);
		ax=1; mt=s.size();
		t0=0;
		for(j=mt-1;j>=0;j--){
			t0+=(s[j]-'0')*v10[mt-1-j];
		}
		
		for(i=-1;i<10;i++){
			a=t;
			if(i>=0) a+=t0*v10[mt+1]+i*v10[mt];
			else a+=t0*v10[mt];

			a2=a*a;
			s2=lltostr(a2);
			m2=s2.size();
			
			q=(m2>>1); ax=1;
			for(k=0;(k<q)&&(ax==1);k++){
				if(s2[k]!=s2[m2-1-k]) ax=0;
			}
			if(ax==1){
				v[a]=1;
				//cout<<a<<' '<<a2<<endl;
			}
		}
	}

	v[0]=v[1]=v[2]=v[3]=1;
	for(i=1;i<=nmax;i++) v[i]+=v[i-1];

	//scanf("%lld\n", &cases);
	fromc>>cases;
	for(test=1;test<=cases;test++){
		//scanf("%lld %lld %lld %lld %lld\n", &a, &b, &c, &d, &k);
		fromc>>a>>b;

		t0=sqrt(1.0*a); if(t0*t0==a) t0--;
		t1=sqrt(1.0*b);
		res=v[t1]-v[t0];

		//printf("%lld\n", res);
		cout<<"Case #"<<test<<": "<<res<<endl;
	}

	//time(&ltime1);

	//printf("Runtime in seconds:\t%ld\n", ltime1 - ltime0);

	return 0;
}

string lltostr(long long x){
	long long n, rt, i;
	char ch;
	string s, st;

	s=st="";
	n=0;
	if(x<0){
		s+='-';
		x=-x;
	}
	if(x==0) s="0";
	else{
		rt=x;
		while(rt>0){
			ch='0'+rt%10;
			st+=ch;
			rt/=10;
			n++;
		}
	}
	for(i=n-1;i>=0;i--) s+=st[i];

	return s;
}


