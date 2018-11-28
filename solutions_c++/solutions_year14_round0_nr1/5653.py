#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
int ans1, ans2, init[4][4], finl[4][4];
int ans3=-1;
char ans4[30]="";

void solution()
{
    int nm=0, sol=-1;
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if(init[ans1-1][i]==finl[ans2-1][j])
            {
                nm++;
                sol=init[ans1-1][i];
            }
        }
    }
    if(nm==0)
        strcpy(ans4, "Volunteer cheated!");
    else if(nm==1)
        ans3=sol;
    else
        strcpy(ans4, "Bad magician!");
}

int main()
{
    int n, m=1, j, i;
    ifstream f2("A-small-practice.in");
    f2>>n;
    ofstream f3("A-small-practice.out", ios::app);
    while(m<=n)
    {
        ans3=-1;
        f2>>ans1;
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
                f2>>init[i][j];
        }
        f2>>ans2;
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
                f2>>finl[i][j];
        }
        solution();
        if(ans3==-1)
            f3<<"Case #"<<m<<": "<<ans4<<endl;
        else
            f3<<"Case #"<<m<<": "<<ans3<<endl;
        m++;
    }
    return 0;
}

