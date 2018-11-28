#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <memory.h>
#include <math.h>
#define eps 0.000001
using namespace std;


vector<double> p1;
vector<double> p2;
void read(){
	int n;
	scanf("%d",&n);
	
	for(int i= 0 ;i < n; i++){
		double x;
		scanf("%lf",&x);
		p1.push_back(x);
	}

	for(int i = 0; i < n; i++){
		double x;
		scanf("%lf",&x);
		p2.push_back(x);
	}

	sort(p1.begin(),p1.end());
	sort(p2.begin(),p2.end());
}

void debug(const vector<double> v){
	for(int i= 0;i < v.size(); i++){
		cout << v[i] << " ";
	}
	cout << endl;
}


int findWar(){
	int p1Last = p1.size()-1;
	int p2Last = p2.size()-1;
	int p2First = 0;
	int len = p1.size();
	int cnt =0;
	for(int i =0 ; i < len; i++){
		if(p1[p1Last] + eps  > p2[p2Last]){
			p2First++;
			p1Last--;
			cnt++;
		}else{
			p2Last--;
			p1Last--;		
		}
	}
	cout << cnt  <<endl;
}

int cnt;
int maxDW =-1;
int len;
int dp[5000][5000];
int maskP1,maskP2;
int maxV = -1;
int getMax(int a,int b){
	return (a>b)?a:b;
}
int dWar(int k, int maskP1, int maskP2){
	if(k == 0){
		return dp[maskP1][maskP2] = 0;
	}
	if(dp[maskP1][maskP2] != -1){
		return dp[maskP1][maskP2];
	}

	for(int i = 0; i < len; i++){
		if((maskP1 & (1<<i))){
			for (int j = 0; j < len; j++){
				if((maskP2 & (1<<j))){ 
					int val =0;
					if(p1[len-i-1] +eps > p2[len-j-1])
						val = 1;
					dp[maskP1][maskP2] = getMax(dp[maskP1][maskP2],val + dWar(k-1,maskP1 & ~(1<<i) ,maskP2 & ~(1<<j)));
				}
			}
		}
	}
	return dp[maskP1][maskP2];

}

int main(){
	int T;
	scanf("%d",&T);

	for(int i =0 ; i < T ;i++){
		p1.clear();
		p2.clear();
		maskP1 = maskP2 = 0;
		memset(dp,-1,sizeof dp);
		maxDW = -1;
		cnt =0;
		read();
		cout << "Case #" << (i+1) <<": ";
		len = p1.size();
		cout << dWar(len, (1<<len)-1, (1<<len)-1) << " ";
		findWar();
	}


	return 0;
}