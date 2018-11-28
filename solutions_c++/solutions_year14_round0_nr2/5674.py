/*krypto..................................jagsxi...!! */


#include <bits/stdc++.h>


using namespace std;
int main()
{
 
int T;
double C,F,X;
 
cin>>T;
int t=1;
while(T--){
 
scanf("%lf %lf %lf",&C,&F,&X);
 
double res = 0;
double act = 2;
 
while(1){
 
double t1 = X/act;
double t2 = ( C / act )+( X / ( F+act ) );
 
if(t2 < t1 ){
res+=(C/act);
act+=F;
}
else
{
res+=X/act;
break;
}
 
}
printf("Case #%d: %.7lf\n",t,res);
t++;
 
}
 
return 0;
}