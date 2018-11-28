#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
 int p;
char a[1008];
int main(){
int t,h,i;
int x = 1;
int y;
cin>>t;
while(t--){
cin>>p;
cin>>a;
h = 0;
y = 0;
for(i = 1; i <= p;i++){
h = h + (a[i-1] - 48);
if(h < i){
	y = max(y, i - h);
}
}
cout<<"Case #"<<x<<": "<<y<<endl;
x++;
}
}
