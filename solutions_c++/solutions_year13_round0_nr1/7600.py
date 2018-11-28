#include <fstream>
#include <iostream>
#include <conio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    int counter, flag, counter2, dot_count;
    char ch, ch2;
    char tic[4][4];
    ifstream fin("A.in");
    ofstream fout("A.out");
    fin>>T;
    for(int i=0; i<T; i++)
    {
        flag = 0;
        dot_count = 0;
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
            {
                fin>>tic[j][k];
                if(tic[j][k] == '.')
                    dot_count++;
            }


        for(int j=0; j<4; j++)
        {
            counter = 1;
            counter2 = 1;
            ch = tic[0][j];
            ch2 = tic[j][0];
            for(int k=1; k<4; k++)
            {
                if(ch == tic[k][j])
                    counter++;
                else if(tic[k][j] == 'T')
                    counter++;
                if(ch2 == tic[j][k])
                    counter2++;
                else if(tic[j][k] == 'T')
                    counter2++;
            }
            if(counter == 4 && ch!='.')
            {
                fout<<"Case #"<<i+1<<": "<<ch<<" won"<<endl;
                flag=1;
                break;
            }
            else if(counter2 == 4 && ch2!='.')
            {
                fout<<"Case #"<<i+1<<": "<<ch2<<" won"<<endl;
                flag=1;
                break;
            }
        }
        if(flag==1)
        {
            //fin>>ch;
            continue;
        }
        counter = 1;
        counter2 = 1;
        ch = tic[0][0];
        ch2 = tic[0][3];
        for(int j=1; j<4; j++)
        {
            if(ch == tic[j][j])
                counter++;
            else if(tic[j][j] == 'T')
                counter++;
            if(ch2 == tic[j][3-j])
                counter2++;
            else if(tic[j][3-j] == 'T')
                counter2++;
        }
        if(counter == 4 && ch!='.')
            {
                fout<<"Case #"<<i+1<<": "<<ch<<" won"<<endl;
                continue;
            }
        else if(counter2 == 4 && ch2!='.')
            {
                fout<<"Case #"<<i+1<<": "<<ch2<<" won"<<endl;
                continue;
            }
        if(dot_count == 0)
            fout<<"Case #"<<i+1<<": Draw"<<endl;
        else
            fout<<"Case #"<<i+1<<": Game has not completed"<<endl;
        //fin>>ch;
    }

}
