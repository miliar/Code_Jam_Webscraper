#include <iostream>
#include <math.h>
#include <stdio.h>
#include <algorithm>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int ty=0;ty<t;ty++){
		int n;
		cin>>n;
		double a[n],b[n];
		for(int i=0;i<n;i++){
			cin>>a[i];
		}
		for(int i=0;i<n;i++){
			cin>>b[i];
		}
		sort(a,a+n);
		sort(b,b+n);
		int count1,count2;
		int i=0,j=0;
		while(true){
			if(j==n){
				count1=i;
				break;
			}
			if(b[i]<a[j]){
				i++;
				j++;
			}
			else j++;
		}
		i=0,j=0;
		while(true){
			if(j==n){
				count2=n-i;
				break;
			}
			if(a[i]<b[j]){
				i++;
				j++;
			}
			else j++;
		}
		cout<<"Case #"<<ty+1<<": "<<count1<<" "<<count2<<endl;
	}
}
