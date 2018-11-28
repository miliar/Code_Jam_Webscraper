#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<string.h>
#include<limits.h>
#include<functional>
#include<vector>
#include<utility>
#include<stdlib.h>
#include<time.h>
using namespace std;

#define mem(a) memset(a,0,sizeof(a))
int a[11];

bool update(long long int n) {
	while(n>0) {
		int k = n%10;
		a[k] = 1;
		n/=10;
	}
	for(int i=0;i<10;i++){
		if(a[i]==0){
			return false;
		}
	}
	return true;
}

int main() {
	// your code goes here
	long long tc;
	cin>>tc;
	long long int n;
	for(int c=1;c<=tc;c++) {
		cin>>n;
		if(n == 0) {
		    cout<<"Case #"<<c<<": INSOMNIA"<<endl;
		    continue;
		}
		
		mem(a);
		bool complete = false;
		long long int i=0;
		while(!complete) {
			i++;
			complete = update(n*i);
		}
		cout<<"Case #"<<c<<": "<<n*i<<endl;
		
	}
	return 0;
}
