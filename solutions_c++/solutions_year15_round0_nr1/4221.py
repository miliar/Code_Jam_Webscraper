#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
            int Smax;
            cin>>Smax;
            char *ch = new char[Smax+2];
            cin>>ch;
            int total=0;
            int freind=0;
            for(int j=0;j<=Smax+1;j++)
            {
             if(total>=j)
             {
                         total+=(ch[j]-'0');
             }
             else
             {
                 freind+=(j-total);
                 total+=(j-total);
                 total+=(ch[j]-'0');
             }                     
            }
            cout<<"Case #"<<i<<": "<<freind<<"\n";
    }
}
