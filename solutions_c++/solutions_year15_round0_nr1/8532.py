#include <stdio.h>
#include <string>
#include <iostream>
#include <math.h>

using namespace std;

int main(){
	int n;
	scanf("%d",&n);

	for(int i=0;i<n;i++){
		int m,ret=0,now=0;
		scanf("%d",&m);
		string str;
		cin>>str;
		for(int j=0;j<=m;j++){
			int k = str[j]-'0';
			ret += max(j-now,0);
			now = max(j,now);
			now += k;
		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
}