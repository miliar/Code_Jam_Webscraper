#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;

int T,in[200];
int chk[10],ch;
ifstream ifs;
ofstream ofs;
void input()
{
    ifs>>T;
    for(int i=0;i<T;i++)
        ifs>>in[i];
}
void init()
{
    ch=0;
    for(int i=0;i<10;i++)
        chk[i]=0;
}
void digits(int n)
{
    int m;
    while(n>0)
    {
        m=n%10;
        n=n/10;
        //cout<<"m: "<<m;
        if(chk[m]==0)
        {
            chk[m]=1;
            ch++;
        }
        //cout<<"   ch: "<<ch<<endl;
    }
}
void calc(int tc,int num)
{
    init();
    int i=1;
    while(ch<10&&i<=1000)
    {
        digits(i*num);
        i++;
    }
    if(ch==10)
    {
        ofs<<"Case #"<<tc<<": "<<((i-1)*num)<<endl;
    }
    else
    {
        ofs<<"Case #"<<tc<<": INSOMNIA\n";
    }
}
void exec()
{
    for(int i=0;i<T;i++)
    {
        calc(i+1,in[i]);

    }
}
int main()
{
    ifs.open("A-large.in",ios::in);
    ofs.open("A-large.out",ios::out);
    input();
    //cout<<"----End of Input----\n";
    exec();
}
