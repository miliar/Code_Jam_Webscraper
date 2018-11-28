#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

#define ll long long

string words[]={
"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"
};


string ex="ZWXGHRFVON";
int digs[]={0,2,6,8,3,4,5,7,1,9};

int main()
{
	int N;
	scanf("%d",&N);
	char s[3000];
	int kol[10], symb[256];
	for(int tNum=1; tNum<=N; ++tNum)
	{
		printf("Case #%d: ",tNum);	
		fill(kol,kol+10,0);
		fill(symb,symb+256,0);
		scanf("%s",s);
		for(int i=0; s[i]!=0; ++i)
			++symb[s[i]];
		for(int i=0; i<10; ++i)
			while(symb[ex[i]]>0){
				int ok=1;
				for(int j=0; j<words[digs[i]].length(); ++j)
					if(symb[words[digs[i]][j]]<=0)
						ok=0;
				if(!ok) break;
				for(int j=0; j<words[digs[i]].length(); ++j)
					--symb[words[digs[i]][j]];
				++kol[digs[i]];
			}
		for(int i=0; i<10; ++i)
			for(int j=0; j<kol[i]; ++j)
				printf("%d",i);
		printf("\n");
	}
}
