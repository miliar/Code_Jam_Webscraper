#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
int main()
{
    freopen("bin.txt","r",stdin);
    freopen("bout.txt","w",stdout);
    int test,group,i,j,length;
    string line;
    char prev;
    cin>>test;
    for(i=0; i<test; i++)
    {
        cin>>line;
        length=line.length();
        prev=line[0];
        group=1;
        for(j=1; j<length; j++)
        {
            if(line[j]!=prev)
            {
                group++;
                prev=line[j];
            }
        }
        if(line[length-1]=='+')
        {
            group--;
        }
        cout<<"Case #"<<i+1<<": "<<group<<endl;
    }
    fclose(stdout);
    return 0;
}
