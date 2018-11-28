#include <iostream>
#include <algorithm>
#include <fstream>
#include <stdio.h>
using namespace std;
int main()
{ifstream cin("B-large.in"); 
//ofstream printf("output.txt");
int t; cin>>t; double ans[t];
for(int i=0;i<t;i++)
{
double c,f,x; cin>>c>>f>>x; double e[100000];
e[0]=x/2.000000000;
for(int h=0;h<100000;h++)
{e[h+1]=e[h]*1.0000000-(x/(h*f+2.0000000)*1.00000)+c/(h*f+2.0000000)+x/(h*f+f+2.000000000);
}
double min=10000000;
for(int h=0;h<100000;h++)
{if(e[h]<min) min=e[h];
}
ans[i]=min*1.000000000;
}
for(int i=0;i<t;i++)
{ cout<<"Case #"<<i+1<<": "; printf("%0.12f",ans[i]); cout<<endl; }

return 0;
}
 
