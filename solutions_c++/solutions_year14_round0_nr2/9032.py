#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;
int main(){
int t1;
cin>>t1;
for(int ty1=1;ty1<=t1;ty1++){
double c,f,x;
cin >> c >> f >> x ;
double cr=2;
double ans=c/2;
while(true){
if((x-c)/cr <= x/(cr+f)){
ans=ans+(x-c)/cr;
break;
}
else{
cr=cr+f;
ans=ans + (c/cr);
}
}
cout << "Case #" << ty1;
cout << ": ";
printf("%0.7f",ans);
cout << endl;
}
}
