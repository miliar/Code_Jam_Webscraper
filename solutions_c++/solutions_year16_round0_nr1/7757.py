#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
bool visited[10];
int main()
{

    freopen("file.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
cin>>t;
long long int l,tmp,por,z,i,j,p,check;
por=0;
 while(t--)
    {memset(visited,false,sizeof visited);
     por++;
    cin>>l;
    tmp=l; p=l;
    check=0;
   for(j=2;j<=100;j++)
     {//cout<<"l"<<l<<endl;
            while(tmp!=0)
       {
         z=tmp%10;
         if(visited[z]==false)
         {
             visited[z]=true;
             check++;
         }

         tmp=tmp/10;
       }
    /*   for(i=0;i<10;i++)
         {check=0;
         if(visited[i]==true)
            {
            check++;
            }
         }*/
         if(check==10)
         {
         break;j=1e12+2;
         }
         else
          {

          l=l+p;
          }
      tmp=l;
     }
     if(j==101)
      {
      cout<<"Case #"<<por<<": INSOMNIA"<<endl;
      }
      else
      cout<<"Case #"<<por<<": "<<l<<endl;



    }


return 0;

}
