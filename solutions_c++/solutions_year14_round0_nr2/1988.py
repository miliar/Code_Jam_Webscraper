#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
double round( double value, int precision )
{
    const int adjustment = pow(10,precision);
    return floor( value*(adjustment) + 0.5 )/adjustment;
}

int main()
{
int T,i;

long double c,f,x,y,ans[102],prevtime,cps=2.0,newtime,fcost=0.0;
cin>>T;
for(i=0;i<T;i++)
{fcost=0.0;
cps=2.0;
	cin>>c>>f>>x;
prevtime=(x/cps);
newtime=((c/cps)+(x/(cps+f)));


while(prevtime>newtime){
fcost+=(c/cps);
cps+=f;
prevtime=newtime;
newtime=fcost+((c/cps)+(x/(cps+f)));

}
ans[i]=prevtime;

}

for(i=1;i<=T;i++){
cout<<"Case #"<<i<<": ";
printf("%.7Lf",ans[i-1]);
cout<<endl;
}
return 0;
}
