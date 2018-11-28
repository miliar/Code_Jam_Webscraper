#include <iostream>
#include<algorithm>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
int main() {
	int i,j,k,x,y,count1,count2,t,n;
	cin>>t;
	int c=1;
	while(t--){
		
		count1=0;
		count2=0;
		cin>>n;
		float arr1[n],arr2[n];
		for(i=0;i<n;i++){
			cin>>arr1[i];
		}
		for(i=0;i<n;i++){
			cin>>arr2[i];
		}
		//war
		sort(arr1,arr1+n);
		sort(arr2,arr2+n);
		i=n-1;
		int k=n-1 ,j=0;
		while(j<=k){
		if(arr1[i]>arr2[k])
		{
			j++;
			count1++;
			i--;
		}
		else
		{
			i--;
			k--;
		}
	}
	
	int x=0,y=n-1;
	i=n-1;
	while(x<=y){ 
		if(arr1[y]>arr2[i]){
			i--;
			y--;
			count2++;
		}
		else{
			i--;
			x++;
		}
	}
		cout<<"Case#"<<c<<":"<<" "<<count2<<" "<<count1<<"\n";
		c++;
	}
	
	
	return 0;
}