#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ofstream myfile;//file for output
    int cases=0,n=0;
    myfile.open ("output.in");
    cout<< "Input: ";
    cin>> cases;

    for(int i=0;i<cases;i++)
    {
      cin >>n;
      string str;
      int index=0;
      long long answer=0;
      vector <long long> digitTab;
      bool var=false;

      for(int j=1;j<=1000000;j++)
      {
         answer=j*n;
         str= to_string(answer);
         for(int k=0;k< str.length();k++)
         {
            var=false;
           for(int m=0;m<index;m++)
           {
              if((int)str[k]-48 == digitTab[m])var=true;
           }
           if(var==false)
           {
             digitTab.push_back((int)str[k]-48);
             index++;
           }
         }if(index==10)break;
      }
      if(index==10)
      {
      cout <<"Case #"<<i+1<<": "<< answer<<endl;
      myfile <<"Case #"<<i+1<<": "<< answer<<endl;
      }
       else
      {
      cout <<"Case #"<<i+1<<": "<< "INSOMNIA"<<endl;
      myfile <<"Case #"<<i+1<<": "<< "INSOMNIA"<<endl;
      }


    }

    myfile.close();
    return 0;
}
