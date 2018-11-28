#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int t;
int r1, r2;
int p1[5][5], p2[5][5];
vector <int> v;

int main(){
	scanf("%d", &t);
	for(int x=1; x<=t; x++){
		printf("Case #%d: ", x);
		scanf("%d", &r1);
		for(int i=1; i<=4; i++)
			for(int j=1; j<=4; j++)
				scanf("%d", &p1[i][j]);
		for(int i=1; i<=4; i++)
			v.push_back(p1[r1][i]);
		scanf("%d", &r2);
		for(int i=1; i<=4; i++)
			for(int j=1; j<=4; j++)
				scanf("%d", &p2[i][j]);
		for(int i=1; i<=4; i++)
			v.push_back(p2[r2][i]);
		sort(v.begin(), v.end());
		int wyn=0;
		bool ok=false;
		bool oszukal=false;
		for(int i=0; i<7; i++){
			if(v[i]==v[i+1] && ok==false){wyn=v[i];ok=true;}
			else if(v[i]==v[i+1] && ok==true)oszukal=true;
		}
		if(wyn!=0 && oszukal==false)printf("%d\n", wyn);
		if(wyn==0)puts("Volunteer cheated!");
		if(wyn!=0 && oszukal==true)puts("Bad magician!");
		v.clear();
	}
	
	return 0;
}
