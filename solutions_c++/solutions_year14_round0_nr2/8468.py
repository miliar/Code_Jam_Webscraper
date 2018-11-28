#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
double c,f,x;
int t,l=0;
cin>>t;
while(t--){
l++;
cin>>c;
cin>>f;
cin>>x;
double i=2.0;
double prev=0, current, prevsum=c/i;
current=x/i;
i+=f;
bool first=true;
do {
//cout<<prevsum<<endl;
prev=current;
//cout<<x/i<<endl;
current=prevsum+x/i;
prevsum+=c/i;
i+=f;
//cout<<current<<endl<<endl;
} while(current<prev);
cout<<"Case #"<<l<<": ";
printf("%.7lf\n", prev);
}
return 0;
}
