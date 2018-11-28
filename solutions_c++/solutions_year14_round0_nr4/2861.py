#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void Solution(){
	int N;
	double x[1005], y[1005];
	cin>>N;
	for(int i = 0; i < N; i++)cin>>x[i];
	for(int i = 0; i < N; i++)cin>>y[i];
	
	sort(x, x + N);
	sort(y, y + N);
	
	int score;
	double *p;
	
	score = 0;
	p = &y[0];
	for(int i = 0; i < N; i++){
		if(x[i] > *p){
			p++;
			score++;
		}
	}
	cout<<score<<" ";
	
	score = 0;
	p = &x[0];
	for(int i = 0; i < N; i++){
		if(y[i] > *p){
			p++;
			score++;
		}
	}
	cout<<N - score<<endl;
	
}

int main(){
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int t;
	cin>>t;
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		Solution();
	}
	return 0;
}
