#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

bool G[150][150];
int cnt=0;

void grid(string, string);
int solve(string, string);

int main(){
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		string a, b;
		cin >> a >> b;
		grid(a, b);
		int res = solve(a, b);
		printf("Case #%d: ", ++cnt);
		if(res != -1) printf("%d\n", res);	
		else printf("Fegla Won\n");
	}
	return 0;
}

void grid(string a, string b){
	for(int i=0; i<a.size(); ++i){
		for(int j=0; j<b.size(); ++j){
			G[i][j] = a[i] == b[j];
		}	
	}
}

int solve(string a, string b){
	int i=0;
	int j=0;
	int res=0;
	if(!G[i][j]) return -1;
	while(true){
		if(i+1<a.size() && j+1<b.size() && G[i+1][j+1]){
			i += 1;
			j += 1;
		}else if(i+1<a.size() && G[i+1][j]){
			i += 1;
			res++;
		}else if(j+1<b.size() && G[i][j+1]){
			j += 1;
			res++;
		}else{
			break;
		} 	
	}
	if(i==a.size()-1 && j==b.size()-1) return res;
	else return -1;
}
