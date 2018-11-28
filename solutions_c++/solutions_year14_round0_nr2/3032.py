#include<iostream>
#include<climits>
#include<cstdio>
#include<set>
#include<cstring>
#include<map>
#include<cmath>
#include<vector>
using namespace std;

int main()
{ 
int t,k,i,j;
double c,f,x,ctime=0,ftime=0,ft=0,p;
cin>>t;
for(k=1;k<=t;k++)
{   
     cin>>c>>f>>x;
     ftime=x/2;
     p=2+f;
	 ft=(x/p);
	 ctime=(c/2)+ft;
	 
     while(ctime<ftime)
     {
     //	cout<<ftime<<" -c "<<ctime<<"\n";
     	ftime=ctime;
        ctime=ctime-ft+c/p+x/(p+f);
        p+=f;
		ft=x/p;
     }
     printf("Case #%d: %.7f\n",k,ftime);
     
 //    cout<<"Case #"<<k<<": "<<ftime<<"\n";
}
}

