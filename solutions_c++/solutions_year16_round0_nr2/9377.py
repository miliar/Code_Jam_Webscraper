#include <iostream>
#include <fstream>
#include <math.h>
#include <string.h>

using namespace std;

string reverse(string N)
    {   int length=0;
        string s;
        s=N;
        for(int i=0;N[i]!=NULL;i++)
        length++;
        for(int i=0;i<length;i++)
        N[i]=s[length-1-i];

        return N;
    }

int main()
{
    int casesnum;
    string N,h;
    int reversecounter=0,outputcounter=0,length=0;
    ifstream input;
    ofstream output;
	input.open("B-large.in");
	output.open("B-large.out");
    input>>casesnum;

      while (input>> N)
      { reversecounter=0;
        length=0;
        N=reverse(N);
        h=N;
        for(int i=0;N[i]!=NULL;i++)
        length++;

        for(int j=1;j<=length;j++)
             {

                if(N[j-1]=='+')
                    ;
                else if(N[j-1]=='-')
                    {
                           for(int i=j-1;i<length;i++)
                                {   if (N[i]=='+')
                                         {
                                         N[i]='-';
                                         }
                                    else if(N[i]=='-')
                                            N[i]='+';
                                }
                        reversecounter++;


                    }

             }
          outputcounter++;
         output<<"Case #"<<outputcounter<<": "<<reversecounter<<endl;
      }

  return 0;
}
