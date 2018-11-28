#include<stdAfx.h>
#include <iostream>
#include <cmath>
#include <string>
#include <queue>
using namespace std;
int main()
{
//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
double C,F,X;
int n=1;
int tests;
cin>>tests;
for (int j=1; j<=tests; j++){
cin>>C>>F>>X;
double ans=100000000000;double ans1=2,ans2=0;
for (int n=1; n<100000; n++){
ans=min(ans,ans2+X/ans1);
ans2+=C/ans1;
ans1+=F;
}
cout.precision(7);
cout<<"Case #"<<j<<": "<<fixed<<ans<<endl;
}
cin>>n;
return 0;
}