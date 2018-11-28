#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output_l.txt","w",stdout);
    int T,smax,needed,temp;
    char aud[1001];
    cin>>T;
    for(int t=0;t<T;t++)
    {
        temp=0;
        needed=0;
        cin>>smax;
        for(int i=0;i<smax+1;i++)
        {
            cin>>aud[i];
            if(i>temp && aud[i]!='0')
            {
                needed+=i-temp;
                temp+=i-temp;
            }
            temp+=int(aud[i])-'0';
        }
        cout<<"Case #"<<t+1<<": "<<needed<<endl;

    }
}
