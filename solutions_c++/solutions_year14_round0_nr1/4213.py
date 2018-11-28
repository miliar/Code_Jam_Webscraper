#include <iostream>
#include <conio.h>
#include <map>
#include <stdlib.h>
#include <stdio.h>
#include <string>
//Kye Wei

using namespace std;

void change(int dollars, int cents)
{
    int total = dollars*100+cents;

    map<string, int> coins; // Map that connects a string key to a integer quantity
    //start from the highest coin possible to be most efficient, and modulus down
    coins["$1.00 Loonies"] = total/100;
    total = total%100;
    coins["$0.25 Quarters"] = total/25;
    total = total%25;
    coins["$0.10 Dimes"] =total/10;
    total = total%10;
    coins["$0.05 Nickels"] = total/5;
    total = total%5;
    coins["$0.01 Pennies"] = total/1;
    total = total%1;
    // I added numbers to preserve the order of map since iterator iterates using key organized alphabetically
    for(map<string, int>::iterator k=coins.begin(); k !=coins.end(); k++) //iterate through and print
        if(k->second!=0)
            cout<<"Quantity of "<<k->first<<": "<<k->second<<endl; //first is key, second is is value
    cout<<endl;

}

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

    /*int a, b, acount, bcount;
    a=b=acount=bcount=0;
    int mkdircount=0;*/
    string input_line, temp;
    int a, acount, b, bcount;
    a=acount=b=bcount=0;
    int array1[4], array2[4];
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
        //read in row number
        a = atoi(input_line.c_str());
        //printf("a: %d\n", a);
        if (a!=0)
            currentstep=2;

    }
    else if (currentstep==2)
    {
        acount++;

        if (acount==a){
            int space[3];
            int counter = 0;
            //printf("%s\n", input_line.c_str());
            for (int i = 0; i< input_line.length(); i++){

                if (input_line[i]==' ' && counter<3){
                    space[counter]=i;
                    counter++;
                }
            }

            array1[0]=atoi((input_line.substr(0, 2)).c_str());
            array1[1]=atoi((input_line.substr(space[0], 3)).c_str());
            array1[2]=atoi((input_line.substr(space[1], 3)).c_str());
            array1[3]=atoi((input_line.substr(space[2])).c_str());
            //printf("%d, %d, %d\n", space[0], space[1], space[2]);
                    //printf("%d, %d, %d, %d\n", array1[0], array1[1], array1[2], array1[3]);


        }

        if (acount==4)
            currentstep=3;
    }
    else if (currentstep==3)
    {
        b = atoi(input_line.c_str());
        //printf("b: %d\n", b);
        if (b!=0)
            currentstep=4;
    }
    else if (currentstep==4)
    {
        bcount++;

        if (bcount==b){
            int space[3];
            int counter = 0;
            //printf("%s\n", input_line.c_str());
            for (int i = 0; i< input_line.length(); i++){

                if (input_line[i]==' ' && counter<3){
                    space[counter]=i;
                    counter++;
                }
            }

            array2[0]=atoi((input_line.substr(0, 2)).c_str());
            array2[1]=atoi((input_line.substr(space[0], 3)).c_str());
            array2[2]=atoi((input_line.substr(space[1], 3)).c_str());
            array2[3]=atoi((input_line.substr(space[2])).c_str());
        }
        if (bcount==4)
            currentstep=5;
    }
    if (currentstep==5)
    {
        int result = 0;

        for (int i = 0; i< 4; i++)
        {
            for (int j=0; j<4; j++)
            {
                if (array1[i]==array2[j])
                    result++;
            }
        }


        if (result==1){
            for (int i = 0; i< 4; i++)
            {
                for (int j=0; j<4; j++)
                {
                    if (array1[i]==array2[j]){
                    result=array1[i];
                    i=5;
                    j=5;
                    }
                }
            }

            printf("Case #%d: %d\n", roundcount, result);
        }
        else if (result>1){
            printf("Case #%d: Bad magician!\n", roundcount);

        }
        else if (result==0){
            printf("Case #%d: Volunteer cheated!\n", roundcount);

        }
        //printf("\n");
        a = b = acount = bcount = 0;
        for (int i=0; i<4; i++)
            array1[i]=array2[i]=0;

        if (roundcount==rounds)
            currentstep=8;
        else
        currentstep = 1;

    }

    /*else if (currentstep==1)
    {
        roundcount++;

        //collect data, split


        //a = atoi((input_line.substr(0, input_line.find(" ")).c_str()));
        //b = atoi(input_line.substr(input_line.find(" ")+1).c_str());
        //printf("%s, a, b, %d, %d\n", input_line.c_str(), a, b);

        if (a!=0){
        currentstep=2;
        }
        else if(b!=0){
            currentstep=3;
        }
        else
            currentstep=4;

    }
    else if (currentstep ==2)
    {
        acount++;

        folders[input_line] =1;

        if (acount== a)
            currentstep =3;
    }
    else if (currentstep ==3)
    {
        bcount++;
        for (int i = 0; i< input_line.length(); i++){
                        //printf("%c\n", input_line[i]);

            if (input_line[i]=='/'){

            temp = input_line.substr(0, i);
                //printf("%s\n", temp.c_str());
            }
            if(temp!= ""){
                //check if in
                //ifnot in, add
                if (!folders[temp]){
                    folders[temp]=1;

                mkdircount++;
                }
            }
        }
        temp = input_line;
        //printf("%s\n", temp.c_str());

        if (!folders[temp]){
            folders[temp]=1;

            mkdircount++;
        }

        //printf("mkdircount : %d", mkdircount);
        if (bcount== b){
            currentstep =4;
        }
    }
    if (currentstep ==4)
    {
        //print round, mkdircount
        printf("Case #%d: %d\n", roundcount, mkdircount);
        a = b = 0;
        acount=0;

        bcount=0;
        mkdircount=0;
        if (roundcount==rounds)
            currentstep=8;
        else
        currentstep =1;
        folders.clear();

    }*/



    };


    return 0; //finish
}
