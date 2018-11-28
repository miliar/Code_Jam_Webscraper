#include <bits/stdc++.h>
using namespace std;

    int steps=0;
    int numInput[100];

    void reverseArray(int cakes[])
    {
        int i=0;
        while(cakes[i]!=0)
        {
          cakes[i]=-cakes[i];
          i++;
        }



    }

    void  calculatesteps(int cakesNumStack[])
    {

        int i=99;
        while(cakesNumStack[i]>=0 && i>=0)
        {
          cakesNumStack[i]=0;
          i-- ;

        }


        //cout<<endl<<i<<endl;

        if(i>=0)
        {
        reverseArray(cakesNumStack);
        steps++;
        calculatesteps(cakesNumStack);
        }

        else
        {
        return;
        }



    }

    void convertInput(char input[])
    {
        int i;
        while(input[i]=='+' or input[i]=='-')
    {
        if (input[i]=='+')
            numInput[i]=1;
        else
            numInput[i]=-1;

        i++;
    }

    }

int main()
{
    int noCase;
    char input[100];
    int soln[100];
    ifstream fin ( "C:/Users/6030777/Desktop/input.txt" );
    ofstream fout ( "C:/Users/6030777/Desktop/output.txt" );
    fin>>noCase;
    for(int n=0;n<noCase;n++)
    {
    fin>>input;
    steps=0;
    convertInput(input);
    for(int i=0;i<100;i++)
    //cout<<numInput[i];
    calculatesteps(numInput);
    //cout<<endl;
    soln[n]=steps;

    }
    for(int n=0;n<noCase;n++)
    {
      fout<<"Case #"<<n+1<<": "<<soln[n]<<endl;
    }
    return 0;
}
