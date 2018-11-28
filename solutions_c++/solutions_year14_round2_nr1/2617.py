#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

ifstream in("A-small-attempt0.in");
ofstream out("output.out");

int t,n,l;
string s[100];
int q[100][100];

void input()
{
    in>>n;
    for(int i=0;i<n;i++)in>>s[i];
}

string reduce(int k)
{
    string u=s[k];
    int i=0,y=1;
    while(i<u.size())
    {
        if(u[i]==u[i+1])
        {
            u.erase(i,1);
            y++;
        }
        else
        {
            q[k][i]=y;
            i++;
            y=1;
        }
    }
    //cout<<"u "<<u<<endl;
    return u;
}

bool check()
{
    string c=reduce(0);
    l=c.size();
    for(int i=1;i<n;i++)
    {
        if(c!=reduce(i))return 0;
    }
    return 1;
}

void show()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<l;j++)
        {
            cout<<q[i][j]<<" ";
        }
        cout<<endl;
    }
}

int count()
{
    int sum[l];
    int m=0;
    for(int i=0;i<l;i++)sum[i]=0;
    for(int i=0;i<l;i++)for(int j=0;j<n;j++)sum[i]+=q[j][i];
    for(int i=0;i<l;i++)
    {
        int a;
        if(sum[i]/(float)n>=sum[i]/n+0.5)a=sum[i]/n+1;
        else a=sum[i]/n;
        for(int j=0;j<n;j++)m+=abs(q[j][i]-a);
    }
    return m;
}

int main()
{
    in>>t;
    for(int i=0;i<t;i++)
    {
        input();
        if(check())
        {
            //show();
            out<<"Case #"<<i+1<<": "<<count()<<endl;
        }
        else out<<"Case #"<<i+1<<": Fegla Won"<<endl;

    }
    return 0;
}
