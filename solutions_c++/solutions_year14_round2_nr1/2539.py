#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <cmath>

using namespace std;

const int MAXN = 200;



void solve(int test){
	
	int n;
	scanf("%d", &n);

	string all[MAXN];
	string master;
	int rep[MAXN][MAXN];
	//~ int index[MAXN];
	
	fill( (int*)rep, (int*)rep + MAXN*MAXN, 0);
	
	for(int i = 0; i < n; i++)
		cin >> all[i];
	
	master = all[0][0];
	for(int i = 1; i < all[0].size(); i++)
		if(master[master.size()-1] != all[0][i])
			master += all[0][i];//, ;
	
	//~ cout << master << endl;
	
	int index = master.size();
	
	bool winable = true;
	for(int i = 0; i < n; i++){
		int ind = 0;
		
		for(int j = 0; j < all[i].size();){
			if(ind > index){
				printf("Case #%d: Fegla Won\n", test);
				return;
				}
			if(master[ind] != all[i][j])
				ind++;
			else
				rep[i][ind]++,  j++;
			}
				
		ind++;
		}
	
	for(int i = 0; i < n; i++)
		for(int k = 0; k < index; k++)
			if(rep[i][k] == 0){
				printf("Case #%d: Fegla Won\n", test);
				return;
				}
	int answ = 0;
	for(int i = 0; i < index; i++){
		double vid = 0;
		
		for(int k = 0; k < n; k++)
			vid += rep[k][i];
			
		vid /= n;
		
		vid = floor(vid + 0.5);
		int t = (int)vid;
		
		//~ cout << t << endl;
		
		for(int k = 0; k < n; k++)
			answ += abs(t - rep[k][i]);
		
		}
	
	printf("Case #%d: %d\n", test, answ);
	}

int main(){	
	int testcases;
	scanf("%d", &testcases);
	
	for(int test = 0; test < testcases; test++)
		solve(test+1);
	
	return 0;
}
