#include <bits/stdc++.h>
using namespace std;
char convert(char x){
if(x=='+') return '-';
else return '+';
}
int main() {
	// your code goes here
	long long t,i=1,n,s,j,p;
	string a;
	cin>>t;
	while(t--){
		s=0;
		cin>>a;
		a.erase(unique(a.begin(), a.end()), a.end());
		n=a.length();
		while(n>0){
			if(a[n-1]=='+'){
				n--;
			} 
			else{
				if(a[0]=='-'){
					for(j=0;j<n;j++)
		            a[j]=convert(a[j]);
		            for(j=0;j<n;j++)
		            a[j]=a[n-1-j];
		            s++;
		            n--;
		            
				}
				else{
					for(j=1;j<n;j++)
		            a[j]=convert(a[j]);
		            for(j=0;j<n-1;j++)
		            a[j]=a[n-1-j];
		            a[n-1]='+';
		            s=s+2;
		            n--;
		           
				}
				
			}
		}
		cout<<"Case #"<<i<<": "<<s<<endl;
		i++;
		
		}
	return 0;
}
