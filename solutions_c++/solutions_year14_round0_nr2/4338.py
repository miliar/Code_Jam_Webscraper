#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

#define forn(i,n) for(int i = 0; i<(int) n; i++)
#define forns(i,n,s) for(int i = s; i<n; i++)
#define forn1(i,n) for(int i = 1; i<=(int) n; i++)

#define dforn(i,n) for(int i = n; i>=0; i--)
#define dforn2(i,n,s) for(int i = n; i>=s; i--)

#define MAX 1048576
#define pb push_back
#define mp make_pair

using namespace std;
double n,C,F,X;
double emp=2;
double gasto = 0;
double calculo()
{
    double par = C/emp;
    emp+=F;
    gasto +=par;
    return gasto+(X/emp);
}
int main()
{
   	freopen("cookie.txt", "r", stdin);
   	freopen("cookieout.txt", "w", stdout);
   	cin>>n;
   	forn(i,n)
   	{
   	    cout<<"Case #"<<i+1<<": ";
   	    emp=2;
   	    gasto=0;
   	    cin>>C>>F>>X;
        double resp = X/emp;
        double voy;
        while(resp>(voy=calculo()))
             resp=voy;
        printf("%.7lf\n",resp);
   	}
    return 0;
}
