#include<iostream>

using namespace std;


int main()
{
    char a[10][10];
    int t,q,i,j,flag,count;
    cin>>t;
    for(q=0; q<t; q++)
    {
        for(i=0; i<4; i++)
        {


                cin>>a[i];

        }
        flag=0;
        for(i=0; i<4; i++)
        {
            count=0;
              for(j=0; j<4; j++)
              {
                  if(a[i][j]=='X' || a[i][j]=='T')
                  {
                      count++;
                  }
              }
              if(count==4)
              {
                  cout<<"Case #"<<q+1<<": "<<"X won"<<endl;
                  flag=1;
                  break;
              }
        }
        if(flag==1)
        continue;

        flag=0;
        for(j=0; j<4; j++)
        {
            count=0;
              for(i=0; i<4; i++)
              {
                  if(a[i][j]=='X' || a[i][j]=='T')
                  {
                      count++;
                  }
              }
              if(count==4)
              {
                  cout<<"Case #"<<q+1<<": "<<"X won"<<endl;
                  flag=1;
                  break;
              }
        }
        if(flag==1)
        continue;

        if(a[0][0]=='X' || a[0][0]=='T' )
        {
            if(a[1][1]=='X' || a[1][1]=='T' )
            {
                if(a[2][2]=='X' || a[2][2]=='T' )
                {
                        if(a[3][3]=='X' || a[3][3]=='T' )
                        {
                              cout<<"Case #"<<q+1<<": "<<"X won"<<endl;
                              continue;
                         }
                }
            }
        }

        if(a[0][3]=='X' || a[0][3]=='T' )
        {
            if(a[1][2]=='X' || a[1][2]=='T' )
            {
                if(a[2][1]=='X' || a[2][1]=='T' )
                {
                        if(a[3][0]=='X' || a[3][0]=='T' )
                        {
                              cout<<"Case #"<<q+1<<": "<<"X won"<<endl;
                              continue;
                         }
                }
            }
        }

        flag=0;
        for(i=0; i<4; i++)
        {
            count=0;
              for(j=0; j<4; j++)
              {
                  if(a[i][j]=='O' || a[i][j]=='T')
                  {
                      count++;
                  }
              }
              if(count==4)
              {
                  cout<<"Case #"<<q+1<<": "<<"O won"<<endl;
                  flag=1;
                  break;
              }
        }
        if(flag==1)
        continue;

        flag=0;
        for(j=0; j<4; j++)
        {
            count=0;
              for(i=0; i<4; i++)
              {
                  if(a[i][j]=='O' || a[i][j]=='T')
                  {
                      count++;
                  }
              }
              if(count==4)
              {
                  cout<<"Case #"<<q+1<<": "<<"O won"<<endl;
                  flag=1;
                  break;
              }
        }
        if(flag==1)
        continue;

        if(a[0][0]=='O' || a[0][0]=='T' )
        {
            if(a[1][1]=='O' || a[1][1]=='T' )
            {
                if(a[2][2]=='O' || a[2][2]=='T' )
                {
                        if(a[3][3]=='O' || a[3][3]=='T' )
                        {
                              cout<<"Case #"<<q+1<<": "<<"O won"<<endl;
                              continue;
                         }
                }
            }
        }

        if(a[0][3]=='O' || a[0][3]=='T' )
        {
            if(a[1][2]=='O' || a[1][2]=='T' )
            {
                if(a[2][1]=='O' || a[2][1]=='T' )
                {
                        if(a[3][0]=='O' || a[3][0]=='T' )
                        {
                              cout<<"Case #"<<q+1<<": "<<"O won"<<endl;
                              continue;
                         }
                }
            }
        }

        flag=0;

        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                 if(a[i][j]=='.')
                 {
                     cout<<"Case #"<<q+1<<": "<<"Game has not completed"<<endl;
                     flag=1;
                     break;
                 }
            }
            if(flag==1)
            break;
        }
        if(flag==1)
        continue;

        cout<<"Case #"<<q+1<<": "<<"Draw"<<endl;


    }
    return 0;
}
