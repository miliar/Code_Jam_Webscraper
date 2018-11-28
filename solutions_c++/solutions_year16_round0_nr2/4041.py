#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>

#define fi "b.inp"
#define fo "b.out"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int len;
char s[110];
char q[1000000][110];
int dist[1000000];
map<string, int> mymap;

void input();
void output();
bool check();

bool done(char x[]){
	//printf("  **%s\n", x);
	for(int i = 0 ; i < len; i++){
		//printf("??? %c\n", x[i]);
		if(x[i] == '-'){
			//printf("??? %c\n", x[i]);
			return false;
		}
	}
	return true;
}

int flip(int dau, int cuoi, int flipPoint){
	int c = 0;
	char x[110];
	
	//printf("%d %d %d\n", dau, cuoi, flipPoint);
	
	for(int i = flipPoint; i >= 0; i--)
		x[c++] = q[dau][i] == '-' ? '+' : '-';
	
	for(int i = flipPoint + 1 ; i < len; i++)
		x[c++] = q[dau][i];
		
	x[c] = '\0';
	
	//printf("gen: %s\n", x);
		
	if(mymap.find(x) == mymap.end()){
		
		mymap[x]++;
		strcpy(q[cuoi + 1], x);
		dist[cuoi + 1] = dist[dau] + 1;
		return 1;
	}
	
	return 0;
}

int bfs(){
	int dau, cuoi;
	
	dau = -1;
	cuoi = 0;
	strcpy(q[0], s);
	dist[0] = 0;
	mymap.clear();
	mymap[s]++;
	
	//printf("%s\n", s);
	
	while(dau < cuoi){
		dau++;
		//printf("  %d %s\n", dau, q[dau]);
		if(done(q[dau])){
			//printf("wtf %s\n", q[dau]);
			return dist[dau];
		}
		
		for(int i = 0; i < len; i++){
			//if(q[dau][i] == '-'){
				cuoi += flip(dau, cuoi, i);
			//}
		}
	}
}



void input()
{
	int ntest;
	
	scanf("%d", &ntest);
	for(int i = 1; i <= ntest ; i++){
		scanf("%s", &s);
		len = strlen(s);
		printf("Case #%d: %d\n", i, bfs());
	}
}

void output()
{
}

int main() {
	
	//freopen(fi,"r",stdin);
	//freopen(fo,"w",stdout);
	
	input();
	
	return 0;
}
