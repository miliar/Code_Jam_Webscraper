#include<stdio.h>
#include<algorithm>
using namespace std;
double tr[1000],tx[1000];
double r[1000],x[1000];
double avai[1000];
double fill[1000];
int ind[1000];
int n;
double gv,gx;
int cmp(int a,int b){
	return tx[a]>tx[b];
}
int check(double time){
	double max_x = 0,min_x = 0, left;
	double sum = 0;
	for(int i = 0 ; i < n ; i++ ){
		avai[i] = time*r[i];
		sum += avai[i];
	}
	int chk = 1;
	if( sum < gv ){chk = 0; }

	left = gv;
	for(int i = 0 ; i < n ; i++ ){
		if( left > avai[i] ){
			left-=avai[i];
			max_x+=avai[i]*x[i];
		}else{
			max_x+=left*x[i];
			left = 0;
		}
	}
	max_x/=gv;
	//if( left != 0 ) chk = 0;

	left = gv;
	for(int i = n-1 ; i>=0 ; i-- ){
		if( left > avai[i] ){
			left-=avai[i];
			min_x+=avai[i]*x[i];
		}else{
			min_x+=left*x[i];
			left = 0;
		}
	}
	min_x/=gv;

	if( max_x >= gx-0.0000000001 && min_x <= gx+0.0000000001 );
	else{ chk = 0; 
	//printf("%.9lf %.9lf t %lf\n",max_x,min_x,time); 
	}

	return chk;
}
int main(){
	int t;
	scanf("%d",&t);
	for(int e = 0 ; e< t; e++ ){
		scanf("%d %lf %lf",&n,&gv,&gx);
		//printf("%d %lf %lf\n",n,gv,gx);
		for(int i = 0 ; i < n ;i++){
			scanf("%lf %lf",&tr[i],&tx[i]);
			//printf("%lf %lf\n",tr[i],tx[i]);	
			ind[i] = i;
		}

		printf("Case #%d: ",e+1);
		sort(ind,ind+n,cmp);
		for(int i = 0 ;i < n ; i++ ){
			r[i] = tr[ind[i]];
			x[i] = tx[ind[i]];
		}
		double minr = r[0];
		for(int i = 0 ; i < n ; i++ ){
			minr = min(minr,r[i]);
		}
	
		int cc = 0;
		for(int i = 0 ; i < n ; i++ ){
			if( x[i] >= gx ) cc|=2;
			if( x[i] <= gx ) cc|=1;
		}
		if( cc != 3 ){
			printf("IMPOSSIBLE\n");
			continue;
		}


		double first = 0 , last = gv/minr;
		for(; ;){
			double time=(last+first)/2;
			//printf("%lf\n",time);
			if( (last-first)/time < 0.0000000001 ) break;
			int chk = check(time);
			if( chk == 0 ){
				first = time;
			}else{
				last = time;
			}
		}
		printf("%.9lf\n",first);
	}
}
