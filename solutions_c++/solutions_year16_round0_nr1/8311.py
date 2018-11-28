#include<bits/stdc++.h>
using namespace std;

int main()
{
 freopen("A-large.in","r",stdin);
 freopen("output_file_name.out","w",stdout);
 long long int t=0,t1=1;
// file *fin,*fout;
 scanf("%lld",&t);

 while(t1<=t)
 {
 int a[10]={0};
 long long int n=0,f=0;

 scanf("%lld",&n);
 long long int n2=n;

 long long int i=1;
 while(i>=0)
 {
   long long int new1=n,r;

   while(new1>0)
   {
     r=new1%10;
     a[r]=1;
     new1=new1/10;
   }

   if(a[0]==1 && a[1]==1 && a[2]==1 && a[3]==1 &&a[4]==1 && a[5]==1&&a[6]==1 && a[7]==1&&a[8]==1 && a[9]==1)
      break;

   i++;
   long long int check=i*n2;

   if(n==check)
     {
     f=1;
     break;
     }
   n=i*n2;
   //cout<<n<<endl;

 }
 if(f==1)
  printf("Case #%lld: INSOMNIA\n",t1);
 else
  printf("Case #%lld: %lld\n",t1,n);

 t1++;
 }

return 0;
}
