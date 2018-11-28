// prob_A.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#include <vector>
#include <stack>
#include <algorithm>

using namespace std; 

//#define out	stdout
#define BASE	1000002013

vector<pair<int,int>> origin,dest ; 

int N,M ; 

__int64 previous, now ; 

bool comp ( const pair<int, int>& left, const pair<int, int>& right ) {
	return ( (left.first < right.first) || ( (left.first == right.first) &&  (left.second < right.second ) ) ) ; 
}



__int64 process() {
	previous =0 ; now = 0 ; 
	for(int i=0;i<M;i++) {
		__int64 k= dest[i].first - origin[i].first +1;
		previous += ( ( ((k-1)*(2*N+2-k)/2)%BASE ) * origin[i].second ) % BASE ;
		previous %= BASE;
	}

	sort(origin.begin(),origin.end(),comp);
	sort(dest.begin(),dest.end(),comp);

	stack<pair<int,int>> table ; 

	int idx1=0, idx2=0 ; 
	while ( idx1<M || idx2 <M) {
		if (idx1<M && ( idx2==M || origin[idx1].first <= dest[idx2].first) ) {
			table.push(origin[idx1]);
			idx1++;
		} else {
			while ( dest[idx2].second >0) {
				if ( table.top().second > dest[idx2].second ) {
					__int64 k = dest[idx2].first - table.top().first+1;
					now += ( ( ((k-1)*(2*N+2-k)/2)%BASE ) * dest[idx2].second ) % BASE ;
					now %= BASE;
					table.top().second -= dest[idx2].second ; 
					dest[idx2].second =0 ; break; 
				} else {
					__int64 k = dest[idx2].first - table.top().first+1;
					now += ( ( ((k-1)*(2*N+2-k)/2)%BASE ) * table.top().second ) % BASE ;
					now %= BASE;
					dest[idx2].second -= table.top().second ;
					table.pop();
				}
			}
			idx2++;
		}
	}
	
	return ((previous+BASE)-now)%BASE ; 
}


int _tmain(int argc, _TCHAR* argv[])
{
	int numCases;

	FILE *in = fopen("A-large.in","r");
	FILE *out = fopen("output.txt","w");

	fscanf(in,"%d\n",&numCases);

	for(int cnt=1;cnt<=numCases;cnt++){
		fprintf(out,"Case #%d: ",cnt);
		fscanf(in,"%d %d\n",&N,&M); 
		origin.clear(); dest.clear();
		for(int i=0;i<M;i++) {
			int o,e,p;
			fscanf(in,"%d %d %d\n",&o,&e,&p);
			origin.push_back(make_pair(o,p));
			dest.push_back(make_pair(e,p));
		}
		fprintf(out,"%I64d\n",process());
	}

	fclose(in);
	fclose(out);

	//char temp = getchar();

	return 0;
}

