#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <utility>
#include <cstdio>
#include <string>
using namespace std;

int main() {
	int t;
	cin>>t;
	for (int ulu= 1; ulu<=t; ulu++){
		int n;
		cin>>n;
		long long int a[n];
		for (int i=0; i<n; i++){
			cin>>a[i];
		}
		long long int ansfirst= 0;
		for (int i=0; i<n-1; i++){
			if (a[i+1]<a[i]){
				ansfirst+=a[i]-a[i+1];
			}
		}
		long long int test= 0;
		for (int i=1; i<n; i++){
			if (a[i]<a[i-1]){
				test= max(test, a[i-1]-a[i]);
			}
		}
		long long int anstest= 0, curr= a[0];
		bool check= 1; 
		for (int i=1; i<n; i++){
			if (curr-test>a[i]){
				check= 0;
				break;
			}
			else{
				if (curr-test<0){
					anstest+=curr;
				} 
				else{
					anstest+=test;
				}
				curr= a[i];
				
			}
			
			
		}

	
		cout<<"Case #"<<ulu<<": "<<ansfirst<<" "<<anstest<<endl;

	}
	return 0;
}