// teststl.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
//source here
#include<iostream>
#include<map>
#include<string>
#include<fstream>
#include<iomanip>
using namespace std;

int cmp(const void *p1, const void *p2) {
	double a = *((double *)p1);
	double b = *((double *)p2);
	if (a<b) return 1;
	if (a>b) return -1;
	return 0;
}
void Dec() {
	int t;
	cin>>t;
	double now[1001];
	double ken[1001];
	for (int cases=1; cases<=t; cases++) {
		int n;
		cin>>n;
		for (int i=0; i<n; i++) cin>>now[i];
		for (int i=0; i<n; i++) cin>>ken[i];
		qsort(now,n,sizeof(now[0]),cmp);
		qsort(ken,n,sizeof(ken[0]),cmp);
		int score1 = 0;
		int start = 0;
		int end = n-1;
		for (int i=0; i<n; i++) {
			if ( now[start] > ken[i] ) {
				++score1;
				++start;
			} else {
				--end;
			}
		}
		int score2 = 0;
		start = 0;
		end = n-1;
		for (int i=0; i<n; i++) {
			if ( ken[start] > now[i] ) {
				++start;
			} else {
				--end;
				++score2;
			}
		}
		cout<<"Case #"<<cases<<": "<<score1<<" "<<score2<<endl;
	}

}
int main() {
	freopen("D:\\D-small-attempt0.in","r",stdin);
	freopen("D:\\D.out","w",stdout);
//    MagicTrick();
	//click();
	Dec();
	fclose(stdin);
	fclose(stdout);
    return 0;
}
