/*
Author: Shu LIN
Data: 2012/4/14
language: C++
*/

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;


char Data[4][4];


bool judge1(int j,char ch)
{
    //hang
    if(Data[j][0]==ch||Data[j][0]=='T')
    {
        if(Data[j][1]==ch||Data[j][1]=='T')
        {
            if(Data[j][2]==ch||Data[j][2]=='T')
            {
                if(Data[j][3]==ch||Data[j][3]=='T')
                {
                    return true;
                }
            }
        }
    }
    return false;
}

bool judge2(int k,char ch)
{
    if(Data[0][k]==ch||Data[0][k]=='T')
    {
        if(Data[1][k]==ch||Data[1][k]=='T')
        {
            if(Data[2][k]==ch||Data[2][k]=='T')
            {
                if(Data[3][k]==ch||Data[3][k]=='T')
                {
                    return true;
                }
            }
        }
    }
    return false;
}

bool judge3(char ch)
{
    if(Data[0][0]==ch||Data[0][0]=='T')
    {
        if(Data[1][1]==ch||Data[1][1]=='T')
        {
            if(Data[2][2]==ch||Data[2][2]=='T')
            {
                if(Data[3][3]==ch||Data[3][3]=='T')
                    return true;
            }
        }
    }

    if(Data[0][3]==ch||Data[0][3]=='T')
    {
        if(Data[1][2]==ch||Data[1][2]=='T')
        {
            if(Data[2][1]==ch||Data[2][1]=='T')
            {
                if(Data[3][0]==ch||Data[3][0]=='T')
                    return true;
            
            }
        }
    }
    return false;
}
//1:X..2:O..3:Draw..4:Game has not completed
int judge()
{
    bool Draw_flag=false;
    // bool Com_Flag=false;
    for(int i=0;i<4;i++)
    {
        if(judge1(i,'X')||judge2(i,'X'))
        {
            return 1;
        }
        if(judge2(i,'O')||judge1(i,'O'))
        {
            return 2;
        }
        if(judge3('X'))
            return 1;
        if(judge3('O'))
            return 2;
    }
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(Data[i][j]=='.')
            {
                Draw_flag=true;
                break;
            }
        }
    }
    if(!Draw_flag)
    {
        return 3;
    }
    return 4;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int TT;
    scanf("%d",&TT);
    for(int idx=1;idx<=TT;idx++)
    {
        for(int i=0;i<4;i++)
        scanf("%s",&Data[i]);
        printf("Case #%d: ",idx);
        if(judge()==1)
        {
            printf("X won\n");
            continue;
        }
        if(judge()==2)
        {
            printf("O won\n");
            continue;
        }
        if(judge()==3)
        {
            printf("Draw\n");
            continue;
        }
        if(judge()==4)
        {
            printf("Game has not completed\n");
            continue;
        }
    }

    return 0;
}






