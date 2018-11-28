#include<iostream>
#include<cstdio>
#include<map>
#include<algorithm>
#include<sstream>
#include<string>
#include<cstring>
#include<cmath>
#include<queue>
#include<cstdlib>
#include<vector>
#define MAXLEN 100000
#define INF 10000000000
#define WHITE 0
#define GRAY 1
#define BLACK 2

using namespace std;
bool vcheck(int i,int j,char c,char a[][5])
{
//    cout<<a[i][j]<<"\n";
//    cout<<"vcheck() "<<i<<" "<<j<<"\n";
    if(a[i][j]=='T')
    c = a[i][j+1];
    if(c=='.')
    return false;

    int k = i;
    while(k<4 && (a[k][j]==c || a[k][j]=='T'))
    {
        k++;
    }
    if(k==4) return true;
    else return false;
}

bool hcheck(int i,int j,char c,char a[][5])
{
//    cout<<a[i][j]<<"\n";
//    cout<<"hcheck() "<<i<<" "<<j<<"\n";
    if(a[i][j]=='T')
    c = a[i][j+1];
    if(c=='.')
    return false;

    int k = j;
    while(k<4 &&(a[i][k]==c || a[i][k]=='T') )
    {
        k++;
    }
    if(k==4) return true;
    else return false;
}
bool diagonal(int i,int j,char c,char a[][5])
{
//    cout<<a[i][j]<<"\n";
//    cout<<"diagonal "<<i<<" "<<j<<"\n";
    if(i == 0 && j==0)
    {
        if(a[i][j]=='T')
        c = a[i+1][j+1];
        if(c=='.')
    return false;
        while(i<4 && j<4 &&(a[i][j]==c || a[i][j]=='T') )
        {
            i++;j++;
        }
        if(i==4 && j==4) return true;
        else return false;
    }
    else
    {
        if(a[i][j]=='T')
        c = a[i+1][j-1];
        if(c=='.')
    return false;
        while(i>=0 && j<4 &&(a[i][j]==c || a[i][j]=='T') )
        {
            j--;i++;
        }
        if(i==4 && j<0) return true;
        else return false;
    }
}
int main()
{
    char a[5][5];
    char winner;
    int t;
    scanf("%d\n",&t);
    int count = 1;
    while(t--)
    {
        bool found = false;
        for(int i=0;i<4;i++)
            scanf("%s",a[i]);
//        for(int i=0;i<4;i++)
//            for(int j=0;j<4;j++)
//                cout<<a[i][j]<<"\n";
        int i=0;
        int dot=0;
        for(int j=0;j<4 && (!found); j++)
        {
            if(a[i][j] != '.')
            {
                if(j==0 && diagonal(i,j,a[i][j],a))
                {
                    found = true;
                    if(a[i][j]=='T')
                    winner = a[i+1][j+1];
                    else
                    winner = a[i][j];
                    break;
                }
                if(j==3 && diagonal(i,j,a[i][j],a))
                {
                    found = true;
                    if(a[i][j]=='T')
                    winner = a[i+1][j-1];
                    else
                    winner = a[i][j];
                    break;
                }
                if(vcheck(i,j,a[i][j],a))
                {
                    found = true;
                    if(a[i][j]=='T')
                    winner = a[i+1][j];
                    else
                    winner = a[i][j];
                    break;
                }
            }
            else dot++;
        }
        int j=0;
        for(i=0;i<4 && (!found) ;i++)
        {
            if(a[i][j] != '.')
            {
                if(hcheck(i,j,a[i][j],a))
                {
                    winner = a[i][j];
                    found = true;
                    break;
                }
            }
            else dot++;
        }
        printf("Case #%d: ",count++);
        if((!found) && dot==0)
        {
            printf("Draw\n");
        }
        else if((!found) && dot>0)
        {
            printf("Game has not completed\n");
        }
        else if(found)
        {
            printf("%c won\n",winner);
        }

    }
    return 0;
}
