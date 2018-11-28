#include <cmath> 
#include <cstdio> 
#include <vector> 
#include <iostream> 
#include <algorithm> 
using namespace std; 
int main() { 
int t,i,u,p,l,x=0,f;
long long int n;
vector<long long int> A;
cin>> t;
while(t--){
	i=0;
f=1;
x++;
cin >> n;


if(n==0){
cout << "Case #"<<x<<": "<<"INSOMNIA"<<endl;
continue;
}
while(f){
i++;
u=i*n;
l=u;
while(u){
p=u%10;
u=u/10;
A.push_back(p);
}
sort(A.begin(),A.end());
A.erase(unique(A.begin(),A.end()),A.end());


if(A.size()==10){
f=0;
cout <<"Case #"<<x<<": "<<l<<endl;
}}

A.clear();
}

return 0; 
} 
