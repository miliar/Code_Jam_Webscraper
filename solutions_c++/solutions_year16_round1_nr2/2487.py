/*  sourav verma(Swerve7) IPG_2013108 ABV-IIITM,Gwalior
    Task @ Google Code JAM  */
  
   
#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main() {
	int ts; cin>>ts;
	for(int t=1;t<=ts;t++){
		int n,x,list[2515],xlist[57],k=0;
	    cin>>n;
	    memset(list,false,sizeof(list));
		for(int i=0;i<2*n-1;i++) {
			for(int j=0;j<n;j++){
				cin>>x; list[x]++;
			}
		}
		for(int i=0;i<2515;i++) {
			if(list[i] & 1) xlist[k++]=i;
		}
		cout<<"Case #"<<t<<": ";
		for(int i=0;i<n;i++) cout<<xlist[i]<<" ";
		cout<<"\n";
		
	}
	// your code goes here
	return 0;
}