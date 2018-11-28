#include<stdio.h>
#include<conio.h>
//double calc(double c,double f,double x,double curr,double time){
//	printf("%lf %lf %lf %lf\n",c,f,x,curr);
//	//if(curr == f+2)return  (x/curr);
//	double d1 = time + x/curr;
//	double d2 = time + c/curr + x/(curr+f);
//	printf("we will take %lf time with current speed and %lf time if farm bought\n",d1,d2);
////	getch();
//	if(d1<=d2)return d1;	
//	return calc(c,f,x,curr+f,time + c/curr);
//	
//}
double calc(double c,double f,double x,double curr,double time){
	
	while(1){
		double d1 = time + x/curr;
		double d2 = time + c/curr + x/(curr+f);
		if(d1+1e-10<=d2)return d1;
		time=time+c/curr;
		curr=curr+f;
	}
}
int main(){
	int t,h=1;	
	double c,f,x;
	scanf("%d",&t);
//	printf("%d",t);
	while(t--){
		scanf("%lf %lf %lf",&c,&f,&x);
		printf("Case #%d: ",h);
		printf("%.12lf\n",calc(c,f,x,2,0.0));
		h++;
	}
	return 0;

}
