#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream f;
    ofstream fo;
    f.open("A-small-attempt4.In");
    fo.open("A-small_out.txt");
  int temp[4],temp1[4],arr[4][4];
  int r,s,n,p,a,b,x,y,z,count=0;
  f>>n;
  for(int i=0;i<n;i++)
  {
      for(int j=0;j<2;j++)
      {
      
       f>>p;
       for(int r=0;r<4;r++)
       {
        for(s=0;s<4;s++)
        {
            f>>arr[r][s];            
        }       
       }
               if(p==1)a=0;
               else if(p==2)a=1;
               else if (p==3)a=2;
               else if(p==4)a=3;
         for(int b=0;b<4;b++)
         {
                 if(j==0)
                 {
                 temp[b]=arr[a][b];
                 }
                 if(j==1)
                 {
                  temp1[b]=arr[a][b];       
                 }   
         }              
      }
      for(int a=0;a<4;a++)
      {
         x=temp[a];
         for(int z=0;z<4;z++)
         {
          if(x==temp1[z])
          {
           count++;
           y=x;
          }       
         }      
      }
     if(count==1)
      fo<<"Case #"<<i+1<<": "<<y<<endl;
      else if(count>1)
      fo<<"Case #"<<i+1<<": Bad magician!"<<endl;
      else if(count==0)
      fo<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
      
      count=0;
  }
    f.close();
   fo.close();
}
