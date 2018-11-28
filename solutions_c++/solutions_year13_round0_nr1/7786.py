#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<cctype>
#include<cmath>
#include<ctime>
#include<algorithm>
using namespace std;

#define SIZE 100000
#define MOD 1000000007
#define LL long long int
#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)
#define SWAP(a,b) { (a)=(a)+(b); (b)=(a)-(b); (a)=(a)-(b); }

char a[5][5];

bool winner(char ch)
{
    int i,j;
    bool flag=false;

    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(a[i][j]!=ch && a[i][j]!='T')
                break;
        }
        if(j==4) flag=true;

        for(j=0;j<4 && !flag;j++)
        {
            if(a[j][i]!=ch  && a[j][i]!='T')
                break;
        }
        if(j==4) flag=true;
    }
    for(i=0;i<4 && !flag;i++)
        if(a[i][i]!=ch  && a[i][i]!='T')
            break;
    if(i==4) flag=true;

    for(i=0;i<4 && !flag;i++)
        if(a[i][3-i]!=ch  && a[i][3-i]!='T')
            break;
    if(i==4) flag=true;

    return flag;
}

bool draw()
{
    int i,j;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            if(a[i][j]=='.')
                return false;
    return true;
}

int main()
{
    int t,T,i;

    scanf("%d",&T); //No of test cases.

    for(t=0;t<T;t++)
    {
        for(i=0;i<4;i++)
            cin>>a[i];
        cout<<"Case #"<<t+1<<": ";
        if(winner('X'))
            cout<<"X won\n";
        else if(winner('O'))
            cout<<"O won\n";
        else if(draw())
            cout<<"Draw\n";
        else
            cout<<"Game has not completed\n";
    }
	return 0;
}
