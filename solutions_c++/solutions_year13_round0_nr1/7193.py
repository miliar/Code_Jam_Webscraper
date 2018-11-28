#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<queue>
#include<vector>
#include<map>
#include<string>
#include<cstring>

using namespace std;

char a[6][6];int n;

void read()
{
    int i,j;
    for(i=1;i<=4;i++)
    for(j=1;j<=4;j++)
    {
        cin>>a[i][j];
    }
}

void check(int x)
{
    int br=0,l=0,ll=0,i,j;
    cout<<"Case #"<<x<<": ";
    for(j=1;j<=4;j++)
    
    {
        for(i=1;i<=4;i++)
        {
            if(a[i][j]=='X')br++;
            if(a[i][j]=='T'){br++;l=1;}
            if(a[i][j]=='.')br=5;
        }
        if(br==4){cout<<"X won\n";return;}
        if(br==0||(br==1&&l)){cout<<"O won\n";return;}
    
        br=0;l=0;
    }
    
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            if(a[i][j]=='X')br++;
            if(a[i][j]=='T'){br++;l=1;}
            if(a[i][j]=='.')br=5;
        }
        if(br==4){cout<<"X won\n";return;}
        if(br==0||(br==1&&l)){cout<<"O won\n";return;}
        
        br=0;l=0;
    }
    
    for(i=1;i<=4;i++)
    {
        if(a[i][i]=='X')br++;
        if(a[i][i]=='T'){br++;l=1;}
        if(a[i][i]=='.')br=5;
    }
    if(br==4){cout<<"X won\n";return;}
    if(br==0||(br==1&&l)){cout<<"O won\n";return;}
    
    br=0;l=0;
    
    for(i=4;i>=1;i--)
    {
        if(a[i][4-i+1]=='X')br++;
        if(a[i][4-i+1]=='T'){br++;l=1;}
        if(a[i][4-i+1]=='.')br=5;
    }
    
    if(br==4){cout<<"X won\n";return;}
    if(br==0||(br==1&&l)){cout<<"O won\n";return;}
    
    br=0;l=0;
    
    for(i=1;i<=4;i++)
    for(j=1;j<=4;j++)
    if(a[i][j]=='.'){cout<<"Game has not completed\n";return;}
    
    cout<<"Draw\n";
}

int main()
{
    int i;
    cin>>n;
    
    for(i=1;i<=n;i++)
    {
        read();
        check(i);
    }
    return 0;
}