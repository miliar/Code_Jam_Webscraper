#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<cmath>

using namespace std;

bool is_sq(string a)
{
    int i=0;
    while(a[i]!='.')
        i++;
    i++;
    for(;i<a.length();i++)
        if(a[i] != '0')
            return false;
    return true;
}

bool is_pal(string s,int l)
{
    while(s[0] == '0')
    {
        s.erase(s.begin());
        l--;
    }
    for(int j = 0,k = l-1;;j++,k--)
    {
        if(s[j] == s[k]);
        else return false;
        if(k == j || k == j+1)
            break;
    }
    return true;
}

int func(int b,int e)
{
    int ret = 0;
    cout<<"b:"<<b<<"e:"<<e<<endl;
    for(int i=b;i<=e;i++)
    {
        cout<<"i:"<<i<<endl;
        stringstream ss;
        ss << i;
        string ali = ss.str();
        if(is_pal(ali,ali.length()))
        {
            double sq = sqrt(i);
            stringstream s2;
            s2 << sq;
            string alih = s2.str();
            if(is_sq(alih))
            {
                int a;
                for(a=0;alih[a] != '.';a++);
                for(;alih.length()>a;)
                    alih.erase(alih.begin()+a);
                if(is_pal(alih,alih.length()))
                    ret++;
                else continue;
            }
            else continue;
        }
    }
    return ret;
}

int main()
{
    char file[8] = "ali.txt";
    char file2[8] = "out.txt";
    ifstream in(file);
    ofstream out(file2,ios::out);
    int test,i,j,k,begin_n,end_n;
    in>>test;
    for(k=0;k<test;k++)
    {
        in>>begin_n;
        in>>end_n;
        out<<"Case #"<<k+1<<": "<<func(begin_n,end_n)<<"\n";
    }
    return 0;
}
