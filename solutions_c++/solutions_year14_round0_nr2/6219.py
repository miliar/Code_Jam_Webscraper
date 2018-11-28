#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

#define reps(i,f,n) for(int i=f;i<int(n);i++)
#define rep(i,n) reps(i,0,n)

int main(){
	int T;
	cin>>T;
	
	reps(t,1,T+1){
		double c,f,x;
		cin>>c>>f>>x;
		
		double time = 0;
		double ans = 100000;
		double speed = 2;
		while(1){
			double tm_end = time + x/speed;
			if(tm_end>=ans)break;
			ans = tm_end;
			
			double tm_cost = c/speed;
			time += tm_cost;
			speed += f;
		}
		
		printf("Case #%d: %.10lf\n",t,ans);
	}
}