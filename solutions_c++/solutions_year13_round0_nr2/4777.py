#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>

using namespace std;

int testcase,n,m;

int ar[100][100];
int rmax[100],cmax[100];

int main(){
	
	scanf("%d\n",&testcase);
	int tc;
	for(tc=1;tc<=testcase;tc++){
		for(int i=0; i<100 ; i++){
			for(int j=0;j<100;j++){
				ar[i][j]=0;
			}
			rmax[i]=0;
			cmax[i]=0;
		}
		
		scanf("%d %d\n",&n,&m);
		
		for(int i =0 ; i<n; i++){
			for(int j =0 ; j<m; j++){
				cin>>ar[i][j];
				if(ar[i][j]>rmax[i]) rmax[i]= ar[i][j];
				if(ar[i][j]>cmax[j]) cmax[j] = ar[i][j];
			}
		}
		
		int yes = 0;
		
		for(int i =0 ; i<n; i++){
			for(int j =0 ; j<m; j++){
				if(ar[i][j]==rmax[i] || ar[i][j]==cmax[j]) yes++;
			}
		}
		
		cout<< "Case #" << tc << ": ";
		if(yes==n*m){
			cout <<"YES"<<endl;
		}else cout << "NO" <<endl;
		
	}
		
	return 0;
}