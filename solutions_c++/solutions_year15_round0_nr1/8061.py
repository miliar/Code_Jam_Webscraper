#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {

int n,x,count=0,have=0;
string y;
freopen("A-large.in","r",stdin);
cin>>n;
for (int i=1;i<=n;i++){

	cin>>x;
	cin>>y;
	for (int j=0;j<x+1;j++){
	
	
	if (j>0){if (have<j &&(y[j]-48!=0)){count+=(j-have);
	have+=j-have;}}
	have+=(y[j]-48);

}
	freopen("A-large.out","a+",stdout);
	cout<<"Case #"<<i<<": "<<count<<endl;   

 
 count=0;
 have=0;
}

	return 0;
}
