#include<iostream>
using namespace std;

int get_z(const double *she,const double *he,int n);
int get_y(const double *she,const double *he,int n);
int sign(double i){if(i>0)return 1;if(i==0)return 0;if(i<0)return -1;}
int comp(const void*a,const void*b){return sign(*(double*)a-*(double*)b);}//from small to large;

int main(){
	double she[1000];
	double he[1000];
	int n,i;
	int t,j;
	cin>>t;
	for(j=1;j<=t;j++){
		cin>>n;
		for(i=0;i<n;i++)cin>>she[i];
		for(i=0;i<n;i++)cin>>he[i];
		qsort(she,n,sizeof(double),comp);
		qsort(he,n,sizeof(double),comp);
		printf("Case #%d: %d %d\n",j,get_y(she,he,n),get_z(she,he,n));
	}
	return 0;
}

int get_y(const double *she,const double *he,int n){
	int i;
	int num=0;
	int max=n-1,min=0;
	for(i=0;i<n;i++){
		if(she[i]>he[min]){num++;min++;}
		else max--;
	}
	return num;
}

int get_z(const double *she,const double *he,int n){
	int i;
	int num=0;
	int max=n-1,min=0;
	for(i=n-1;i>=0;i--){
		if(she[i]>he[max]){num++;min++;}
		else max--;
	}
	return num;
}