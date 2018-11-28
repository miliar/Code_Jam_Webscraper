#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<algorithm>
#include<math.h>
#include <iomanip>
using namespace std;
int main(){
int t,v=1;

cin>>t;
while(t--){
int a,b,k;
long long int ans=0;
cin>>a>>b>>k;
for(int i=0;i<a;i++){
	for(int j=0;j<b;j++){
	//	cout<<(i&j)<<" ";
		if((i&j)<k)
		ans++;
	}
}
cout<<"Case #"<<v<<": "<<ans<<endl;
ans=0;
v++;
}

system("pause");
  return 0;
}

