#include <iostream>
#include <conio.h>
#include <map>
#include <stdlib.h>
#include <stdio.h>
#include <string>
//Kye Wei

using namespace std;




int main()
{
    int lineNum=0;
    int rounds;
    int roundcount = 0;
    short currentstep = 0;
    //map<string, bool> folders;

    //1 numberoflines
    //2 datacollection
    //3 datacollection
    //4 analysis
    int blocknum = 0;
    double * naomi;
    double * ken;
    string input_line, temp;

    while(cin) {
    getline(cin, input_line);



    lineNum+=1;

    if (lineNum==1){
        rounds = atoi(input_line.c_str());

        if (rounds>0)
            currentstep = 1;
    }
    else if (currentstep ==1)
    {
        roundcount++;
        blocknum = atoi(input_line.c_str());


        naomi = new double[blocknum];
        ken = new double[blocknum];
        if (blocknum>0)
            currentstep = 2;
    }
    else if (currentstep ==2)
    {
        //printf("blocknum: %d\n", blocknum);
        if (blocknum>1)
        {

            int space[blocknum-1];
            int counter = 0;
            for (int i = 0; i< input_line.length(); i++)
            {
                if (input_line[i]==' ' && counter<blocknum-1)
                {
                    space[counter]=i;
                    counter++;
                    //printf("%d\n)", space[counter]);
                }
            }


            for (int i =0; i< blocknum; i++)
            {
                if (i==0)
                {
                    naomi[i]=atof((input_line.substr(0, space[0])).c_str());

                }
                else if (i+1 == blocknum)
                {
                    naomi[i]=atof(input_line.substr(space[i-1]+1).c_str());
                }
                else
                {
                    naomi[i]=atof((input_line.substr(space[i-1]+1, space[i]-space[i-1])).c_str());
                }
                //printf("input: %f\n", naomi[i]);
            }

        }
        else if (blocknum==1)
        {
            //printf("KK%f\n", atof(input_line.c_str()));
            naomi[0]=atof(input_line.c_str());

        }
        currentstep = 3;
    }
    else if (currentstep ==3)
    {

        if (blocknum>1)
        {
            int space[blocknum-1];
            int counter = 0;
            for (int i = 0; i< input_line.length(); i++)
            {
                if (input_line[i]==' ' && counter<blocknum-1)
                {
                    space[counter]=i;
                    counter++;
                }
            }

            for (int i =0; i< blocknum; i++)
            {
                if (i==0)
                {
                    ken[i]=atof((input_line.substr(0, space[0])).c_str());
                }
                else if (i+1 == blocknum)
                {
                    ken[i]=atof(input_line.substr(space[i-1]+1).c_str());
                }
                else
                {
                    ken[i]=atof((input_line.substr(space[i-1]+1, space[i]-space[i-1])).c_str());
                }
            }

        }
        if (blocknum ==1)
        {
            ken[0]=atof(input_line.c_str());
            //printf("KK%f\n", atof(input_line.c_str()));
        }
        currentstep = 4;
    }
    if (currentstep ==4)
    {
        //sort

        double temp;
        for(int i = 0; i < blocknum; i++)
        {
            for (int j = 0; j < blocknum-1; j++)
            {
                if (naomi[j] > naomi[j+1])
                {
                    temp = naomi[j];
                    naomi[j] = naomi[j+1];
                    naomi[j+1] = temp;
                }
            }
        }

        for(int i = 0; i < blocknum; i++)
        {
            for (int j = 0; j < blocknum-1; j++)
            {
                if (ken[j] > ken[j+1])
                {
                    temp = ken[j];
                    ken[j] = ken[j+1];
                    ken[j+1] = temp;
                }
            }
        }

        int deceitwinners=0;
        int tempint=0;
        for(int i = 0; i < blocknum; i++)
        {
            while (ken[i]>naomi[tempint] && tempint < blocknum)
                tempint++;
            //guarantee ken<naomi
            if(tempint < blocknum && ken[i]<naomi[tempint]){
                    //printf ("ken: %f, naomi: %f", ken[i], naomi[tempint]);
                deceitwinners++;
                //printf("tempint: %d\n", tempint);
            }
            tempint++;
        }

        //printf("deceit: %d\n",deceitwinners);


        int regularwinners=0;
        int kenhigh=0, kenlow = 0;

        for (int i = blocknum-1 ; i >=0; i--)
        {
            double play = naomi[i];


            for (int j =0; j< blocknum; j++)
                if (ken[j] > ken[kenhigh])
                kenhigh=j;
            for (int j =0; j< blocknum; j++)
                if (ken[j] < ken[kenlow])
                kenlow=j;

            if (ken[kenhigh]>naomi[i])
                ken[kenhigh]=-1;
            else if (ken[kenhigh]<naomi[i]){
                ken[kenlow]=-1;
                regularwinners++;
            }
            kenhigh=0;
            kenlow = 0;

        }
    //printf("regular: %d\n",regularwinners);
        /*for (int i =0; i< blocknum; i++)
            printf("naomi: %f, ken: %f\n", naomi[i], ken[i]);*/



        printf("Case #%d: %d %d\n", roundcount, deceitwinners, regularwinners);

        currentstep=1;
        if (roundcount==rounds)
            currentstep=8;
        blocknum = 0;

        delete [] naomi;
        delete [] ken;

    }

    };


    return 0; //finish
}
