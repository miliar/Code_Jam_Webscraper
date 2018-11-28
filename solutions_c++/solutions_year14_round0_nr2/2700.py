#include<cstdio>

#define For(Q,W) for(int Q=0; Q<W; Q++)

int main(){
	int t;
	scanf("%d ",&t);
	For(test,t){
		double c,f,x;
		scanf("%lf %lf %lf ",&c,&f,&x);
		
		double t=0;
		double prod =2;
		while(true){
			if( (x)/(prod+f) + c/prod < x/prod ){
				t+= c/prod;
				prod+=f;
			}
			else{
				printf("Case #%d: %.10lf\n",test+1,x/prod+t);
				break;
			}
		}
	}
}
