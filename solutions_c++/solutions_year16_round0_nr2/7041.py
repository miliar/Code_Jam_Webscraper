#include <string>
#include <stdlib.h>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    ofstream myfile;
    int cases=0;
    myfile.open ("output.in");
    cout << "Input: ";
    cin >> cases;

    for(int i=0;i<cases;i++)
    {
       string order;
       cin>> order;
       char debut,fin;
       int  numberofFlip=0,limit=0;
       bool stop=false;

       while(!stop)
       {
         debut=order[0];
         fin=order[0];
       for(int j=0;j<order.length();j++)
       {
         if(order[j]!=fin)
         {
          debut=order[j-1];
          fin =order[j];
          if(order[j]=='+')limit=j;
         }

       }

        if(debut=='+' && fin=='+')stop=true;
        else{
           if(fin=='-')
           {
              for(int k=0;k<order.length();k++)
              {
               if(order[k]=='-')order[k]='+';
               else order[k]='-';
              }

           }
           else
           {
              for(int k=0;k<limit;k++)
              {
               if(order[k]=='-')order[k]='+';
               else order[k]='-';
              }

           }

         numberofFlip++;
        }

       }


     cout << "Case #"<<i+1<<": "<<numberofFlip<<endl;
     myfile << "Case #"<<i+1<<": "<<numberofFlip<<endl;

    }


    myfile.close();

    return 0;
}
