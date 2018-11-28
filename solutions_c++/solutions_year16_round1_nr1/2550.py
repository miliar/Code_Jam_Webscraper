/*  sourav verma(Swerve7) IPG_2013108 ABV-IIITM,Gwalior
    Task @ Google Code JAM  */
  
   
#include <bits/stdc++.h>
using namespace std;
#define ll long long int
char s[1110],y[1110],ch;

int main() {
	int ts; cin>>ts;
	for(int t=1;t<=ts;t++){
		cin>>s; int mx=1000,l;
		l=strlen(s);
		y[mx]=s[0];
		for(int i=1;i<l;i++) {
			ch=s[i];
			if(y[mx]>ch) y[mx+i]=ch;
			else {
				y[mx-1]=ch; mx-=1;
			}
		}
		cout<<"Case #"<<t<<": ";
		for(int i=mx;i<mx+l;i++) cout<<y[i];
		cout<<"\n";
		
	}
	// your code goes here
	return 0;
}