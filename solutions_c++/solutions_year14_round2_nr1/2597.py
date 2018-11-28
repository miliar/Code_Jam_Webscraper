#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include <conio.h>
#include <functional>
#include <numeric>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>  

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define Fill(s,v) memset(s,v,sizeof(s))
#define ull unsigned long long
using namespace std;

fstream fout;
fstream fin;
int read_int_from_char(char in[],int l,int ret[]){
  int i,n,fg,mfg;
  if(l<0) {for(i=0;;i++) if(in[i]<' ') break; l=i;}
  n=0; fg=0; mfg=0; ret[0]=0;
  rep(i,l+1){
    if(in[i]=='-'){mfg=1; continue;}
    if(isdigit(in[i])){ret[n]=ret[n]*10+in[i]-'0'; fg=1; continue;}
    if(!fg) continue;
    fg=0; if(mfg){ret[n]=-ret[n]; mfg=0;}
    ret[++n]=0;
  }
  return n;
}
//ceil round
int gcd(int a, int b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}
int lcm(int a, int b) {
	return (a/gcd(a,b))*b; 
}
int lcms(int l, int * a)
{
        int i, result;
        result = 1;
        for (i = 0; i < l; i++) result = lcm(result, a[i]);
        return result;
}
int gcds(int l, int * a)
{
        int i, result;
        result = a[0];
        for (i = 1; i < l; i++) result = gcd(result, a[i]);
        return result;
}
void multy(){
	int j;
	string line;
	for(j=0;j>3;j++){
		getline(fin, line);
        istringstream iss(line);
		int A;

        while (iss >> A)
        {
			double B;
			iss >> B;
			fout <<A << B;
            
        }
	}
    
}

char nonv(char c){
	if(c!='a' && c!='A' 
	&& c!='e' && c!='E'
	&& c!='i' && c!='I'
	&& c!='o' && c!='O'
	&& c!='u' && c!='U')
	return true;
	return false;
}
		
/*
void make(int t) {

	int n;
	ull i;
	fout<< "Case #"<<t<<": ";

 	string s;
	s.reserve(1000000);
	fin >> s;
	fin >> n;
	ull l = 0;
	ull res =0;
	ull lbefore = 0;
	for(i=0;i<s.length()-n+1;i++){
		bool b = true;
		for(ull j=0; j<n;j++){
			if(!nonv(s[j+i])){
				b = false;
				break;
			}
		}
		if(b){
			ull before = i-lbefore;
			lbefore = i+1;
			ull after = s.length()-n-i;
			res +=(before+1)*(after+1);
		}

	}

	fout.precision(3);
	fout << res<<" " << endl;

 
    return;
}
*/

string contract(string& a){
	string b;
	int i;
	int p;
	b.push_back(a[0]);
	p = 0;
	for(i = 1; i< a.size(); i++)
		if(a[i] == b[p]){

		}else {
			p++;
			b.push_back(a[i]);
		}
	return b;
}
void make(int t) {

	int N;
	fin >> N;
	fout<< "Case #"<<t<<": ";
	vector<string> lines;
	int i;
	string s4;
	getline(fin, s4);
	for(i=0;i<N;i++){
		string s;
		getline(fin, s);
		lines.push_back(s);
	}
	vector<string> contracted;
	string s1 = contract(lines[0]);
	for(i=1;i<N;i++){
		string s;
		s = contract(lines[i]);
		if (s.compare(s1) !=0) {
			fout<<  "Fegla Won" << endl;
			return;

		}
	}
	int count[100][100];
	int j;
	for (i= 0; i<100; i++)
		for (j= 0; j<100; j++)
			count [i][j] = 0;
	int p;
	int c;
	for(i=0;i<N;i++){
		p = 0;

		count[i][0] = 1;
		for (j= 1; j<lines[i].size(); j++) {
			if(lines[i][j] == lines[i][j-1]){
				count[i][p] ++;
			} else {
				p++;
				count[i][p] ++;
			}

		}
	}
	float avr[100];
	for (j= 0; j<100; j++)
		avr[j] = 0;
	for (j= 0; j<p+1; j++){
		for (i= 0; i<N; i++){
			avr[j] += (float)count[i][j]/ (float) N;
		}
	}
	int x[100];
	for (j= 0; j<p+1; j++){
		 avr[j] = avr[j]  + 0.5; 
		 x[j] = (int) avr[j];
	}


	ull move = 0;
	for (j = 0; j<p+1; j++) {
		for (i= 0; i<N; i++){
			move += abs(count[i][j] - x [j]);
		}
	}

	fout << move <<" " << endl;

 
    return;
}




int main() {
	int i,j;

	fin.open("B.in", fstream::in | fstream::out | fstream::app);
	fout.open("B.out", fstream::out);
	int T;
	fin >> T;


	int t = 1;
    while(T--) {
        make(t);
		t++;
    }
	fin.close();
	fout.close();
    return 0;
}
