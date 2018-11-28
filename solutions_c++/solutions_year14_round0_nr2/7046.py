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


void make(int tcase) {


	fout<< "Case #"<<tcase<<": ";
	double c, f, x;
	fin >> c;
	fin >> f;
	fin >> x;
	double s = 2;

	double cc = 0;
	double t = 0;
	while (true){
		if((x - c)/ s <= (x)/ (s+f)){
			t += x/s;
			break;
		} else {
			t += c/s;
			s += f;

		}
	}

	char st [100];
	sprintf(st,"%.7f", t);
	fout << st << endl;

    return;
}



int main() {

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
