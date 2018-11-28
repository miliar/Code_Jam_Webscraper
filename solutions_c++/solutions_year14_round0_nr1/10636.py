#include<iostream>
#include<stdio.h>
#define m 4
using namespace std;

int main()
{ int t,a[m][m],i,j,count,t_a[4],k,ans;


//////////////////////////////



FILE * pFile;
   //char buffer [100];

   pFile = fopen ("A-small-attempt1.in" , "r");
 {

  FILE *f = fopen("file2.txt", "w");
fscanf (pFile, "%d", &t);
  //cin>>t;

k=1;

 while ( ! feof (pFile) )
     {
while(k<=t)
{
 {
   fscanf (pFile, "%d", &ans); //cin>>ans;
 //cout<<ans;
    for(i=0;i<m;i++)
      {
          for(j=0;j<m;j++)
            fscanf (pFile, "%d", &a[i][j]);//cin>>a[i][j];

      }
ans--;
for(j=0;j<m;j++)
    {

        t_a[j]=a[ans][j];

    }

  fscanf (pFile, "%d", &ans); //cin>>ans;

for(i=0;i<m;i++)
      {

        for(j=0;j<m;j++)
            fscanf (pFile, "%d", &a[i][j]);//cin>>a[i][j];


      }

ans--;

count=0;
for(i=0;i<m;i++)

   {
     for(j=0;j<m;j++)
     {
      if(t_a[i] == a[ans][j])
       {
            count++;
        }
     }
   }

     if(count>1)
       {
         fprintf(f, "Case #%d: Bad magician!\n",k);
       }

    else {if(count == 0)
       {
         fprintf(f, "Case #%d: Volunteer cheated!\n",k);


       }

      else  {
              int flag=0;
            for(i=0;i<m;i++)

             {
             for(j=0;j<m;j++)
              {
               if(t_a[i]==a[ans][j])
               {
                 fprintf(f, "Case #%d: %d\n",k,t_a[i]);
                 flag=1;
                 break;
            }
            if(flag==1)
               break;
          }

         }
        }
    }
}
    k++;
}


  //////////////
     }
     fclose (f);
    fclose (pFile);
   }






//////////////////////////////////



return 0;
}
