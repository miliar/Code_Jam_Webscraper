#include <iostream>
#include <string.h>
#include <stdio.h>
#include <fstream>
using namespace std;

int main()
{
    int t,i,j,n,num1,num2;
    char ch[16],flag;
    ifstream cin("A-small-attempt5.in");
    ofstream cout("A.out");
    while(cin>>t)
    {

        n = 0;
        while(t--)
        {
            memset(ch,0,sizeof(ch));
            for(i=0;i<16;i++)
                cin >> ch[i];
            num1 = 0;
            flag = 'a';

            for(i<0;i<16;i++)
            {
                if(ch[i] == 'T')
                {
                    for(j=i/4*4;j+1<(i/4+1)*4;j++)
                    {
                        if(i!=j)
                        {
                            flag = ch[j];
                            if(i!=j&&ch[j] != ch[j+1])
                            {
                                flag = 'a';
                                break;
                            }
                        }
                    }
                }

                if(flag != 'a')
                    break;

                if(ch[i] == 'T')
                {
                    for(j=i%4;j+1<=(i%4)+12;j+=4)
                    {
                        if(i!=j)
                        {
                            flag = ch[j];
                            if(i!=j&&ch[j] != ch[j+1])
                            {
                                flag = 'a';
                                break;
                            }
                        }
                    }
                }

                if(flag != 'a')
                    break;
            }

            if(flag == 'a')
                for(i=0;i<16;i++)
                {
                    if(ch[i] == '.')
                        flag = '.';

                    if(i%4 == 0)
                    {
                        for(j=i+1;j<i+4;j++)
                            if(ch[i] == ch[j] || ch[j] == 'T')
                                num1++;

                        if(num1 == 3)
                        {
                            flag = ch[i];
                            break;
                        }
                        num1 = 0;
                    }
                    if(i < 4)
                    {
                        for(j=i+4;j<=i+12;j += 4)
                            if(ch[i] == ch[j] || ch[j] == 'T')
                                num1++;

                        if(num1 == 3)
                        {
                            flag = ch[i];
                            break;
                        }
                        num1 = 0;
                    }
                    if(i == 0)
                    {
                        for(j=5;j<16;j+=5)
                            if(ch[i] == ch[j] || ch[j] == 'T')
                                num1++;

                        if(num1 == 3)
                        {
                            flag = ch[i];
                            break;
                        }
                        num1 = 0;
                    }
                    if(i == 3)
                    {
                        for(j=6;j<13;j+=3)
                            if(ch[i] == ch[j] || ch[j] == 'T')
                                num1++;

                        if(num1 == 3)
                        {
                            flag = ch[i];
                            break;
                        }
                        num1 = 0;
                    }
                }
            n++;
            switch(flag)
            {
                case 'X': cout<<"Case #"<<n<<": X won"<<endl;break;
                case 'O': cout<<"Case #"<<n<<": O won"<<endl;break;
                case '.': cout<<"Case #"<<n<<": Game has not completed"<<endl;break;
                case 'a': cout<<"Case #"<<n<<": Draw"<<endl;break;
            }
        }
    }
}
