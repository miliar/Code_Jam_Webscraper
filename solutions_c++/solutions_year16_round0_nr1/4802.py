#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen( "input.txt","r",stdin );
    freopen( "output.txt","w",stdout );
    long long a,b,c,d=0,e,f,g,h,i,j,k=1,l=0,m[10];
    cin>>a;
    for (i=0;i<a; i++) {
    	for (j=0;j<10; j++) m[j]=0;
    	cin>>c;
    	b=c;
    	d=c;
    	k=0;
    	if (b==0)  {cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<"\n"; continue;}
    	while (k<10) {                  //cout<<b<<"\n";
    		while (b!=0) {
    			m[b%10]=1;
    			b=b/10;
    		}
    		for (j=0;j<10; j++) l+=m[j];
    			if (l==10) {cout<<"Case #"<<i+1<<": "<<d<<"\n"; }
    		k=l;
    		l=0;
    		d=d+c;
    		b=d;
    	}
    }

return 0;
}
