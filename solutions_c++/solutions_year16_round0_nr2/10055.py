#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int i;
	for(i=1;i<=t;i++){
	    char c[100];
	    scanf("%s",c);
	    int l=strlen(c);
	    int k=0;
	    int j;
	    if(c[0]=='-'){
	            k++;
	        }
	    for(j=0;j<l-1;j++){
	        
	        if(c[j]!=c[j+1] && c[j]=='+'){
	            k+=2;
	        }
	    }
	    if(l==1 && c[0]=='-')
	        k=1;
	    cout<<"Case #"<<i<<": "<<k<<endl;
	    
	}
	return 0;
}
