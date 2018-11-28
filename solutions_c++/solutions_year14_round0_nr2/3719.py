/* Sahil Sondhi : Don't check my solutions STALKER!*/
 

#include <iostream>
#include<vector>
#include<cmath>
#include <iomanip>
#include<string>
#include<algorithm>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<list>
#include<map>
#include<cctype>
#include<limits>

#define scan(x) scanf("%d",&x)
#define forall(i,x,n) for(int i=x;i<n;i++)
#define forequal(i,x,n) for(int i=x;i<=n;i++)
#define scanl(x) scanf("%ld", &x)
#define scanll(x) scanf("%lld", &x)
#define minimum(a,b) (a>=b?b:a)
#define maximum(a,b) (a<=b?b:a)
#define scanfloat(x) scanf("%f", &x)
#define mod 1000000009
#define swap(xxx,yyy) { xxx=xxx+yyy; yyy=xxx-yyy; xxx=xxx-yyy; }
#define MAXARRAY 730000
#define __gcd(a,b) gcd(a,b)
#define LL long long
#define LD long double


using namespace std;




int main()
{
    
    long test;
	double c,f,x,t1,fmax;
    
	scan(test);
    
	
	for(int p=1;p<=test;p++)
    {
		
		
        cin>>c>>f>>x;
		fmax=2.0;
		t1=0.0;
        
		while((x/(fmax+f))<((x-c)/fmax))
        {
            t1=t1+c/fmax;
            fmax+=f;
        }
		
        t1+=x/fmax;
        cout<<"Case #"<<p<<": ";
		
		printf("%.7f\n",t1);
		//cout<<setprecision(7)<<fixed<<t1<<endl;
	}

return 0;

}
