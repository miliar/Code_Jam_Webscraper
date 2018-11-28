#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
using namespace std;
int a[5][5],n,lamp=0;
void read()
{
    int i,j;
    memset(a,0,16);
    char s;
    for(i=1;i<=4;i++)
    {
    for(j=1;j<=4;j++)
    {
        scanf("%c",&s);
        if(s=='X')a[i][j]=1;
        if(s=='O')a[i][j]=2;
        if(s=='T')a[i][j]=3;
        if(s=='.'){a[i][j]=0;lamp=1;}
    }
    scanf("%c",&s);
    }
    
}
void print()
{
    int i,j;
    for(i=1;i<=4;i++)
    {for(j=1;j<=4;j++)
    cout<<a[i][j]<<" ";
    cout<<endl;
    }
}
int provx()
{
    int i,j,l=1;
    for(i=1;i<=4;i++)
    if(a[i][i]==2 || a[i][i]==0)l=0;
    if(l==1){return 1;}
    l=1;
    for(i=1;i<=4;i++)
    if(a[i][4-i+1]==2 || a[i][4-i+1]==0)l=0;
    if(l==1){return 1;}
    l=1;
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        if(a[i][j]==2 || a[i][j]==0)l=0;
        if(l==1){return 1;}
        l=1;
        for(j=1;j<=4;j++)
        if(a[j][i]==2 || a[j][i]==0)l=0;
        if(l==1){return 1;}
        l=1;
    }
    return 0;
}
int provy()
{
    int i,j,l=1;
    for(i=1;i<=4;i++)
    if(a[i][i]==1 || a[i][i]==0)l=0;
    if(l==1){return 1;}
    l=1;
    for(i=1;i<=4;i++)
    if(a[i][4-i+1]==1 || a[i][4-i+1]==0)l=0;
    if(l==1){return 1;}
    l=1;
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        if(a[i][j]==1 || a[i][j]==0)l=0;
        if(l==1){return 1;}
        l=1;
        for(j=1;j<=4;j++)
        if(a[j][i]==1 || a[j][i]==0)l=0;
        if(l==1){return 1;}
        l=1;
    }
    return 0;
}
int main()
{
    cin>>n;
    char s;
    scanf("%c",&s);
    int i;
    for(i=1;i<=n;i++)
    {
        read();
        //print();
        if(provx()==1)printf("Case #%d: X won\n",i); //cout<<"Case #"<<i<<": X won"<<endl;
        if(provy()==1)printf("Case #%d: O won\n",i); //cout<<"Case #"<<i<<": O won"<<endl;
        if(provx()==0 && provy()==0)
        {
            if(lamp==1)printf("Case #%d: Game has not completed\n",i); //cout<<"Case #"<<i<<": Game has not completed"<<endl;
            else printf("Case #%d: Draw\n",i); //cout<<"Case #"<<i<<": Draw"<<endl;
        }
        lamp=0;
    scanf("%c",&s);        
    }
    return 0;
}