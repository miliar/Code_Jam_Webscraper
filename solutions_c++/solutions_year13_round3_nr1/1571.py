#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int ifsat(char s[],int i,int n,int l){
    int j1,j,k,count,netcounter=0;
	j1=i;
    for(j=j1;j<=l-n;j++){
        count=0;
		while( (s[j]=='a' || s[j]=='e' || s[j]=='i' || s[j]=='o' || s[j]=='u') && j<=l-n){
			j++;		
		}
		count++;
		k=j+1;
		while(k<=j+n-1){
			if( s[k]!='a' && s[k]!='e' && s[k]!='i' && s[k]!='o' && s[k]!='u')
				count++;
			else
				break;
		k++;
		}
	
		if(count==n){
			netcounter++;
			netcounter+=l-k;
			break;
		}
	}
    return(netcounter);
}

int main(){
    int t,n,l,counter;
    char s[1003];
    scanf("%d",&t);
    for(int i1=1;i1<=t;i1++){
        counter =0;
        scanf("%s",s);
        scanf("%d",&n);
        l=strlen(s);
        for(int i=0;i<=l-n;i++){
           counter += ifsat(s,i,n,l);            
        }
        printf("Case #%d: %d\n",i1,counter);
        
    }
    return 0;
}