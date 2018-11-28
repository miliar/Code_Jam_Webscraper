#include <iostream>
#include <conio.h>
#include <math.h>
#include <fstream>

using namespace std;

int fair (int a) {
    int b; 
    int c=0;
    b=a;
    do {
        c = ((c*10) + (b%10));
        b=b/10;
    }
    while (b!=0); 
    if (c==a)
    {
             return 1;
    }
    else
    {
        return 0;
    } 
};
int square (int s, int t) {
    int d;
    int e=0;
    for (int i=s; i<=t; i++)
    {
        if (fair(i) == 1)
        {
                 d=sqrt(i);  
        }
        if (d*d == i)
        {
                if (fair(d) == 1)
                {
                       e+=1;
                }
        }     
    }
    return e;
};
int main () {
    fstream inFile;
    int a;
    int b[2];
    int c[100][2];
    inFile.open("C-small-attempt2.in");
    inFile>>a;
    for (int i=0; i<a; i++)
    {
        for (int j=0; j<2; j++)
        {
            if (!(cin))
            cin.clear();
            inFile>>b[j];
        }
        c[i][0]=(i+1);
        c[i][1]=square(b[0], b[1]);
    }
    inFile.close();
    inFile.open ("Output.txt");
    for (int k=0; k<a; k++)
    {
        inFile<<"Case #"<<c[k][0]<<": "<<c[k][1]<<"\n";
    }
    inFile.close();
    getch();
}
    
