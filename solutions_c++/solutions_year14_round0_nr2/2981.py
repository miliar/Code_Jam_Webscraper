#include<iostream>
#include<stdio.h>
#define forn(i,n) for(i=0;i<n;i++)
#include <iomanip>
using namespace std;
int main()
{
	int t;
	freopen("prob2_large.in","r",stdin);
	freopen("prob2_large.txt","w",stdout);
	cin>>t;
	for(int p=1;p<=t;p++){
        double c,f,x,time1=0.0000000,time2=0.0000000;
        cin>>c>>f>>x;
        double rate=2.0000000;
        double s=0.0000000;
        while(1){
            time1=s+x/rate;
            s+=(c/rate);
            rate+=f;
            time2=s+(x/rate);
            if(time1<=time2)
                break;
        }

        cout<<"Case #"<<p<<": ";
        cout.precision(7);
        cout<<fixed<<time1;

		cout<<endl;
	}
    return 0;
}
