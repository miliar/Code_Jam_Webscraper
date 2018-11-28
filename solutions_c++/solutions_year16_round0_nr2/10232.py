#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

int main()
{
    int n,x[1000],y[1000],R[1000],st[1000]={0},i,j,max,count=0,k;
    cin>>n;
    for(i=0;i<n;i++) cin>>x[i]>>y[i]>>R[i];
    while(1){
    	for(i=0;i<n;i++) st[i]=0;
	    for(i=0;i<n;i++){
    		if(x[i]!=-999 && y[i]!=-999){
    			for(j=i+1;j<n;j++){
    				if(x[j]!=-999 && y[j]!=-999){
    					if(abs(R[i]-R[j]) <= sqrt(pow((x[i]-x[j]),2)+pow((y[i]-y[j]),2)) && 	sqrt(pow((x[i]-x[j]),2)+pow((y[i]-y[j]),2)) <= abs(R[i]+R[j])){
    						st[i]++;
    						st[j]++;
    					}
    				}
    			}
    		}
    	}
  	//	for(i=0;i<n;i++) cout<<st[i]<<endl;
    	max=0;
    	for(i=0;i<n;i++) if(st[i]>max) { max=st[i]; k=i; }
    	if(max==0) break;
    //	cout<<max;
    	count++;
    	x[k]=-999;
    	y[k]=-999;
    	R[k]=0;
    //	cout<<endl<<endl;
    }
    cout<<count;
    return 0;
}
