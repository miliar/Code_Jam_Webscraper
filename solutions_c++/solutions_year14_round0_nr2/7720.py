#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
const int P = 1000000007;
int main(){
    int T,TT;
    cin>> T;
    TT=T;
    while (T--){
    	double C,F,X,FF;
    	scanf("%lf%lf%lf",&C,&F,&X);
    	FF=0;
    	int N=int(X)+1;
    	double mn=X/2,t=X/2;
    	for (int i=1;i<=N;i++){
    		t=t-X/(2+FF)+X/(2+FF+F)+C/(2+FF);
    		if (t<mn) mn=t;
    		FF+=F;
    	}
    	printf("Case #%d: %.8lf\n",TT-T,mn);
    	
    }
    return 0;
}
