#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <iostream>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		vector<int> A(10,0), L(26,0);
		string S;
		cin>>S;
		for(int j=0; j<S.length(); j++){
			L[S[j]-'A']++;
		}
		
		A[0]=L['Z'-'A'];
		L['E'-'A']-=L['Z'-'A'];
		L['R'-'A']-=L['Z'-'A'];
		L['O'-'A']-=L['Z'-'A'];
		L['Z'-'A']-=L['Z'-'A'];
		
		A[2]=L['W'-'A'];
		L['T'-'A']-=L['W'-'A'];
		L['O'-'A']-=L['W'-'A'];
		L['W'-'A']-=L['W'-'A'];
		
		A[4]=L['U'-'A'];
		L['F'-'A']-=L['U'-'A'];
		L['O'-'A']-=L['U'-'A'];
		L['R'-'A']-=L['U'-'A'];
		L['U'-'A']-=L['U'-'A'];
		
		A[6]=L['X'-'A'];
		L['S'-'A']-=L['X'-'A'];
		L['I'-'A']-=L['X'-'A'];
		L['X'-'A']-=L['X'-'A'];
		
		A[8]=L['G'-'A'];
		L['E'-'A']-=L['G'-'A'];
		L['I'-'A']-=L['G'-'A'];
		L['H'-'A']-=L['G'-'A'];
		L['T'-'A']-=L['G'-'A'];
		L['G'-'A']-=L['G'-'A'];
		
		A[1]=L['O'-'A'];
		L['N'-'A']-=L['O'-'A'];
		L['E'-'A']-=L['O'-'A'];
		L['O'-'A']-=L['O'-'A'];
		
		A[3]=L['R'-'A'];
		L['T'-'A']-=L['R'-'A'];
		L['H'-'A']-=L['R'-'A'];
		L['E'-'A']-=L['R'-'A'];
		L['E'-'A']-=L['R'-'A'];
		L['R'-'A']-=L['R'-'A'];
		
		A[5]=L['F'-'A'];
		L['I'-'A']-=L['F'-'A'];
		L['V'-'A']-=L['F'-'A'];
		L['E'-'A']-=L['F'-'A'];
		L['F'-'A']-=L['F'-'A'];
		
		A[7]=L['S'-'A'];
		L['E'-'A']-=L['S'-'A'];
		L['V'-'A']-=L['S'-'A'];
		L['E'-'A']-=L['S'-'A'];
		L['N'-'A']-=L['S'-'A'];
		L['S'-'A']-=L['S'-'A'];
		
		A[9]=L['I'-'A'];
		L['N'-'A']-=L['I'-'A'];
		L['N'-'A']-=L['I'-'A'];
		L['E'-'A']-=L['I'-'A'];
		L['I'-'A']-=L['I'-'A'];
		
		for(int j=0; j<10; j++){
			for(int k=0; k<A[j]; k++){
				printf("%d",j);
			}
		}
		printf("\n");
	}
}	
