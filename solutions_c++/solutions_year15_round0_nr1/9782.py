#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
using namespace std;


void readFile(char *fileName)
{
    ofstream myfile("output.out");
    FILE *fp = fopen(fileName,"r");
    if(fp == NULL){
        printf("ERROR:unable to open %s\n",fileName);
        exit(1);
    }
    int numLine = 1;
    int testCase = 0;
    fscanf(fp,"%d",&testCase);
    for(int i = 0;i < testCase;i++)
    {
        char ignore;
        int maxLevel = 0;
        fscanf(fp,"%d",&maxLevel);
        maxLevel++;
        char queue[maxLevel];
        int temp[maxLevel];
        fscanf(fp,"%c",&ignore);

        for(int i = 0;i < maxLevel;i++)
        {
            fscanf(fp,"%c",&queue[i]);
            temp[i] = queue[i] - '0';
        }

        fscanf(fp,"%c",&ignore);
        while(ignore != '\n')
            fscanf(fp,"%c",&ignore);
        int neededPeople = 0;
        int realPeople = 0;


        for(int j = 1;j < maxLevel;j++)
        {
            realPeople += temp[j - 1];
            if(temp[j] > 0)
                if(realPeople  < j)
                {
                    neededPeople += j - realPeople ;
                    realPeople += neededPeople;
                }
        }
        cout<<"Case #"<<i + 1<<": "<<neededPeople<<endl;
        if(myfile.is_open())
        {
            myfile << "Case #"<<i + 1<<": "<<neededPeople<<endl;
        }
        else
            cout<<"file error"<<endl;

    }
}

int main()
{
    char fileName[20] = "input.in";
    char *pc = fileName;
    readFile(pc);
    return 0;
}

