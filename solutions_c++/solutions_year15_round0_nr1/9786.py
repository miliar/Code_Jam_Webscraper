#include <iostream>

using namespace std;

int ctoint(char num)
{
    switch (num)
    {
    case '0':return 0;
    case '1':return 1;
    case '2':return 2;
    case '3':return 3;
    case '4':return 4;
    case '5':return 5;
    case '6':return 6;
    case '7':return 7;
    case '8':return 8;
    case '9':return 9;
    default:{
                cout << "error";
                return 0;
            }
    }
}

int getit(string s)
{

    int res=ctoint(s.at(0)),req=0,num;

    for(int i=1;i<s.length();i++)
        {
           num = ctoint(s.at(i));
           if(num!=0)
               {
                if(res>=i)
                    res = res + num;
                else{
                        req  += i-res;
                        res = res + num+req;
                    }
               }
        }


    return req;



}


int main()
{

    int tc;cin>>tc;
    for(int i=1;i<=tc;i++)
        {
            int l;string s;
            cin >> l >> s;
            cout << "Case #"<<i<<": "<<getit(s)<<"\n";
        }

    return 0;
}

