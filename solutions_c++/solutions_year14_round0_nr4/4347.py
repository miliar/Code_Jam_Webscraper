#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<vector>
#include<map>
#include<list>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
	int kp,t,n,count1,count2=0,val;
	cin>>kp;
	for(int t=1;t<=kp;t++){
		cin>>n;
		double arr[n],brr[n];
		count1=count2=0;
		for(int i=0;i<n;i++)
			cin>>arr[i];
		for(int i=0;i<n;i++)
			cin>>brr[i];
		count1=count2=0;
		sort(arr,arr+n);
		sort(brr,brr+n);
		
		bool visited[n];
		for(int i=0;i<n;i++)
			visited[i]=false;
		int j;
		for(int i=0;i<n;i++){
			for( j=0;j<n;j++){
				if(arr[i]<brr[j] && visited[j]==false){
					visited[j]=true;
					//count2++;
					break;
				}
				
			}
			if(j>=n)
				count1++;
		}
		
		for(int i=0;i<n;i++)
			visited[i]=false;
		
		count2=0;
		for(int i=0;i<n;i++){
			for(int j=n-1;j>=0;j--){
				if(arr[i]>brr[j] && visited[j]==false){
					visited[j]=true;
					count2++;
					break;
					
				}
			}
		}
			
		cout<<"Case #"<<t<<": "<<count2<<" "<<count1<<endl;
		
	/*
		cout<<"---------------"<<endl;
		for(int i=0;i<n;i++)
			cout<<arr[i]<<" ";
			cout<<endl;
		
		cout<<"---------------"<<endl;
		for(int i=0;i<n;i++)
			cout<<brr[i]<<" ";
			cout<<endl;		
		*/
		
		
		
	}
	
	
	
	
	return 0;
}

