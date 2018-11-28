#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    long long int x;
    int T;
    fstream f,f2;
    f.open("A-large.in",ios::in);
    f2.open("result.txt",ios::out);
    f>>T;
    for(int i=1; i<=T;i++)
    {
        int done=45,multiplier=1;
        f>>x;
        if(x==0)
            {f2<<"Case #"<<i<<": INSOMNIA"<<endl; continue;}
        bool check[10];
        for(int j=0;j<10;j++)
            check[j]=false;
        while(true)
        {
            auto temp=x*multiplier,temp2=temp;
            while(temp!=0)
            {
                if(check[temp%10]==false)
                {
                    check[temp%10]=true;
                    done-=temp%10;
                }
                temp/=10;
            }
            if(done==0 && check[0])
            {
                f2<<"Case #"<<i<<": "<<temp2<<endl;
                break;
            }
            ++multiplier;
        }
    }
    f.close();
    f2.close();
    return 0;
}
