# include <stdio.h>

# define mi(x,y) (x<y ? x : y)

double ans, C, F, X, income, money;
int t;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d",&t);
	
	for(int ii=0; ii<t; ii++){
		scanf("%lf %lf %lf",&C,&F,&X);
		
		income = 2;
		ans = X/income;
		money = 0;
		double tm = 0;
		
		while(tm < ans){
			//printf("money = %lf   income =  %lf   time = %lf\n",money,income,tm);
			double needC = (C-money)/income;
			double needX = (X-money)/income;
			
			ans = mi(ans, needX + tm);
			
			tm += needC;
			money += needC*income;
			
			money -= C;
			income += F;
		}
		
		printf("Case #%d: %.7lf\n",ii+1,ans);
		
		getchar();
	}
}
