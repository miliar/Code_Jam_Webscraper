#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
bool x[10];
void f(int n){
   int r;
   while (n!=0){
     r=n%10;
	 x[r]=1;
	 n/=10;}}
bool f1(){
   int c=0;
   for (int i=0;i<10;i++){
      if (x[i])c++;}
   if (c==10)return true;
   return false;}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i=1;i<=t;i++){
	   int n;
	   cin >> n;
	   cout << "Case #" << i << ": ";
	   if (n==0){cout << "INSOMNIA" << endl;}
	   else if (n==1){cout << 10 << endl;}
	   else {
	      int r=n;
		  f(r);
		  while (true){
		    r+=n;
	        f(r);
			if (f1()){cout << r << endl;break;}}
	   for (int i=0;i<10;i++){x[i]=0;}
	   }
	
	}

return 0;
}