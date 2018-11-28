#define Federico using
#define Javier namespace
#define Pousa std;
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <unordered_map>


Federico Javier Pousa

int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}

void misort(vector<char> &act, int pri, int ult){
	if(ult-pri<=1)return;
	misort(act,pri,(pri+ult)/2);
	misort(act,(pri+ult)/2,ult);
	vector<char> act1, act2;
	for(int i=pri; i<(pri+ult)/2; i++){
		act1.push_back(act[i]);
	}
	for(int i=(pri+ult)/2; i<ult; i++){
		act2.push_back(act[i]);
	}
	
	if(act1>act2){
		for(int i=pri; i<(pri+ult)/2; i++){
			swap(act[i],act[i-pri+(pri+ult)/2]);
		}
	}
	return;
}

int main(){
	int T, N, R, P, S;
	cin >> T;
	for(int caso=1; caso<=T; caso++){
		cin >> N >> R >> P >> S;
		vector<char> torneo;
		vector<char> res;
		bool hay = false;
		
		torneo.push_back('P');
		int act = 0;
		int cuantos = 1;
		for(int i=0; i<N; i++){
			for(int j=0; j<cuantos; j++){
				if(torneo[act]=='P'){
					torneo.push_back('P');
					torneo.push_back('R');
				}
				if(torneo[act]=='R'){
					torneo.push_back('R');
					torneo.push_back('S');
				}
				if(torneo[act]=='S'){
					torneo.push_back('P');
					torneo.push_back('S');
				}
				act++;
			}
			cuantos *= 2;
		}
		int actP = 0;
		int actR = 0;
		int actS = 0;
		for(int i=(1<<N)-1; i<(int)torneo.size(); i++){
			if(torneo[i]=='P')actP++;
			if(torneo[i]=='R')actR++;
			if(torneo[i]=='S')actS++;
		}
		
		
		if(actP==P&&actR==R&&actS==S){
			vector<char> act(1<<N);
			copy(torneo.begin()+(1<<N)-1,torneo.end(), act.begin());
			misort(act,0,act.size());
			res = act;
			hay = true;
		}
		
		
		torneo.clear();
		torneo.push_back('R');
		act = 0;
		cuantos = 1;
		for(int i=0; i<N; i++){
			for(int j=0; j<cuantos; j++){
				if(torneo[act]=='P'){
					torneo.push_back('P');
					torneo.push_back('R');
				}
				if(torneo[act]=='R'){
					torneo.push_back('R');
					torneo.push_back('S');
				}
				if(torneo[act]=='S'){
					torneo.push_back('P');
					torneo.push_back('S');
				}
				act++;
			}
			cuantos *= 2;
		}
		actP = 0;
		actR = 0;
		actS = 0;
		for(int i=(1<<N)-1; i<(int)torneo.size(); i++){
			if(torneo[i]=='P')actP++;
			if(torneo[i]=='R')actR++;
			if(torneo[i]=='S')actS++;
		}
		if(actP==P&&actR==R&&actS==S){
			vector<char> act(1<<N);
			copy(torneo.begin()+(1<<N)-1,torneo.end(), act.begin());
			misort(act,0,act.size());
			if(hay){
				res = min(res,act);
			}else{
				res = act;
			}
			hay = true;
			
		}
		
		
		
		torneo.clear();
		torneo.push_back('S');
		act = 0;
		cuantos = 1;
		for(int i=0; i<N; i++){
			for(int j=0; j<cuantos; j++){
				if(torneo[act]=='P'){
					torneo.push_back('P');
					torneo.push_back('R');
				}
				if(torneo[act]=='R'){
					torneo.push_back('R');
					torneo.push_back('S');
				}
				if(torneo[act]=='S'){
					torneo.push_back('P');
					torneo.push_back('S');
				}
				act++;
			}
			cuantos *= 2;
		}
		actP = 0;
		actR = 0;
		actS = 0;
		for(int i=(1<<N)-1; i<(int)torneo.size(); i++){
			if(torneo[i]=='P')actP++;
			if(torneo[i]=='R')actR++;
			if(torneo[i]=='S')actS++;
		}
		if(actP==P&&actR==R&&actS==S){
			vector<char> act(1<<N);
			copy(torneo.begin()+(1<<N)-1,torneo.end(), act.begin());
			misort(act,0,act.size());
			if(hay){
				res = min(res,act);
			}else{
				res = act;
			}
			hay = true;
		}
		
		
		
		
		
		cout << "Case #" << caso << ": ";
		if(hay){
			for(int i=0; i<(int)res.size(); i++){
				cout << res[i];
			}
			cout << endl;
		}else{
			cout << "IMPOSSIBLE" << endl; 
		}
		
	}
	
	return 0;
}
