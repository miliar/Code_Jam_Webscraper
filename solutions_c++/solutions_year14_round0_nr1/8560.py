#include "stdafx.h"

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <fstream>
 
#define PI 3.14159265358979
 
using namespace std;
typedef unsigned long long ull;

int min (int a,int b) {
	return a<b?a:b;
}

int max (int a,int b) {
	return a>b?a:b;
}

//vector <int> (,0);


int main()
{
	FILE * in=fopen("D:\\dev\\VPW\\problem 4\\p4\\p4\\A-small-attempt1.in","r");
	FILE * out=fopen("D:\\dev\\VPW\\problem 4\\p4\\p4\\A-out.out","w");
	int t;
	fscanf(in,"%d",&t);

	for (int i=0;i<t;i++) {
		vector < vector <int> > cards(4,vector <int> (4,0));
		int ans;
		fscanf(in,"%d",&ans);

		for (int j=0;j<4;j++) {
			fscanf(in,"%d %d %d %d",&cards[j][0],&cards[j][1],&cards[j][2],&cards[j][3]);
		}

		vector <int> poss1(4,0);
		for (int j=0;j<4;j++) {
			poss1[j]=cards[ans-1][j];
		}

		fscanf(in,"%d",&ans);

		for (int j=0;j<4;j++) {
			fscanf(in,"%d %d %d %d",&cards[j][0],&cards[j][1],&cards[j][2],&cards[j][3]);
		}

		vector <int> poss2(4,0);
		for (int j=0;j<4;j++) {
			poss2[j]=cards[ans-1][j];
		}

		sort(poss1.begin(),poss1.end());
		sort(poss2.begin(),poss2.end());

		int count=0;
		for (int j=0;j<4;j++) {
			for (int k=0;k<4;k++) {
				if (poss1[j]==poss2[k]) {
					count++;
					ans=poss1[j];
				}
			}
		}

		if (count>1) {
			fprintf(out,"Case #%d: Bad magician!\n",i+1);
		} else if (count==0) {
			fprintf(out,"Case #%d: Volunteer cheated!\n",i+1);
		} else if (count==1) {
			fprintf(out,"Case #%d: %d\n",i+1,ans);
		}
	}
	fclose(in);fclose(out);
    return 0;
}