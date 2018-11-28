#include<fstream>
#include<iostream>
#include<vector>
using namespace std;
ifstream in("in.in");
ofstream out("output.txt");
vector<int> v;
vector<int> v1;
vector<int> s;
int main()
{
    int T;
    in>>T;
    for(int z=0;z<T;z++)
    {
        int riga;
        in>>riga;
        for(int i=1;i<5;i++)for(int j=1;j<5;j++){int a; in>>a; if(i==riga)v.push_back(a);}
        in>>riga;
        for(int i=1;i<5;i++)for(int j=1;j<5;j++){int a; in>>a; if(i==riga)v1.push_back(a);}
        for(int i=0;i<v.size();i++)for(int j=0;j<v1.size();j++)if(v[i]==v1[j])s.push_back(v[i]);
        out<<"Case #"<<z+1<<": ";
        if(s.size()==0)out<<"Volunteer cheated!"<<endl;
        else if(s.size()!=1)out<<"Bad magician!"<<endl;
        else out<<s[0]<<endl;
        v.clear();
        v1.clear();
        s.clear();
    }
    in.close();
    out.close();
}
