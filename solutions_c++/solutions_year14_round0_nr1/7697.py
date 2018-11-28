#include<iostream>
using namespace std;
int main()
{
  int t,i ;
  cin >> t ;
  int a1,a2;
  int x;
  int hash[17];
  for(int j=1;j<=t;j++)
  {
    for(i=1;i<=16;i++)
      hash[i]=0;   
  
     cin >> a1;
     int f = (a1-1)*4;
     for(i=1;i<=16;i++)
     {
        cin >> x ;
        if(i>f && i<=(f+4))
         hash[x]=1;
     } 
	    
 
cin >> a2;
      f = (a2-1)*4;
     for(i=1;i<=16;i++)
     {
        cin >> x ;
        if(i>f && i<=(f+4))
        { 
           if(hash[x]==1)
            hash[x]=2;
        }
     }
   
 int count=0;
     int index=-1;
     for(i=1;i<=16;i++)
     {
       if(hash[i]==2)
       {
          index=i;
          count++;
       }
     }
     if(count==0)
       cout << "Case #"<< j<<": Volunteer cheated!\n" ;
     else if (count > 1 )
       cout << "Case #"<< j<<": Bad magician!\n";
     else
       cout << "Case #"<< j<<": "<< index <<"\n"; 
     
        
  }
}
