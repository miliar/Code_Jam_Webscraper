#include<bits/stdc++.h>
using namespace std;
 int ans(int n,int a[]){
	int large = a[0];
	int p=0;
	for(int i=1;i<n;i++){
		if(a[i]>large){
			large=a[i];
			p = i;
		}
	}
	a[p]--;	
	return p;
}
 
int main(){
freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
    int t,n,i,pos;
    cin>>t;
    int p=1;
    while(t--){
       
        char s[27];int k,flag=0;
        for(i=0; i<26; i++){
            s[i]=char(i+65);
        }
       // for(i=0;i<26;i++)cout<<s[i];
        
        int a[10001], sum =0;
		
		cin>>n;
		for( i=0;i<n;i++){
			cin>>a[i];
			sum+= a[i];	
		}
       
        cout<<"Case #"<<p<<": ";
       for(i=0;i<sum;i++){
			//cout<<" ";
			pos= ans(n,a);
			//cout<<pos;
			cout<<s[pos];k++;
			if(sum%2!=0){if(i==sum-3) flag=1;}
			if(flag==1) {cout<<" ";flag=0;k=0;}
			if(k==2&&flag==0) {cout<<" ";k=0;}			
		}
	        cout<<"\n";
			p++;
    }
}
