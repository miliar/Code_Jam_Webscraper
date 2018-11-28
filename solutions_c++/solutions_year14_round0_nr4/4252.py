#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <vector>

using namespace std;

int main() {
	
	int tt,n,v;
	double na[1000+10],ke[1000+10];
	cin>>tt;
	
	for(int t = 1;t<=tt;t++){
		printf("Case #%d:",t);
		cin>>n;
		for(int i = 0;i<n;i++) cin>>na[i];
		for(int i = 0;i<n;i++) cin>>ke[i];
		sort(na,na+n);
		sort(ke,ke+n);
		
		int dw,w,i=0,j=0;
		dw = w = 0;
		while(i < n && j<n){
			if(na[i] > ke[j]){
				i++; j++; dw++;
			}else{i++;}
		}
		
		i=j=0;
		while(i < n && j<n){
			if(na[i] < ke[j]){
				i++; j++; w++;
			}else{j++;}
		}
		
		printf(" %d %d\n",dw,n-w);
	}
	
	return 0;
}