#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    fstream icin("input.in",ios::in);
    fstream icout("output.out",ios::out);

    int tst;
    //cout<<"Enter tst\n";
    icin>>tst;
    int j=1;
    while(tst--)
    {
        //cout<<"Enter s\n";
        int s;
        icin>>s;
        string str;
        //cout<<"Enter str\n";
        icin>>str;
        str.resize(s+1);
        //cout<<str<< " - "<<str.size()<<endl;
        unsigned int i,sum,t=0;
        sum=str[0]-'0';
        for(i=1;i<str.size();i++)
        {
            //cout<<"loop "<<i<<endl;
            if(str[i]!='0' && i>sum)
                {t+=i-sum;
                sum+=t+(str[i]-'0');}
            else{
                sum+=(str[i]-'0');
                }
        }

        icout<<"Case #"<<j<<": "<<t<<endl;
        j++;
    }
    //icout << "Hello world!" << endl;
    return 0;
}
