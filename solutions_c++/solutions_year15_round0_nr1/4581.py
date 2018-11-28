#include <iostream>

using namespace std;

int main()
{
    int z;
    cin>>z;
    for(int t=1; t<=z; t++)
    {
        string s;
        int x;
        cin>>x;
        cin>>s;
        int ilemam=s[0]-'0';
        int wynikcaly=0;
        int wynik;
        for(int i=1; i<s.length(); i++)
        {
            if((s[i]-'0')!=0)
            {
                if(ilemam<i)
                {
                    wynik=i-ilemam;
                    wynikcaly+=wynik;
                    ilemam+=wynik;

                }

                ilemam+=s[i]-'0';
            }
        }

        cout<<"Case #"<<t<<": "<<wynikcaly<<endl;

    }

    return 0;
}
