#include <iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;

ifstream in;
ofstream out;

 void   flipCakes(string &s,unsigned int endIndex)
    {
        string temp=s;
        for(int i=0;i<=endIndex;i++)
        {
            s[i]=temp[endIndex-i];
           if(s[i]=='+'){
                s[i]='-';

            }
            else
            {
                s[i]='+';
            }
        }

    }

int main()
{


   in.open("B-large.in");
    out.open("out.txt");
    int numberOfCustomers;
    in>>numberOfCustomers;

    vector<string> customers;
    string s;
    while(in>>s)
    {
        customers.push_back(s);
    }
    in.close();

    vector<int> numOfIterations;

   for(int i=0;i<numberOfCustomers;i++)
    {
        int iterations=0;
        int counter=1;
        string pom=customers[i];
        int pomSize=pom.size();
        while( pom.find('-') != -1 )
        {
            if(pom[pomSize-counter] == '+')
            {
                counter++;
            }
            else
            {
                if(pom[0]!= pom[pomSize-counter])
                {
                    int pomCounter=counter;
                    do
                    {
                        pomCounter++;
                    }while( pom[0]!= pom[pomSize-pomCounter]  );
                    flipCakes(pom,pomSize-pomCounter);
                }
                else
                {
                    flipCakes(pom,pomSize-counter);
                }
                iterations++;
            }

        }

        numOfIterations.push_back(iterations);

    }

    for(int i=0;i<numberOfCustomers;i++)
    {
        out<<"Case #"<<i+1<<": ";
        out<<numOfIterations[i]<<"\n";
    }
    out.close();


    return 0;
}
