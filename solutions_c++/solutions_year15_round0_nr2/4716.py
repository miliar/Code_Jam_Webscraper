#include<bits/stdc++.h>
#include <cstdio>  
#include <cstring>  
#include <algorithm>  
#include<iostream>
using namespace std ;  
int main()
{
int test,n,x1,i,K;
	cin>>test;
	for(x1=0;x1<test;x1++){
		
		cin>>n;
		int arr[n];
		for(K=0;K<n;K++)
		 
		 cin>>arr[K];
		int cdef=arr[0];
		K=1;
		while(K<n){
			if(arr[K]>cdef)cdef=arr[K];
			K++;
		}
		int sw=cdef,s;
		for(i=1;i<cdef+1;i++){
			s=i;
			for(K=0;K<n;K++){
				if(arr[K]>i){
					if(arr[K]%i==0)
						s+=((arr[K]/i)-1);
					else 
						s+=arr[K]/i;
				}
			}
			sw=min(sw,s);	
		}
		int r=sw;
		printf("Case #%d: %d\n",x1+1,r);
	}

	return 0;
}
