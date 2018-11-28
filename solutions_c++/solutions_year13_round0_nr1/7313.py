#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
int main()
{
    int t, notover, f, c, pos;
    int d=0;
    string s[4];
    string r="0";
    scanf("%d", &t);

    for(int i=0;i<t;i++)
    {
        for(int y=0;y<4;y++)
        {
            cin>>s[y];
        }
          notover=0;
        for(int j=0;j<4;j++)
        {
            f=0;
            c=0;
            pos=0;
            r="0";
            int counter=0;
            int e=0;

            for(int p=0;p<4;p++)
            {
                if(s[j][p]=='.')
                {notover=1;
                break;}

            }

               for( e=0;e<4;e++)
               {
                    if (s[j][e]=='X' || s[j][e]=='T')
                   {counter+=1;}}
                   if (counter==4)
                    {r="X won";
                     break;}
                   else
                    counter=0;


               for(e=0;e<4;e++)
               {
                   if (s[e][j]=='X' || s[e][j]=='T')
                    {counter+=1;}}
                   if (counter==4)
                    {r="X won";
                    break;}
                   else counter=0;

                   for(e=0;e<4;e++)
               {
                   if (s[e][e]=='X' || s[e][e]=='T')
                    {counter+=1;}}
                   if (counter==4)
                    {r="X won";
                    break;}
                   else counter=0;


                    for(e=0;e<4;e++)
               {
                   if (s[e][3-e]=='X' || s[e][3-e]=='T')
                    {counter+=1;}}
                   if (counter==4)
                    {r="X won";
                    break;}
                   else counter=0;


                   if(r=="0")
                   {
                    for(e=0;e<4;e++)
                    {
                    if (s[j][e]=='O' || s[j][e]=='T')
                   {counter+=1;}}
                   if (counter==4)
                    {r="O won";
                     break;}
                   else counter=0;

               for(e=0;e<4;e++)
               {
                   if (s[e][j]=='O' || s[e][j]=='T')
                    {counter+=1;}}
                   if (counter==4)
                    {r="O won";
                    break;}
                   else counter=0;



                   for(e=0;e<4;e++)
               {
                   if (s[e][e]=='O' || s[e][e]=='T')
                    {counter+=1;}}
                   if (counter==4)
                    {r="O won";
                    break;}
                   else counter=0;


                    for(e=0;e<4;e++)
               {
                   if (s[e][3-e]=='O' || s[e][3-e]=='T')
                    {counter+=1;}}
                   if (counter==4)
                    {r="O won";
                    break;}
                   else counter=0;
                   }

               if(r!="0")
                break;

        }
        if(r=="0" && notover==0)
            {r="Draw";}
        else if(r=="0" && notover==1)
        {
        r="Game has not completed";
        }

        cout<<"Case #"<<i+1<<": "<<r<<endl;

    }

}
