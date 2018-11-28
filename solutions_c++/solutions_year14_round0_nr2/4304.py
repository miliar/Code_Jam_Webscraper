#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>
#include <ctype.h>
#include <iomanip>
#include <math.h>
using namespace std;



float number(string line)
{
        char j2[]="00000000000000000000";
         for(int j=0;j<sizeof(line);j++)
          {
             j2[j]=line[j];
          }
   //double num = atof(j2);
   double num = atof(line.c_str());;
   return num;
}


int main()
{
    string line;
    char j1[]="00000000000000000000";
    char j2[]="00000000000000000000";
    double collection_time1=0, collection_time2=0;

    ofstream ans;
    ans.open ("ansCokie.txt");


    ifstream infile;
    infile.open("a.txt");
    infile>>line;
    float lines=number(line);
    double C,F,X;
    double C1,F1,X1;
    int inj=1;

    for(int i=0;i<lines;i++)
    {
        inj=1;
        infile>>line;
        C=number(line);
        //cout<<line<<endl;
        //cout<<C<<endl;
        infile>>line;
        F=number(line);
        //cout<<line<<endl;
        //cout<<F<<endl;
        infile>>line;
        X=number(line);
        //cout<<line<<endl;
        //cout<<X<<endl;

        collection_time1=X/2;

        collection_time2=0;
        F1=2;
        for(int ii=0;ii<inj;ii++)
        {
            collection_time2=collection_time2+(C/F1);
            F1=F1+F;
        }
        collection_time2=collection_time2+(X/F1);

        while( collection_time1 > collection_time2)
        {
            inj++;
        collection_time1=collection_time2;
        collection_time2=0;
        F1=2;
        for(int ii=0;ii<inj;ii++)
        {
            collection_time2=collection_time2+(C/F1);
            F1=F1+F;
        }
        collection_time2=collection_time2+(X/F1);

        }

        ans<<"Case #"<<i+1<<": "<<setprecision(7)<<collection_time1<<endl;

        cout<<"Case #"<<i+1<<": "<<setprecision(7)<<collection_time1<<endl;
        //cout<<collection_time2<<endl<<endl;
    }


    ans.close();












//    int i=0;
  /*  ifstream myfile ("a.txt");

      if (myfile.is_open())
      {
        while ( getline (myfile,line) )
        {
          cout << line << '\n';
        }
        myfile.close();
      }

      for(int j=0;j<sizeof(line);j++)
      {
          if(line[j]!=' ')
          {
              break;
          }
         j2[j]=line[j];
         cout<<endl<<j2<<endl<<endl;
      }

      char* pEnd;
      float io=strtof (j2, NULL);

      cout<<io<<endl;
*/
    return 0;
}
