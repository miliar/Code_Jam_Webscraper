#include<iostream>
#include<cstdio>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{ 
    int t,i,j,k,l,m,n,a,b;
    double arr[1005],arr1[1005],arr2[1005],arr3[1005];
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    m=t;
    while(t--)
    {
        a=0;
        b=0;
		cin>>n;
		for(i=0;i<n;i++) 
            cin>>arr[i];
		for(i=0;i<n;i++) 
            cin>>arr1[i];
		sort(arr,arr+n);
		sort(arr1,arr1+n);
		for(i=0;i<n;i++) 
		  arr2[i]=arr1[i];
		  for(i=0;i<n;i++) 
		  arr3[i]=arr[i];
		/*for(i=0;i<n;i++) 
            cout<<arr[i];
		for(i=0;i<n;i++) 
            cout<<arr1[i];
            for(i=0;i<n;i++) 
            cout<<arr2[i];*/
        for(i=0;i<n;i++)
        {
			for(j=0;j<n;j++)
            {
				if(arr2[i]>arr[j]&&arr[j]>-1)
                {
					arr[j]=-5;
					a++;
					break;
				}
			}
		}
		//for(i=0;i<n;i++) 
         //   cout<<arr2[i]<<" ";
		
		for(i=0;i<n;i++)
        {
			for(j=0;j<n;j++)
            {
				if(arr3[i]>arr1[j]&&arr1[j]>-1)
                {
					arr1[j]=-5;
					b++;
					break;
				}
			}
		}
	
		cout<<"Case #"<<m-t<<": "<<b<<" "<<n-a<<endl;
    }
    return 0;
}
