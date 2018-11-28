#include<iostream>
#include<math.h>
using namespace std;
int main(){
int t;
cin>>t;
for(int f=0;f<t;f++){
long a,b;
cin>>a>>b;
long count=(sqrt((2*a-1)*(2*a-1)+8*(b))-2*a+1)/4;
cout<<"Case #"<<f+1<<": "<<count<<endl;
}
return 0;
}
