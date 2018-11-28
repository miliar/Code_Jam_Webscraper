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
#include<limits.h>

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
   FILE *fp,*fo;
	fp=fopen("D-large.in","r");
	fo=fopen("output.o","w");
	
   int test;
   
   int n;
   int nor,dec;
   fscanf(fp,"%d",&test);
   //cin>>test;
   
   float a[1005],b[1005];
   
//   float min;
  // int tempj;
   
   for(int p=1;p<=test;p++)
   {
	dec=nor=0;
	fscanf(fp,"%d",&n);
	//cin>>n;
	
	forall(i,0,n)
	 fscanf(fp,"%f",&a[i]);
	 
	 //cin>>a[i];
	 
	forall(i,0,n)
	 fscanf(fp,"%f",&b[i]);	
		
	//	cin>>b[i];
	
	sort(a,a+n);
	sort(b,b+n);
	
//	forall(i,0,n)
//	 cout<<a[i]<<" ";
//	 cout<<endl;
//	forall(i,0,n)
//	 cout<<b[i]<<" ";
//	 cout<<endl;
	 
	 
	int x,y; 
	x=y=0;

    
	while(x<n)
      {
        if(a[x]>b[y])
           {
             x++;
             y++;
             dec++;
           }
        else
         x++;
       }
    
	x=y=0;
 
    while(x<n)
      {
        if(b[x]>a[y])
         {
           x++;
           y++;
           nor++;
         }
         else
          x++;
      }

 
       
        
	fprintf(fo,"Case #%d: \n",p);
	fprintf(fo,"%d %d\n",dec,n-nor);
	
//	cout<<"Case #"<<p<<": ";
  //  cout<<dec<<" "<<n-nor<<endl;
   
   }

return 0;

}
