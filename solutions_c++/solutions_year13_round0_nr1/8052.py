#include<iostream>
#include<stdlib.h>
using namespace std;
void init(char a[3][3],int& f,int &x,int &y)
{
    f=0;
    for(int i=0;i<3;i++)
    {

    for(int j=0;j<3;j++)
    {
        a[i][j]='_';
    }
    }
    x=0;y=0;
}
void mark(char a[3][3],int p,int flag)
{
    int r,c,temp;
    r=(p-1)/3;
    temp=(p%3)-1;
    if(temp<0)
    c=2;
    else c=temp;
    if(flag%2==0)
    a[r][c]='x';
    else a[r][c]='o';

}
void disp(char a[3][3])
{
    for(int i=0;i<3;i++)
    {
        cout<<"\n";
        for(int j=0;j<3;j++)
        {
            if(a[i][j]=='x' || a[i][j]=='o')
            cout<<" "<<a[i][j];
            else cout<<" _";
        }
    }
}
int xwin(char a[3][3])
{

    for(int i=0;i<3;i++)
    {

    if(a[i][0]=='x'&&a[i][1]=='x'&&a[i][2]=='x' || a[0][i]=='x' && a[1][i]=='x' && a[2][i]=='x')
    {
        return 1;
    }
    }
    if(a[0][0]=='x'&&a[1][1]=='x'&&a[2][2]=='x'||a[0][2]=='x'&&a[1][1]=='x'&&a[2][0]=='x')
    return 1;
    else return 0;
}
int ywin(char a[3][3])
{

    for(int i=0;i<3;i++)
    {

    if(a[i][0]=='o'&&a[i][1]=='o'&&a[i][2]=='o' || a[0][i]=='o' && a[1][i]=='o' && a[2][i]=='o')
    {
        return 1;
    }
    }
    if(a[0][0]=='o'&&a[1][1]=='o'&&a[2][2]=='o'||a[0][2]=='o'&&a[1][1]=='o'&&a[2][0]=='o')
    return 1;
    else return 0;
}
main()
{
    int f,p,x=0,y=0,r,c,temp;
    int ne=1;
    char a[3][3],m,ch='y';
    while(ch=='y')
    {
        if(ne==1)
        init(a,f,x,y);
        ne=0;
    cout<<"\nEnter the position to mark\n";
    cout<<"player "<<((f%2)+1)<<"\n";
    cin>>p;
    r=(p-1)/3;
    temp=(p%3)-1;
    if(temp<0)
    c=2;
    else c=temp;
    if(p>9||p<1)
    {
        cout<<"\nINVALID POSITION\n";
        continue;
    }
    else if(a[r][c]=='x'||a[r][c]=='0')
    {
        cout<<"\nALREADY MARKED\n";
        continue;
    }
   else
    f++;
    mark(a,p,f);
    x=xwin(a);
    y=ywin(a);
   disp(a);
   if(x==1)
   {

       cout<<"\nPLAYER 2 WINS !!\n";
       cout<<"\nDO YOU WANT TO CONTINUE?(y/n)";
       cin>>ch;
       ne=1;
   }
      if(y==1)
   {

       cout<<"\nPLAYER 1 WINS !!\n";
       cout<<"\nDO YOU WANT TO CONTINUE?(y/n)";
       cin>>ch;
       ne=1;
   }

   if(f==9 && x==0 && y==0)
    {
        cout<<"\nMATCH DRAWN\n";
         cout<<"\nDO YOU WANT TO CONTINUE?(y/n)";
       cin>>ch;
       ne=1;

    }



    }
}
