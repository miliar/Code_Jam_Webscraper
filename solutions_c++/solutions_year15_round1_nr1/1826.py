#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <algorithm>
using namespace std;

int x[1111];
int main() {
	int t;
	cin>>t;
for(int i=1;i<=t;i++){
		int n;
		cin>>n;
		for(int i=1;i<=n;i++)cin>>x[i];
		int y=0;
	for(int i=2;i<=n;i++){
		if(x[i-1]>x[i])y=y+(x[i-1]-x[i]);
	}
	int max=0;
	for(int i=2;i<=n;i++){
		if(x[i-1]>x[i]){
			int mm=(x[i-1]-x[i]);
			if(mm>max)max=mm;
		}
	}
	int z=0;
	for(int i=1;i<n;i++){
		if(x[i]>=max)z=z+max;
		else z=z+x[i];
	}
		cout<<"Case #"<<i<<": "<<y<<" "<<z<<endl;
	
}
	return 0;
}

