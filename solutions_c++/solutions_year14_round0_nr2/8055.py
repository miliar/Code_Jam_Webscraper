/*
  nirmankarta
  tomorrow will be kinder

 */

#include <iostream>
#include <stdio.h>
#include <conio.h>
#define N 4

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

using namespace std;

double t,c,f,x;
double r,pr,ti,a,b,m;
int i,j,k;
int main() {
	//freopen("a.txt", "rt", stdin);
	//freopen("B-small-attempt2.in","rt",stdin);
	//freopen("B-small.out","wt",stdout);

	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);

	cin >> t;
	rep(i,t)
	{
	    cin>>c>>f>>x;
        r=2.0;
        pr=ti=0.0;
        m=x/r;
        cout<<"Case #"<<i+1<<": ";
        while(1)
        {
            a=c/double(r);
            b=x/double(r);
            if(m<ti+b)
                break;
            r+=f;
            m=ti+b;
            ti+=a;
        }
        //cout.precision(9);        cout<<m<<endl;
        printf("%.7f\n",m);
    }
	return 0;
}
