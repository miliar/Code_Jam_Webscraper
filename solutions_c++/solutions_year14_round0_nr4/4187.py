#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<limits.h>
using namespace std;
bool cmp (const double &a,const double &b) {
	return a>b ;
}
int main(){
	int t;
	//freopen("D.in","r",stdin);
	cin>>t;
	int t2=0;
	//freopen("out.txt","w",stdout);
	while(t--){
		t2++;
		int n;
		double arr[1002];
		double brr[1002];
		cin>>n;
		for(int i= 0;i<n;i++)
		 cin>>arr[i];
		for(int i= 0;i<n;i++)
		 cin>>brr[i];
		 sort(arr,arr+n);
		 sort(brr,brr+n);
		 int i,j;
		 int count1=0,count2=0;
	   for(i=0,j=0;i<n&&j<n;)
	   {
	   	 // cout<<arr[i] <<" "<<brr[j]<<endl;
		  if(arr[i] > brr[j])
	        {
	        	j++;
	        }
	       else if(arr[i] < brr[j])
	        {
	        	count1++;
				i++;
	        	j++;
	        }
	    }
	    sort(brr,brr+n,cmp);
	    int s=0;
	   for(i=0,j=n-1;i<n&&j>=s;)
	   {
	   	//	 cout<<arr[i] <<" "<<brr[j]<<endl;
			   if(arr[i] > brr[j])
	   		  {
	   		  	count2++;
	   		  	i++;
	   		  	j--;
	   		  }
	   		else if(arr[i] < brr[j])
	   		{
	   			i++;
	   			s++;
	   		}
	   	}
	   	cout<<"Case #"<<t2<<":"<<" "<<count2<<" "<<n-count1<<endl;
	   }
}
	   			
	   			
	   			
	   		
	   		  	
	   		  	
	   		  	
	   
	   
	    
	        	
