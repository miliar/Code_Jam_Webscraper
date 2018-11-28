#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void Solution(){
	int x[4][4], y[4][4];
	int rx, ry;
	cin>>rx;rx--;
	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++){
		cin>>x[i][j];
	}
	cin>>ry;ry--;
	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++){
		cin>>y[i][j];
	}
	
	int ans, an = 0;
	
	for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++){
		if(x[rx][i] == y[ry][j]){
			ans = x[rx][i];
			an++;
		}
	}
	if(an == 0)cout<<"Volunteer cheated!"<<endl;
	else if(an == 1)cout<<ans<<endl;
	else cout<<"Bad magician!"<<endl;
}

int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t;
	cin>>t;
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		Solution();
	}
	return 0;
}
