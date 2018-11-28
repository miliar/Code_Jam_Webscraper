#include<iostream>
#include<algorithm>
using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}
int main()
{
 int t; 
 cin>>t;
 int cases =0;
 while(t-->0)
  {	  
   cases++;
   int n;
   cin>>n;
   int a[n],b[n];
   float x;
   for(int i=0;i<n;i++)
    {cin>>x;a[i] = x*1000000;}
   for(int i=0;i<n;i++)
    { cin>>x;b[i] = x*1000000;}
   qsort(a,n,sizeof(int),compare);
   qsort(b,n,sizeof(int),compare);
     
   int f1=0,f2=0,r1=n-1,r2=n-1,resultcase1=0,resultcase2=0;
   //while(f1 !=r1 && f2 !=r2)
   for(int i=0;i<n;i++)
   {
	 if(a[f1]<b[f2]){
		f1++;
		r2--;
		//r2--;	
		}
	 else
	 { 
	  resultcase1++;
 	  f2++;
 	  f1++;
 	  //f1++;
	  }
   }
   f1=0;
   f2=0;
   r1=n-1;
   r2=n-1;
      for(int i=0;i<n;i++)
   //while(r1 !=f1 && r2 !=f2)
   {
    if(a[r1]>b[r2])
    {
		r1--;
		f2++;
		resultcase2++;
	 }
	 else
	  {
	  r1--;
	  r2--;
	  }
   }
   cout<<"Case #"<<cases<<": "<<resultcase1<<" "<<resultcase2<<endl;
  // Case #1: 0 0
  }
cin.get();
cin.get();
return 0;
}
