#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;
const int INF=100000000;

double ans=INF;
int c;
double C,F,X;
void dfs(double time,int farm,double cookie){
	//cout << (X-cookie)/(2+farm*F)+time << endl;
	if(time>ans) return;
	if((X-cookie)/(2+farm*F)+time<ans){
		ans=(X-cookie)/(2+farm*F)+time;
		c=farm;
	}
	dfs(time+(C-cookie)/(2+farm*F),farm+1,0);
}

int main(){
	int T;
	cin >> T;
	for(int i=0; i<T; ++i){
		ans=INF;
		cin >> C >> F >> X;
		//dfs(0,0,0);
		double time,farm,cookie;
		time=farm=cookie=0;
		while(time<ans){
			if((X-cookie)/(2+farm*F)+time<ans){
				ans=(X-cookie)/(2+farm*F)+time;
				c=farm;
			}
			time=time+(C-cookie)/(2+farm*F);
			++farm;
			cookie=0;
		}
		cout << "Case #" << i+1 << ": ";
		printf("%.7f",ans);
		cout << endl;
	}
	return 0;
}
