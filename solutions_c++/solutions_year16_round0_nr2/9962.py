#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    ifstream File;
	int numberofCases;
    File.open("B-large.in");
    ofstream outfile;
    outfile.open("outlarge.txt");
    File >> numberofCases;
    string arr[numberofCases];

     for (int i = 0; i < numberofCases; i++)
    {
        File >> arr[i];
    }

    for(int ing = 0; ing < numberofCases; ing++ )
    {

    int countr = 0;
    string input = arr[ing];
    //cout<< (input.substr(0,1));
    if (input[0] == '-')
        int minu = 1;
    if(input[0] == '+')
        int plusu = 1;
    int sizer = input.size();
    int x = 1;
    //cout<< input[2];
    //while (x=1){}
    while (x!= 0){
        for(int i = 0 ; i < sizer ; i++)
        {

            if(input [0] == '-'){
                for(int ja =0; ja <sizer ; ja++)
                {
                    if(input[ja] == '+')
                        break;
                    if(input[ja] == '-' && ja == sizer-1 ){
                        countr++;
                        outfile<< "Case #"<<ing+1<<": ";
                        outfile<< countr;
                        outfile<<"\n";

                        cout<< countr<<endl;
                        x = 0;
                        break;
                    }
                }
            }
            if(input [0] == '+'){
                for(int ja =0; ja <sizer ; ja++)
                {
                    if(input[ja] == '-')
                        break;
                    if(input[ja] == '+' && ja == sizer-1 ){
                        cout<< countr<< endl;

                        outfile<< "Case #"<<ing+1<<": ";
                        outfile<< countr;
                        outfile<<"\n";
                        x = 0;
                        break;
                    }
                }
            }
            if(input[i] == '-' && input[i+1] == '+' ){
                string subs = input.substr(0,i+1);
                for (int j = 0; j < subs.size(); j++)
                {
                    input[j] = '+';
                }
                countr ++ ;
                i = 0;
            }
            if(input[i] == '+' && input[i+1] == '-'){
                string subs = input.substr(0,i+1);
                for (int j = 0; j < subs.size(); j++)
                {
                    input[j] = '-';
                }
                countr ++ ;
                i = 0;
            }
            if(x == 0)
            {
                break;
            }

        }

    }
    }
}
