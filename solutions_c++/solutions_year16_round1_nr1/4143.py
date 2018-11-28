#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t=0,i=0,start=0,last=0,count=0;
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt",ios::out);
    fin>>t;
    while(t>0)
    {
        count++;
        start=999;
        last=999;
        char str[1000],ans[2001];
        fin>>str;
        ans[start]=str[0];
        for(i=1;str[i]!='\0';i++)
        {      
               if(str[i]>=ans[start])
               {
                                 start--;
                                 ans[start]=str[i];
               }
               else
               {
                   last++;
                   ans[last]=str[i];
               }
        }
        fout<<"Case #"<<count<<": ";
        for(i=start;i<=last;i++)
        {
                                fout<<ans[i];
        }
        fout<<endl;
        t--;
    }
}
