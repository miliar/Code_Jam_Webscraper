#include<iostream> 
#include<climits> 
using namespace std; 

int arr[1000]; 

int test(int a, int x)
 { if(a%x==0) return a/x-1;  return a/x; } 

 int main() 
 { 
 	int T,D,k=1,res;
 	cin>>T; 
 	while(T--) 
 	{ cin>>D; 
 			int m=0;
 			for(int i=0;i<D;i++) 
 			{ 
 				cin>>arr[i]; 
 				m=max(arr[i],m);
 			} 
 			
 			res=INT_MAX; 
 			for(int x=1;x<=m;x++) 
 			{ 
 				int y=x; 
 				 for(int i=0;i<D;i++) 
 				 	if(arr[i]>x) 
 				 		y+=test(arr[i],x); 
 				 	res=min(res,y);
 			} 
 		cout<<"Case #"<<k<<": "<<res<<endl; 
 		k++;
 	} return 0; 
 }