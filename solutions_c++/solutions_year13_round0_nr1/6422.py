#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("C:/Users/Doris/code practise/google-jam-1/a.in", "r", stdin);
    freopen("C:/Users/Doris/code practise/google-jam-1/a.out", "w", stdout);

    int t, n, flag=0, j=0;
    char* a=new char[17];
    a[17]='\0';

    cin>>t;
    n=t;
    while(t)
    {
        for(int i=0; i<16; i++)
            cin>>a[i];

        if((a[0]=='X'||a[0]=='T')&&(a[5]=='X'||a[5]=='T')&&(a[10]=='X'||a[10]=='T')&&(a[15]=='X'||a[15]=='T'))
            flag=1;//x won xie1
        else if((a[0]=='O'||a[0]=='T')&&(a[5]=='O'||a[5]=='T')&&(a[10]=='O'||a[10]=='T')&&(a[15]=='O'||a[15]=='T'))
            flag=2;//o won xie1
        else if((a[3]=='O'||a[3]=='T')&&(a[6]=='O'||a[6]=='T')&&(a[9]=='O'||a[9]=='T')&&(a[12]=='O'||a[12]=='T'))
            flag=2;//o won xie2
        else if((a[3]=='X'||a[3]=='T')&&(a[6]=='X'||a[6]=='T')&&(a[9]=='X'||a[9]=='T')&&(a[12]=='X'||a[12]=='T'))
            flag=1;//x won xie2
        if(!flag)
        {
            for(int i=0; i<4; i++)
            {
                if((a[4*i]=='X'||a[4*i]=='T')&&(a[4*i+1]=='X'||a[4*i+1]=='T')&&(a[4*i+2]=='X'||a[4*i+2]=='T')&& (a[4*i+3]=='X'||a[4*i+3]=='T'))
                    flag=1;//X won heng
                else if((a[4*i]=='O'||a[4*i]=='T')&&(a[4*i+1]=='O'||a[4*i+1]=='T')&&(a[4*i+2]=='O'||a[4*i+2]=='T')&& (a[4*i+3]=='O'||a[4*i+3]=='T'))
                    flag=2;//O won heng
                else if((a[i]=='X'||a[i]=='T')&&(a[i+4]=='X'||a[i+4]=='T')&&(a[i+8]=='X'||a[i+8]=='T')&& (a[i+4*3]=='X' || a[i+4*3]=='T'))
                    flag=1;//X won shu
                else if((a[i]=='O'||a[i]=='T')&&(a[i+4]=='O'||a[i+4]=='T')&&(a[i+8]=='O'||a[i+8]=='T')&& (a[i+4*3]=='O' || a[i+4*3]=='T'))
                    flag=2;//£Ï won shu

            }
            if(!flag)
            {
                for(j=0; j<16; j++)
                    if(a[j]=='.')
                        flag=4;//not complete
                if((flag!=4)&&(j==16))
                    flag=3;// draw
            }
        }
        t--;
        switch(flag)
        {
        case 1:
            cout<<"Case #"<<n-t<<": "<<"X won"<<endl;
            break;
        case 2:
            cout<<"Case #"<<n-t<<": "<<"O won"<<endl;
            break;
        case 3:
            cout<<"Case #"<<n-t<<": "<<"Draw"<<endl;
            break;
        case 4:
            cout<<"Case #"<<n-t<<": "<<"Game has not completed"<<endl;
            break;
        default:
            break;
        }
        flag=0;

    }

    return 0;
}
