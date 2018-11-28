#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cstdio>
#include <fstream>
using namespace std;

#define MAX 2

string isOK(int **lawn, int N, int M){
	
	bool **cut = new bool*[N];
	for (int i=0; i<N; i++){
		cut[i]=new bool[M];
		for (int j=0; j<M; j++){
			if (lawn[i][j]<MAX) cut[i][j]=true;
			else cut[i][j]=false;
		}
	}
	for (int i=0; i<N; i++){
		int j=1;
		for (; j<M; j++)
			if (lawn[i][j]>=MAX||lawn[i][j]!=lawn[i][j-1])
				break;
		if (j==M)
			for (int k=0; k<M; k++)
				cut[i][k]=false;
	}

	for (int j=0; j<M; j++){
		int i=1;
		for (; i<N; i++)
			if (lawn[i][j]>=MAX||lawn[i][j]!=lawn[i-1][j])
				break;
		if (i==N)
			for (int k=0; k<N; k++)
				cut[k][j]=false;
	}

	bool toBeCut=true;
	for (int i=0; i<N; i++)
		for (int j=0; j<M; j++)
			if (cut[i][j]){
				toBeCut=false;
				goto end;
			}

	end:
	return toBeCut?"YES":"NO";
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T=0;
	cin>>T;
	int N=-1, M=-1;
	for (int t=1; t<=T; t++){
		cin>>N>>M;
		int **lawn = new int*[N];
		for (int i=0; i<N; i++){
			lawn[i]=new int[M];
			for (int j=0; j<M; j++)
				cin>>lawn[i][j];
		}
		cout<<"Case #"<<t<<": "<<isOK(lawn,N,M)<<"\n";
	}
	return 0;
}