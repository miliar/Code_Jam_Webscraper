#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
using namespace std;

void readFile(char *fileName)
{
    ofstream myfile("output.out");
    FILE *fp = fopen(fileName,"r");
    if(fp == NULL)
    {
        printf("ERROR:unable to open %s\n",fileName);
        exit(1);
    }
    int testCase = 0;
    char nameG[20] = "GABRIEL";
    char nameR[20] = "RICHARD";
    char *name;
    fscanf(fp,"%d",&testCase);
    for(int i = 0;i < testCase;i++)
    {
        char ignore;
        int X,R,C = 0;
        fscanf(fp,"%d",&X);
        fscanf(fp,"%d",&R);
        fscanf(fp,"%d",&C);

        if(X == 1)
        {
            cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
            if(myfile.is_open())
            {
                myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
            }
            else
                cout<<"file error"<<endl;
        }
        else if(X > R * C)
        {
            cout<<"Case #"<<i + 1<<": "<<nameR<<endl;
            if(myfile.is_open())
            {
                myfile << "Case #"<<i + 1<<": "<<nameR<<endl;
            }
            else
                cout<<"file error"<<endl;
        }
        else if(R * C == 2)
        {
            if(X == 2)
                cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
                }
                else
                    cout<<"file error"<<endl;
        }
        else if(R * C == 3)
        {
            if(X == 2 || X == 3)
             {
                cout<<"Case #"<<i + 1<<": "<<nameR<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameR<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
        }
        else if(R * C == 4 && R != 2)
        {
            if(X == 3 || X ==4)
            {
                cout<<"Case #"<<i + 1<<": "<<nameR<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameR<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
            else if(X == 2)
            {
                cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
        }
        else if(R * C ==4 && R == 2)
        {
            if(X == 3 || X == 4)
            {
                cout<<"Case #"<<i + 1<<": "<<nameR<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameR<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
            else if(X == 2)
            {
                cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
        }
        else if(R * C == 6)
        {
            if(X ==2 || X == 3)
            {
                cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
            else if(X == 4)
            {
                cout<<"Case #"<<i + 1<<": "<<nameR<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameR<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
        }
        else if(R * C == 9)
        {
            if(X == 2 || X ==4)
            {
                cout<<"Case #"<<i + 1<<": "<<nameR<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameR<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
            else if(X == 3)
            {
                cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
        }
        else if(R * C == 8)
        {
            if(X ==3 || X == 4)
            {
                cout<<"Case #"<<i + 1<<": "<<nameR<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameR<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
            else if(X == 2)
            {
                cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
        }
        else if(R * C == 12)
        {
            cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
            if(myfile.is_open())
            {
                myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
            }
            else
                cout<<"file error"<<endl;
        }
        else if(R * C == 16)
        {
            if(X == 2 || X == 4)
            {
                cout<<"Case #"<<i + 1<<": "<<nameG<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameG<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
            else if(X == 3)
            {
                cout<<"Case #"<<i + 1<<": "<<nameR<<endl;
                if(myfile.is_open())
                {
                    myfile << "Case #"<<i + 1<<": "<<nameR<<endl;
                }
                else
                    cout<<"file error"<<endl;
            }
        }

    }




}


int main()
{
    char fileName[20] = "input.in";
    char *pc = fileName;
    readFile(pc);
    return 0;
}

