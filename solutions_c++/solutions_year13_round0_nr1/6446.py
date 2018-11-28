#include<iostream>
using namespace std;
void input(char arr[4][4])
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            cin>>arr[i][j];
}
void test(int t,char arr[4][4])
{
    int i,j,cx,c0,ct,cdot=0;
    for(i=0;i<4;i++)
    {
        cx=0,c0=0,ct=0;
        for(j=0;j<4;j++)
        {
            switch(arr[i][j])
            {
                case 'X':cx++;
                break;
                case 'O':c0++;
                break;
                case 'T':ct++;
                break;
                case '.':cdot++;
                break;
            }
        }
        if(((cx==4)||(c0==4))||(((cx==3)||(c0==3))&&(ct==1)))
        {
            if(cx>=3)
                cout<<"\n"<<"Case #"<<t<<": "<<"X won";
            else if(c0>=3)
                cout<<"\n"<<"Case #"<<t<<": "<<"O won";
            return;
        }
    }
    for(i=0;i<4;i++)
    {
        cx=0,c0=0,ct=0;
        for(j=0;j<4;j++)
        {
            switch(arr[j][i])
            {
                case 'X':cx++;
                break;
                case 'O':c0++;
                break;
                case 'T':ct++;
                break;
                case '.':cdot++;
                break;
            }
        }
        if(((cx==4)||(c0==4))||(((cx==3)||(c0==3))&&(ct==1)))
        {
            if(cx>=3)
                cout<<"\n"<<"Case #"<<t<<": "<<"X won";
            else
                cout<<"\n"<<"Case #"<<t<<": "<<"O won";
            return;
        }
    }
    cx=0,c0=0,ct=0;
    for(i=0;i<4;i++)
    {
        switch(arr[i][i])
        {
            case 'X':cx++;
            break;
            case 'O':c0++;
            break;
            case 'T':ct++;
            break;
            case '.':cdot++;
            break;
        }
    }
    if(((cx==4)||(c0==4))||(((cx==3)||(c0==3))&&(ct==1)))
    {
        if(cx>=3)
            cout<<"\n"<<"Case #"<<t<<": "<<"X won";
        else
            cout<<"\n"<<"Case #"<<t<<": "<<"O won";
        return;
    }
    cx=0,c0=0,ct=0;
    for(i=0;i<4;i++)
    {
        switch(arr[i][3-i])
        {
            case 'X':cx++;
            break;
            case 'O':c0++;
            break;
            case 'T':ct++;
            break;
            case '.':cdot++;
            break;
        }
    }
    if(((cx==4)||(c0==4))||(((cx==3)||(c0==3))&&(ct==1)))
    {
        if(cx>=3)
            cout<<"\n"<<"Case #"<<t<<": "<<"X won";
        else
            cout<<"\n"<<"Case #"<<t<<": "<<"O won";
    }
    else if(cdot)
    {
        cout<<"\n"<<"Case #"<<t<<": "<<"Game has not completed";
    }
    else
    {
        cout<<"\n"<<"Case #"<<t<<": "<<"Draw";
    }
}
int main()
{
    char arr[4][4];
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        input(arr);
        test(i,arr);
    }
    return 0;
}
