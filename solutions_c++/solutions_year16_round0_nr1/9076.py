#include<iostream>
#include<fstream>
#include<string.h>
#include <stdio.h>
using namespace std;
int main()
{
    int input=0,flag[10]={0},t=0,digit[100]={0},i=0,mainFlag=0,baseInput,answer[100]={0},z=0,input2,j=0;
    //char finalanswer[100][10]={'0'};
    ifstream inf;
    ofstream onf;
    inf.open("A-large.in");
    inf >> t;
    for(int ai=0; ai<t; ai++)
    {
        inf >> baseInput;
        mainFlag=0;
        j=0;
        for(i=0;i<10;i++)
            flag[i]=0;
        for(int run=0; run<100; run++)
        {
            if(baseInput==0)
            {
                mainFlag=1;
                input2=0;
            }
            if(mainFlag!=0)
            {
                answer[z]=input2;
                z++;
                break;
            }
            else
            {
                int n=0;
                j++;
                input=baseInput*j;
                input2=input;
                for(i=0; input!=0; i++) ///when input is 0 dikkat
                {
                    digit[i]=input%10;
                    input=input/10;
                    n++;
                }
                for(i=0; i<n; i++)
                    flag[digit[i]]=1;
                for(i=0; i<10; i++)
                {
                    if(flag[i]==1)
                        mainFlag=1;
                    else
                    {
                        mainFlag=0;
                        break;
                    }
                }
            }
        }
    }
    onf.open("out.txt");
    /*for(i=0; i<t; i++)
        {cout << "Case #" <<i+1<<": ";
        if(answer[i]==0)
            cout << "INSOMNIA";
        else
            cout << answer[i];
        cout << endl;}*/
    for(i=0; i<t; i++)
        {onf << "Case #" <<i+1<<": ";
        if(answer[i]==0)
            onf << "INSOMNIA";
        else
            onf << answer[i];
        onf << endl;}
}
