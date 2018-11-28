#include<iostream>
#include<math.h>
#include<string.h>
using namespace std;
int main()
{
 freopen("co.txt","r",stdin);
 freopen("coa.txt","w",stdout);
 int t;
 cin>>t;
 for(int q=1;q<=t;++q)
 {
  double c,f,x,min,ans,term1,inc;
  int k=0;
  cin>>c>>f>>x;
  inc=f;
  min=x/2.0;
  term1=c/2.0;
  xy:
  ans=term1+x/(2.0+f);
  if(ans<min)
  {
   //cout<<min<<" "<<ans<<endl;
   min=ans;
   term1+=c/(2.0+f);
   f=f+inc;
   k++;
   goto xy;          
  }//cout<<k;
  printf("Case #%d: %0.7lf\n",q,min);        
 }    
}
