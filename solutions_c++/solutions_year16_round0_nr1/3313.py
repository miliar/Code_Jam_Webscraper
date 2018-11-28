#include <bits/stdc++.h>
#define lli long long 
using namespace std;
int m, ress = 0,t,counts=0,tt=0;
lli n;
void funcss(lli n,int *arr){
while (n){
if (arr[n % 10] == 0){
arr[n % 10] = 1;
counts++;
}
n = n / 10;
}
return;
}
int main(){
cin >> t;
while (t--){
tt++;
int arr[10];
memset(arr, 0, sizeof arr);
counts = 0;
cin>>n;
if (n == 0){
cout<<"Case #"<<tt<<": INSOMNIA\n";
continue;
}
lli var1 = n;
while (1){
funcss(n, arr);
if (counts == 10)
break;
n += var1;
}
cout<<"Case #"<<tt<<": "<<n<<endl;
}
return 0;
}
