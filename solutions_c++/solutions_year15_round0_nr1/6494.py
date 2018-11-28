#include <iostream>
#include <string>

using namespace std;

int main()
{

    int t;
    cin>>t;
    int d[t];
    string str[t];
    for(int i=0;i<t;i++)
    {
        cin>>d[i]>>str[i];
    }

    int n[t];
    int member;
    int temp;
    for(int i=0;i<t;i++)
    {
        n[i]=0;
        member=0;
        if(d[i]==0)
            n[i]=0;
        else
        {
           for(int j=0;j<str[i].length();j++)
        {
            switch(str[i].at(j))
            {
        case '0':
            {
                temp=0;
                if(member<j+1)
                   temp=(j+1)-member;
                n[i]=n[i]+temp;
                member=member+temp;
                break;
            }
        case '1':
            member+=1;
            break;
        case '2':
            member+=2;
            break;
        case '3':
            member+=3;
            break;
        case '4':
            member+=4;
            break;
        case '5':
            member+=5;
            break;
        case '6':
            member+=6;
            break;
        case '7':
            member+=7;
            break;
        case '8':
            member+=8;
            break;
        case '9':
            member+=9;
            break;

            }
        }
        }



    }



    for(int i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": "<<n[i]<<endl;
    }

    return 0;
}
