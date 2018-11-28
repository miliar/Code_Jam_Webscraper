#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("out.txt");
    string s,lw,temp;
    int t,i=0;
    fin>>t;
    for(int tc=0;tc<t;tc++)
    {
        i=0;
        fin>>s;
        cout<<endl<<s;
        lw=s;
        for(int j=1;j<s.length();j++)
            lw[j]='\0';
        cout<<endl<<lw;
        for(i=1;i<s.length();)
        {
            cout<<endl<<lw;
            if(s[i]>=lw[0])
            {
                temp=s[i];
                lw=temp+lw;
        cout<<endl<<temp<<"\t"<<lw;
                i++;
            }
            else
            {
                lw[i]=s[i];
                i++;
            }
        }
        fout<<"Case #"<<tc+1<<": ";
        for(int j=0;j<lw.length();j++)
        {
            if(lw[j]!=' '&&lw[j]!='\0')
                fout<<lw[j];
        }
        fout<<endl;
    }
    return 0;
}
