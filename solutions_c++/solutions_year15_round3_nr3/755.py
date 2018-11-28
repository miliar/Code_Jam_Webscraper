#include<conio.h>
#include<iostream>
using namespace std;

int checkValues(int *denom,int max)
{
     int ctr=0,needed=0,maxVal=0;
     if (denom[ctr]!=1)
     {   
         needed++;
     }
     else
     {   
         ctr++;
     }
     maxVal+=1;
     if(maxVal>=max)
     return needed;
     if (denom[ctr]!=2)
     {
        needed++;
     }
     else
     {
        ctr++;
     }
     maxVal+=2;
     if(maxVal>=max)
     return needed;
     for (int val=3; val<=max; val++)
     {
//         cout<<"\nMAXVAL: "<<maxVal<<" for "<<val;
         if(denom[ctr]==val)
         {
              ctr++;
              maxVal+=val;
         }
         else
         {
             if(val<=maxVal)
                           continue;
             else
             {
                 needed++;
                 maxVal+=val;
             }
         }
     }
     return needed;
}
int main () {
    int cases,rep,denom,amt,minNew,*denomMatrix,ctr,*posVal;
    scanf("%d",&cases);
    for(int tCase=1; tCase<=cases; tCase++)
    {
            ctr=0;
            scanf("%d %d %d",&rep,&denom,&amt);
            denomMatrix=(int*)malloc(denom*sizeof(int));
            for (int denVal=0; denVal<denom;denVal++)
            {
                scanf("%d",&denomMatrix[denVal]);
            }
/*            for (int i=0; i<denom; i++)
            {
                cout<<":| "<<denomMatrix[i]<<" |:";
            }
*/            cout<<"Case #"<<tCase<<": "<<checkValues(denomMatrix,amt)<<endl;
    }
//    getch();
   
}
