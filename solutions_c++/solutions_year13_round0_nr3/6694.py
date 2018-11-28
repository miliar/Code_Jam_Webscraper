#include <iostream>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<cmath>
#include<math.h>

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


//////////////////////////////
bool is(int x){
queue<int>q;
queue<int>q2;
stack<int>s;
int n;
while(x!=0)
{
    n=x%10;
    q.push(n);
    x=x/10;
}



while(!q.empty()){
s.push(q.front());
q2.push(q.front());
q.pop();
}



while(!q2.empty())
{
  if(s.top()==q2.front()){
  s.pop();
  q2.pop();
  continue;
  }
  return false;
}


return true;
}


///////////////////////////////////////
bool s(int x){
int y;
y=sqrt(x);
if(y*y==x&&is(y))
return true;
return false;
}



int main()
{
   READ("C-small-attempt1 (1).in");
   WRITE("C-large-1.out");
    int time,upper,lower,i=1;

    cin>>time;
     while(i<=time){
         cin>>lower;
         cin>>upper;
         int count=0;
    for(lower;lower<=upper;lower++)
      {
       if(is(lower)&&s(lower))
       {count++;

       }

      }
      cout<<"Case #"<<i<<": "<< count<<endl;
    i++;
    }
    return 0;
}
//////////////////////////////////////////////


