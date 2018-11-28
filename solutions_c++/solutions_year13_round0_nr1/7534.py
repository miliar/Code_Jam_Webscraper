//https://code.google.com/codejam/contest/2270488/dashboard
#include<iostream>
#include<stdio.h>
#include<fstream>
#include<stdlib.h>

using namespace std;

bool check_sum(int sum)
{
    bool won=false;
    if(sum == 348 || sum ==352 )
    {
        won = true;
        // X wins
        cout<<"X won"<<endl;
       // break;

    }
    else
    {
        if(sum == 316 || sum == 321 )
        {
            won = true;
            //O wins
            cout<<"O won"<<endl;
            //break;
        }

    }
                return won;
}

int main()
{
     freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    int c=0;
    cin>>t;

    while(t--)
    {
        c++;
        cout<<"Case #"<<c<<": ";
        bool won = false;
        int sum=0;
        int space=0;
        char a[4][4];
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        for(int i=0;i<4;i++)
        {
            sum = 0;
            for(int j=0;j<4;j++)
            {
                //cin>>a[i][j];
                if(a[i][j]=='.')
                {
                    space++;
                }
                sum = sum + a[i][j];
            }
            won = check_sum(sum);
            if(won)
                break;
        }
        if(!won)
        {

            for(int i=0;i<4;i++)
            {
                sum=0;
                for(int j=0;j<4;j++)
                {
                    sum=sum+a[j][i];
                }
                won = check_sum(sum);
                if(won)
                    break;
            }
            if(!won)
            {
                sum=0;
                for(int i=0;i<4;i++)
                    sum=sum+a[i][i];
                won = check_sum(sum);
                if(!won)
                {
                    sum=0;
                    for(int i=0;i<4;i++)
                        sum=sum+a[i][3-i];
                    won = check_sum(sum);
                    if(!won)
                    {
                        if(space > 0)
                        {
                            cout<<"Game has not completed"<<endl;
                        }
                        else
                        {
                            cout<<"Draw"<<endl;
                        }
                    }
                }

            }
        }

    }
}
