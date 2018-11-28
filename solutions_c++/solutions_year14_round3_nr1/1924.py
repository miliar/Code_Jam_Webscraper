#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

int main()
{
    fstream fil;
    fil.open("A.txt",ios::in);
    char lin[100];
    int cases;
    fil.getline(lin,100);
    cases = atoi(lin);
    for(int j=0;j<cases;j++)
    {
        cout << "\nCase #" << j+1 << ": ";
        int A, B, check=0;
        char A1[10], B1[10];
        fil.getline(lin,100);
        int i;
        for(i=0;i<strlen(lin);i++)
        {
            if(lin[i]=='/')
            {
                A1[i]='\0';
                check=i;
                i++;
            }
            if(!check)
                A1[i]=lin[i];
            else
                B1[i-check-1]=lin[i];
        }
        B1[i-check-1]='\0';
        A = atoi(A1);
        B = atoi(B1);
        int count=0;
        check=0;
        int stopcount=0;
        while((count<=40)&&(!check))
        {
            
            if(A<B)
            {
                count++;
                A*=2;
                if(A>B)
                {
                    if(!stopcount)
                        stopcount=count;
                    A-=B;
                }
            }
            else if (A==B)
            {
                check++;
            }
        }
        if((!check)||(count>40))
            cout << "impossible";
        else if (stopcount)
            cout << stopcount;
        else
            cout << count;
        
    }
    return 0;
}