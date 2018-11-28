#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
    int test,i,j,x=1;
    scanf("%d",&test);
    while(test--)
    {
        char arr[4][4];
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>arr[i][j];
        int c_o=0,c_t=0,c_x=0,d=0;
        //Right_Diagonal
        for(i=0;i<4;i++)
        {
            if(arr[i][i]=='X')
                c_x++;
            if(arr[i][i]=='O')
                c_o++;
            if(arr[i][i]=='T')
                c_t++;
        }
        if(((c_o==3)&(c_t==1))|(c_o==4))
        {
            d=1;
            cout<<"Case #"<<x<<": O won\n";
            //cout<<endl;
            x++;
        }
       else if(((c_x==3)&(c_t==1))|(c_x==4))
        {
            d=1;
            cout<<"Case #"<<x<<": X won\n";
            //cout<<endl;
            x++;
        }
        c_x=0;
        c_o=0;
        c_t=0;
        //Left_Diagonal
        if(d==0)
        {
            for(i=0;i<4;i++)
            {
                if(arr[i][3-i]=='X')
                    c_x++;
                if(arr[i][3-i]=='O')
                    c_o++;
                if(arr[i][3-i]=='T')
                   c_t++;
            }
            if(((c_o==3)&(c_t==1))|(c_o==4))
            {
                d=1;
                cout<<"Case #"<<x<<": O won\n";
                //cout<<endl;
                x++;
            }
            else if(((c_x==3)&(c_t==1))|(c_x==4))
            {
                d=1;
                cout<<"Case #"<<x<<": X won\n";
                //cout<<endl;
                x++;
            }
        }
        c_x=0;
        c_o=0;
        c_t=0;
        //Horizontal
        if(d==0)
        {
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(arr[i][j]=='X')
                        c_x++;
                    if(arr[i][j]=='O')
                        c_o++;
                    if(arr[i][j]=='T')
                       c_t++;
                }
                if(((c_o==3)&(c_t==1))|(c_o==4))
                {
                    d=1;
                    cout<<"Case #"<<x<<": O won\n";
                    //cout<<endl;
                    x++;
                    break;
                }
                else if(((c_x==3)&(c_t==1))|(c_x==4))
                {
                    d=1;
                    cout<<"Case #"<<x<<": X won\n";
                    //cout<<endl;
                    x++;
                    break;
                }
                c_x=0;
                c_o=0;
                c_t=0;
            }
        }
        c_x=0;
        c_o=0;
        c_t=0;
        //Vertical
        if(d==0)
        {
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(arr[j][i]=='X')
                        c_x++;
                    if(arr[j][i]=='O')
                        c_o++;
                    if(arr[j][i]=='T')
                       c_t++;
                }
                if(((c_o==3)&(c_t==1))|(c_o==4))
                {
                    d=1;
                    cout<<"Case #"<<x<<": O won\n";
                    //cout<<endl;
                    x++;
                    break;
                }
                else if(((c_x==3)&(c_t==1))|(c_x==4))
                {
                    d=1;
                    cout<<"Case #"<<x<<": X won\n";
                    //cout<<endl;
                    x++;
                    break;
                }
                c_x=0;
                c_o=0;
                c_t=0;
            }
        }
        //Dot
        if(d==0)
        {
            for(i=0;i<4 && d==0;i++)
                for(j=0;j<4;j++)
                    if(arr[i][j]=='.')
                    {
                        cout<<"Case #"<<x<<": Game has not completed\n";
                        //cout<<endl;
                        x++;
                        d=1;
                        break;
                    }
        }
        if(d==0)
        {
            cout<<"Case #"<<x<<": Draw\n";
            x++;
        }
    }
    //getch();
    return 0;
}
