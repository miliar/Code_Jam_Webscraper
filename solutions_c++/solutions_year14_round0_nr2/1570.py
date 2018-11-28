#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)
#define pb push_back
#define db if(1)
#define ln puts("")

double c,f,x;

bool read(){
	scanf("%lf%lf%lf", &c, &f, &x);
	
	return true;
}

int cn = 1;

void process(){
	double elapsed = 0;
	double prod = 2;
	double res = 1e50;
	
	while(elapsed + x/prod < res){
		res = elapsed + x/prod;
		elapsed += c/prod;
		prod += f;
	}
	

	printf("Case #%d: %.07lf\n", cn++, res);

	
}

int main(){
	int t;
	scanf("%d", &t);
	
	while(t-- && read()) process();
	
	return 0;
}


