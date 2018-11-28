#include<bits/stdc++.h>

using namespace std;

double c, f, x;

double solve(int farm){
	double tot=0.0;
	while(1){
		if(x/(2.0+(f*farm)) < c/(2.0+(f*farm))+x/(2.0+(f*(farm+1)))){
			tot +=  x/(2.0+(f*farm));
			break;
		}
		else{
			tot += c/(2.0+(f*farm));
			farm++;
		}
	}
	return tot;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, t=0;
	cin >> T;
	while(T--){
		cin >> c >> f >> x;
		printf("Case #%d: %.8lf\n", ++t, solve(0));
		
	}
	return 0;
}
