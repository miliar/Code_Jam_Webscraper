#include<iostream>
#include<cstring>
#include<list>
#include<cstdio>
using namespace std;
int main()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    char line[1200];
    list<char>nline;
    list<char>::iterator it;
    int i,j,test,length;
    char temp;
    cin>>test;
    for(i=0; i<test; i++)
    {
        cin>>line;
        length=strlen(line);
        nline.push_back(line[0]);
        temp=line[0];
        for(j=1; j<length; j++)
        {
            if(line[j]>=temp)
            {
                nline.push_front(line[j]);
                temp=line[j];
            }
            else
            {
                nline.push_back(line[j]);
            }

        }
        cout<<"Case #"<<i+1<<": ";
        for(it=nline.begin();it!=nline.end();it++)
        {
            cout<<*it;
        }
        cout<<endl;
        nline.clear();
    }
    return 0;
}
