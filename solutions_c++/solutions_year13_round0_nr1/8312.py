#include <iostream>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#include<cstdio>
using namespace std;

string tic()
{
    string x[4],space;
    for(int i=0; i<4; i++)
    {
        cin>>x[i];

    }
    bool ch=false;
    if((x[0][0]=='X'||x[0][0]=='T')&&(x[1][1]=='X'||x[1][1]=='T')&&
            (x[2][2]=='X'||x[2][2]=='T')&&(x[3][3]=='X'||x[3][3]=='T'))
        return "X won";
    if((x[0][0]=='O'||x[0][0]=='T')&&(x[1][1]=='O'||x[1][1]=='T')&&
            (x[2][2]=='O'||x[2][2]=='T')&&(x[3][3]=='O'||x[2][2]=='T'))
        return "O won";
    if((x[0][3]=='X'||x[0][3]=='T')&&(x[1][2]=='X'||x[1][2]=='T')&&
            (x[2][1]=='X'||x[2][1]=='T')&&(x[3][0]=='X'||x[3][0]=='T'))
        return "X won";

    if((x[0][3]=='O'||x[0][3]=='T')&&(x[1][2]=='O'||x[1][2]=='T')&&
            (x[2][1]=='O'||x[2][1]=='T')&&(x[3][0]=='O'||x[3][0]=='T'))
        return "O won";






    for(int j=0; j<4; j++)
    {
        for(int i=0; i<4; i++)
        {
            if(x[j][i]=='X'||x[j][i]=='T')
            {
                ch=true;

            }
            else
            {ch=false;
                break;
                }
        }
        if(ch)
    return "X won";
    }



    for(int j=0; j<4; j++)
    {
        for(int i=0; i<4; i++)
        {
            if(x[j][i]=='O'||x[j][i]=='T')
            {
                ch=true;

            }
            else
                {ch=false;
                break;
                }
        }
         if(ch)
    return "O won";

    }


///////////////////////////

  for(int j=0; j<4; j++)
    {
        for(int i=0; i<4; i++)
        {
            if(x[i][j]=='X'||x[i][j]=='T')
            {
                ch=true;
            }
            else
            {ch=false;
                break;
                }
        }
        if(ch)
    return "X won";
    }



    for(int j=0; j<4; j++)
    {
        for(int i=0; i<4; i++)
        {
            if(x[i][j]=='O'||x[i][j]=='T')
            {
                ch=true;

            }
            else
                {ch=false;
                break;
                }
        }
   if(ch)
    return "O won";
    }



////////////////////




for(int j=0; j<4; j++)
    {
        for(int i=0; i<4; i++)
        {
            if(x[j][i]!='.')
            {
                ch=true;

            }
            else
                {ch=false;
                break;
                }

        }

if(ch)
return "Draw";


}
return "Game has not completed";
}




int main()
{
    READ("A-small-attempt6.in");
   WRITE("C-large-1.out");
    int time,i=1;

    cin>>time;
     while(i<=time){
    cout<<"Case #"<<i<<": "<<tic()<<endl;

    i++;
    }
    return 0;
}
//////////////////////////////////////////////


