#include<stdio.h>
#include<iostream>
#include<algorithm>
#include <string.h>
#include <math.h>


using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,x=0;
	cin>>t;
	while (x<t) {
		
	
	
	int n,a[10001],sum =0,sum1 =0,max,i,j,ans;
	cin>>n;
	for(i = 0 ;i < n ;i++) {
		cin>>a[i];
	}
	for(i = 0; i < n -1 ;i++) {
		if(a[i+1] < a[i]) {
			sum =  sum + a[i] - a[i+1];
		}
	}
max= 0;
	for(i = 0 ;i < n -1;i++  ) {
		if(a[i+1] < a[i]) {
			ans = a[i] -a[i+1];
			if(ans > max) {
				max = ans;
			}
		}
	}
	//cout<<max<<"l";
	for(i = 0; i < n-1 ;i++) {
		if(a[i] <= max) {
			sum1 = sum1 + a[i];
		}
		else {
			sum1 = sum1 + max;
		}
	}
	
	cout<<"Case"<<" "<<"#"<<x+1<<":"<<" "<<sum<<" "<<sum1<<endl;
	

x++;

}

return 0;
}

