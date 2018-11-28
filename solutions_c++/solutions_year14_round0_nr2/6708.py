#include <iostream>
#include<cstdio>
using namespace std;

int main() {
	int t,i=1;
    double c,f,x,t1,t2,f1,f2;
    cin>>t;
    while(t--){
     cin>>c>>f>>x;
     t1=x/2;
     f1=2+f;
     f2=f1;
     t2=(c/2)+(x/f1);
     while(t1>=t2){
      t1=t2;
      t2=t2+(c/f1)-(x/f1);
      f1=f1+f; 
      t2=t2+(x/f1);
     } 
      printf("Case #%d: %0.7lf\n",i++,t1);
    }
	return 0;
}
