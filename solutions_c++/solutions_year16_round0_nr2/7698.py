#include<bits/stdc++.h>
#include<fstream>
using namespace std;
char ch[101];
void flip(int l)
{
    for(int i=0;i<=l;++i)
    {
        if(ch[i]=='-')
            ch[i]='+';
        else
            ch[i]='-';
    }
}
int main()
{
    int x=1,t,i,count,l;
    ifstream fin;
    fin.open("B-large.in",ios::in);
    ofstream fout;
    fout.open("output2.txt",ios::out);
    fin>>t;
    while(x<=t)
    {
        fin>>ch;
        count=0;
        l=strlen(ch);
        s:
        for(i=l-1;i>=0;--i)
        {
            if(ch[i]=='-')
            {
                flip(i);
                count++;
                goto s;
            }
        }
        fout<<"Case #"<<x<<": "<<count<<endl;
        ++x;
    }
    fin.close();
    fout.close();

}
