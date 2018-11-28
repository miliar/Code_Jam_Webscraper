#include <iostream>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdio.h>

using namespace std;
int i,j,n,k,t,co=0;
double su=0.0,c,f,x,s=0.0,s1=0.0,d=2.0,r[1100];
int main()
{
	freopen("b-large.in","rt",stdin);
freopen ("b-large.out","wt",stdout);
cin>>t;


for (i=1;i<=t;i++)
{
cin>>c>>f>>x;
s=0.0,s1=0.0;su=0.0,d=2.0;
while(s<=s1){
s1=x/d;
d+=f;
s=c/(d-f)+x/d;	
su+=c/(d-f);}	
su-=c/(d-f);
r[i]=su+s1;
}

for (i=1;i<=t;i++)
{
cout<<"Case #"<<i<<": ";printf("%.7f\n",r[i]);
}
	
	return 0;
}

