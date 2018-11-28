#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>
#include<string.h>
#include<vector>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("ans.txt");
    int t,j,len,count,i;
    char a[1011];
    std:: vector<char> v;
    std:: vector<char> :: iterator it;
    //bool arr[11];
    fin>>t;
    //cout<<t;

    for(j=1;j<=t;j++)
    {
        fin>>a;
        len=strlen(a);
        v.push_back(a[0]);
        fout<<"Case #"<<j<<": ";
        for(i=1;i<len;i++)
        {
            it=v.begin();
          //  cout<<*it<<" "<<a[i]<<endl;
            if(*it<=a[i]) v.insert(v.begin(),a[i]);
            else v.push_back(a[i]);

        }

        for(it=v.begin();it!=v.end();it++)
        fout<<*it;
        fout<<endl;
        v.clear();
    }

    return 0;
}
