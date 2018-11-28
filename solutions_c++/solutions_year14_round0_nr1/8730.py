#include <iostream>
# include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
    ifstream input ("A-small-attempt1.in");
    ofstream out ("output.txt");

    int x,row,match,element,array1[4], array2[4];
    string str;
    input>>x;
    //getline(input,str);
    //out<<x<<endl;
   for(int i=0; i<x; i++)
    {
               input>>row;
               getline(input,str);
               for(int j=0;j<4;j++)
               {
                   getline(input,str);
                   if(j==row-1)
                      {
                         stringstream ss(str);

                            int index = 0;
                            while(ss>>element)
                             {
                                 //out<<"element = "<<element<<endl;
                               array1[index]=element;
                               index++;
                             }
                      }

                }// loop for the partition of the case

               input>>row;
               getline(input,str);

               for(int j=0;j<4;j++)
               {
                   getline(input,str);
                   if(j==row-1)
                      {
                         stringstream ss(str);

                            int index = 0;
                            while(ss>>element)
                             {
                                //out<<"element = "<<element<<endl;
                               array2[index]=element;
                               index++;
                             }

                      }

                }// loop for the partition of the case

              //to search for the card number
              int counter=0;
              for(int l=0;l<4;l++)
                 for(int m=0;m<4;m++)
                     if(array1[l]==array2[m])
                     {
                       match=array1[l];
                       counter++;
                     }


              //to print the output of the testcase
               if(counter==1)
                 out<<"Case #"<<i+1<<": "<<match<<endl;
               else
               {  if(counter==0)
                    out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
                  else if (counter>1)
                    out<<"Case #"<<i+1<<": Bad magician!"<<endl;
               }
         }// loop for 3 cases



    return 0;
}//main
