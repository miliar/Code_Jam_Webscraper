#include <iostream>
#include<fstream>
#include <stdio.h>
#include<math.h>
#include<cmath>
using namespace std;

int main()
{
    freopen ("B-large.in","r",stdin);
    freopen ("output.txt","w",stdout);
short int t;
cin>>t;

double c,f,x,total1,total2,lasttime=0;
double cooke=2;

for(int i=0;i<t;i++){
    cooke=2;
    lasttime=0;
cin >>c>>f>>x;
total1 = x/2;
int j;
for( j=0;;j++){
lasttime += c/((f*j)+2);

cooke += f;
total2 = lasttime + (x/cooke);

if(total1 < total2)
{
    break;
}

total1 = total2;
}






cout<<"Case "<<"#"<<i+1<<": ";
printf("%f\n", total1);


}


    return 0;
}
