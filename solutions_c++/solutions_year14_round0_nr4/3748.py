#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
float arr1[1002];
float arr2[1002];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int n,i,j,t,p,y,z,cnt,cntf;
	cin>>t;
	for(p=1;p<=t;p++)
	{
		cin>>n;
  		for(i=0;i<n;i++)
   			cin>>arr1[i];
   		for(i=0;i<n;i++)
    		cin>>arr2[i];
  		sort(arr1,arr1+n);
  		reverse(arr1,arr1+n);
  		sort(arr2,arr2+n);
  		reverse(arr2,arr2+n);

  		y=0,z=n-1,cnt=0;
  		j=0;
   		while(j<=z)
   		{
    		if(arr1[j]>arr2[y])
   			{
       			cnt++;
       			y++;
       			j++;
     		}
    		else if(arr1[j]<arr2[y])
     		{
     			z--;
       			y++;
     		}
   		}
   		cntf=0;
   		y=0;
   		z=n-1;
   		j=0;
   		while(j<=z)
   		{
      		if(arr1[y]>arr2[j])
      		{
        		cntf++;
        		y++;
        		z--;
      		}
      		else if(arr1[y]<arr2[j])
       		{
        	   j++;
        	   y++;
       		}
   		}
   		cout<<"Case #"<<p<<": "<<cnt<<" "<<cntf<<endl;
	}
	return 0;
}
