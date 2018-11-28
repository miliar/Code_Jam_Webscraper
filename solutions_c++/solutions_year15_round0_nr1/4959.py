#include <iostream>
#include <fstream>
#include <cstring>
#define max_shyness 1000
#define sol "Case #"

using namespace std;

int main()
{
    fstream fin,fout;
    int j,i=0,cur_ans,t,s_max,ans[110],counter;char str[max_shyness+10];
    fin.open("A.in",ios::in);
    fin>>t;
    while(i<t)
    {
    fin>>s_max;
    memset(str,0,sizeof(str));
    fin>>str;
    cur_ans=0;
    counter=str[0]-'0';
    for(j=1;j<=s_max;j++)
    {
        if(j>counter && str[j]>'0')
            {cur_ans+=j-counter;counter=j;}
        counter+=str[j]-'0';
    }
    i++;
    ans[i]=cur_ans;
    }
    fin.close();
    fout.open("solution.out",ios::out);
    for(i=1;i<=t;i++)
        fout<<sol<<i<<": "<<ans[i]<<'\n';
    fout.close();
    return 0;
}
