#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;

int main()
{
    int t,r,x,c,k,i=1;
    float z;
    bool flag=true;
    
    cin>>t;
    while(t--)
    {
     cin>>x>>r>>c;
     
     if(x!=1)
     {
       	z=sqrt(x);
        k=z;
       
       if((r*c)%x!=0)
         flag=false;
       else if(r==c&&(r*c)==x&&r>1)
         flag=false;
       else if((z>r||z>c)&&z>=1.5)
         flag=false;
     	else if(x>2&&((r==2&&x==c)||(c==2&&x==r)))
     	{
     		flag=false;
     	}
     }
      
     cout<<"Case #"<<i<<": ";  
     if(flag==true)
      cout<<"GABRIEL";
     else
      cout<<"RICHARD";
      cout<<"\n";
       i++;
      flag=true;        
          }
}
          