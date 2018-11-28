#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main()
{
    int casesnum;
    string S,H;
    ifstream input;
    ofstream output;
	input.open("A-small-attempt0.in");
	output.open("A-small-attempt0.out");
    input>>casesnum;
    int counter=0;
 //output<<N;
          //  for(int i=1;i<=casesnum;i++)
                while (input>> S)
               { // cout<<S<<" ";
                   counter++;
               H=S;
               H[0]=S[0];
               //cout<<H<<" ";
                       for(int i=1;S[i]!=NULL;i++)
                            {   if(S[i]<H[0])
                               {

                                H[i]=S[i];
                                //cout<<"t ";
                               }
                                else
                                {

                                 for(int j=i;j>0;j--)
                                 {

                                 H[j]=H[j-1];
                                 }
                                    H[0]=S[i];
                                //    cout<<"f ";
                                }
                            }

               output<<"Case #"<<counter<<": "<<H<<endl;

               }


    return 0;
}


