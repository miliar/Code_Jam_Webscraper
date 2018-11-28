#include <iostream>
#include<iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>
#include <fstream>
using namespace std;

//https://code.google.com/codejam/contest/351101/dashboard#s=p0
int main()
{

    freopen("B-large.in","r",stdin);
    freopen("out2.out","w",stdout);
int t,cs=1 ;
long double C,F,X,T1,T2,R ,S;
cin>>t ;
while(t--)
{
cin>>C>>F>>X ;
T1=X/2;
T2=X/2;
S=0 ;
R=2 ;
do
{
T1=T2;
S=S+C/R ;
R=R+F ;
T2=S+X/R ;
}while(T2<T1) ;
cout<<"Case #"<<cs<<": "<<fixed<<setprecision(7)<<T1<<endl ;
cs++ ;
}
return 0;
}
