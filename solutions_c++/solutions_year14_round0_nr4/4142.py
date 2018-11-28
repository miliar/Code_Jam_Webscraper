#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <iomanip>
#include <math.h>

using namespace std;

void BubbleSort(float *num)
{

     return;   //arrays are passed to functions by address; nothing is returned
}

int main()
{
    int cases=0;
    string temp;
    int N=0,N1=0;
    int fairScore=0,cheatScore=0;
    float naomiStone, kenStone;
    int count=0;
    int flag2=1;
    int i, j, flag=0;
    float tempf;
    int numLength;

    ofstream ans;
    ans.open ("ansWar.txt");
    ifstream in;
    in.open("a.txt");

    in>>temp;
    cases=atof(temp.c_str());



    for(int a=0;a<cases;a++)
    {
        fairScore=0;
        cheatScore=0;

        in>>temp;
        N=atof(temp.c_str());

        float naomi[N],ken[N];
        int naomiUsedFair[N],kenUsedFair[N];
        int naomiUsedCheet[N],kenUsedCheet[N];

        for(int j=0;j<N;j++)
        {
            naomiUsedFair[j]=-1;
            kenUsedFair[j]=-1;
            naomiUsedCheet[j]=-1;
            kenUsedCheet[j]=-1;
        }

        for(int j=0;j<N;j++)
        {
            in>>temp;
            naomi[j]=atof(temp.c_str());
        }
        for(int j=0;j<N;j++)
        {
            in>>temp;
            ken[j]=atof(temp.c_str());
        }

         for (int passes = 0;  passes < N - 1;  passes++)
         {
          for (int j = 0;  j < N - passes - 1;  j++)
          {
           if (ken[j] > ken[j+1])
           {
            tempf = ken[j];
            ken[j] = ken[j+1];
            ken[j+1]=tempf;
           }
          }
         }

         for (int passes = 0;  passes < N - 1;  passes++)
         {
          for (int j = 0;  j < N - passes - 1;  j++)
          {
           if (naomi[j] > naomi[j+1])
           {
            tempf = naomi[j];
            naomi[j] = naomi[j+1];
            naomi[j+1]=tempf;
           }
          }
         }

        fairScore=0;
        cheatScore=0;

        count=0;
        N1=N;
        for(int a=N-1,b=0;a>=0;a--,b++)
        {
            if(naomi[a]>ken[a])
            {
                kenUsedCheet[count]=a;
                naomiUsedCheet[count]=a;
                count++;
                N1--;
                cheatScore++;
            }
            else
            {
                break;
            }
        }
        for(int a=0,b=N1-1,c=0;a<N1;a++,b--)
        {
            if(naomi[a]>ken[c])
            {
                kenUsedCheet[count]=c;
                naomiUsedCheet[count]=a;
                count++;
                cheatScore++;
                c++;
            }
            else
            {
                kenUsedCheet[count]=b;
                naomiUsedCheet[count]=a;
                count++;
            }
        }

        count=0;
        for(int a=0;a<N;a++)
        {
            naomiUsedFair[a]=a;
            flag2=1;
            for(int b=0;b<N && flag2==1;b++)
            {
                flag=0;
                for(int c=0;c<N  ;c++)
                {
                    if(kenUsedFair[c]==b) flag=1;
                }
                if(flag) continue;
                if(naomi[a]<ken[b])
                {
                    kenUsedFair[count]=b;
                    count++;
                    flag2=0;
                }
            }
            if(flag2) fairScore++;
        }

        ans<<"Case #"<<a+1<<": "<<cheatScore<<" "<<fairScore<<endl;
        cout<<"Case #"<<a+1<<": "<<cheatScore<<" "<<fairScore<<endl;

    }


    return 0;
}
