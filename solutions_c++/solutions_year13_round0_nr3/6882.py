#include<io.h>
#include<math.h>
#include <string>
using namespace std;
#include <iostream>



int checkpali(int num)
{
    int temp=num;
    int sum=0;
    int r;

         while(temp){
             r=temp%10;
             temp=temp/10;
             sum=sum*10+r;
         }
         if(num==sum)
            return 1;
            else
            return 0;
    }
int checksqr(int num)
{
    int sq=sqrt(num);
    if(sq*sq==num && checkpali(sq)==1 )
    return 1;
    else
    return 0;
}

int main()
{
  int a=1,b,op,lr,ur;
   string l;
	FILE * pFile;
	FILE * qFile;

    pFile = fopen ("d:/C-small-attempt11.in","r");
    qFile = fopen ("d:/b.txt","w+");

  
  
  
 
   //cin>>a;
   fscanf (pFile, "%d", &a);
   cout<<"no is " <<a;
   
 
    for(int t = 0; t < a; t++)
    {
        op=0;
        b=t+1;
        fscanf (pFile, "%d", &lr);
		 fscanf (pFile, "%d", &ur); 
   
     for(int i=lr;i<=ur;i++)
     {
         if(checkpali(i)==1 && checksqr(i)==1)
         {
         	op++;
         	cout<<i<<" ";
         }
         

     }
 // cout<<"Case"<<b<<": "<<op;
  fprintf (qFile, "Case #%d: %d", b, op);
 fprintf (qFile, "\n");
    } 

 fclose (pFile);
 fclose (qFile);
return 0;


}

