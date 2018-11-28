#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int n;
int ans2[1001];
int ans1[1001];

bool myfunction(double a, double b){
return a>b?true:false;
}
/*
void printarrays(){
int i;
for(i=0;i<n;i++);
		cout<<arrnaomi[i]<<" ";
		
cout<<endl;
for(i=0;i<n;i++)
		cout<<arrken[i]<<" ";
		
cout<<endl;

}
*/
int main(){
double arrnaomi[1000];
double arrken[1000];
int t,caseno=1,temp,i,j;
scanf("%d",&t);
while(caseno<=t){
	scanf("%d",&n);
	for(i=0;i<n;i++)
		scanf("%lf",&arrnaomi[i]);
	for(i=0;i<n;i++)
		scanf("%lf",&arrken[i]);
		
	//	printarrays();
//input taken 
	sort(arrnaomi,arrnaomi+n,myfunction);
	sort(arrken,arrken+n,myfunction);
//sorting done
	//printarrays();
	j=n-1;
	temp=0;
	for(i=n-1;i>=0;i--){
		for(;j>=0;j--){	
			if(arrken[j]>arrnaomi[i]){
				temp++;
				//cout<<arrnaomi[i]<<endl;
				j--;
				break;
			}
		}
		if(j==-1)
			break;
	}	
	ans2[caseno]=n-temp;
	j=n-1;
	temp=0;
	for(i=n-1;i>=0;i--){
		for(;j>=0;j--){
			if(arrnaomi[j]>arrken[i]){
				temp++;
				j--;
				//cout<<arrken[i]<<endl;
				break;
			}
		}
		if(j==-1)
			break;
	}
	ans1[caseno]=temp;			
caseno++;
}
for(i=1;i<=t;i++)
	printf("Case #%d: %d %d\n",i,ans1[i],ans2[i]);
	
return 0;
}
