#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in;
    ofstream out;
    long int n,t,i,standing,extra;
    in.open("inp.txt",ios::in);
    out.open("out.txt",ios::out);
   if(!in.eof())
    {
        in>>t;
        for(int l=1;l<t+1;l++)
        {
        in>>n;
        string a;
        in>>a;

        standing=0;
        extra=0;
        for(i=0;i<=n;i++)
        {
            if(standing>=i)
            {
                //cout<<"yes\n";
                standing+=a[i]-48;
                //cout<<standing<<" st\n";
            }
            else if(a[i]!='0')
            {
               // cout<<a[i]<<" hi\n";
                extra+=(i-standing);
                standing+=(i-standing)+a[i]-48;
                //cout<<extra<<"\n";
            }
        }
        cout<<"case #"<<l<<": "<<extra<<"\n";
        out<<"case #"<<l<<": "<<extra<<"\n";
        }
    }

    return 0;
}
