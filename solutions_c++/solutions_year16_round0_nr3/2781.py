#include<bits/stdc++.h>
using namespace std;
int t,t0,j,n,flag;
long long int d;
vector<string> op;
vector<vector<int> > divs;
vector<int> tempdivs;
string str;

int div(long long int n)
{
    for(int i=2;i<=sqrt(n);i++)
    {
        if(n%i==0)
            return i;
    }
    return -1;
}

long long int convertBase(string str, int b)
{
    long long int sum = 0;
    for(int i=0;i<str.length();i++)
    {
        sum=(sum*b)+str[i]-'0';
    }
    return sum;
}

void check(string str)
{
    flag=0;
    tempdivs.clear();
    for(int i=2;i<=10;i++)
    {
        if(flag==1) continue;
        d = div(convertBase(str,i));
        tempdivs.push_back(d);
        if(d==-1) flag=1;
    }
    if(!flag)
    {
        op.push_back(str);
        divs.push_back(tempdivs);
    }
}

void generateJam(int n, int j,int pos)
{
    if(pos==n-1){
        check(str); 
        return;
    }
    if(op.size()==j) return;
    generateJam(n,j,pos+1);
    str[pos]='1';
    generateJam(n,j,pos+1);
    str[pos]='0';
}

int main()
{
    cin>>t;
    t0=1;
    while(t--)
    {
        op.clear();
        cin>>n>>j;
        str="";
        for(int i=1;i<n-1;i++)
            str=str+'0';
        str='1'+str+'1';
        generateJam(n,j,1);
        cout<<"Case #"<<t0++<<": "<<endl;
        for(int i=0;i<op.size();i++)
        {
            cout<<op[i]<<" ";
            for(int j=0;j<divs[i].size();j++)
                cout<<divs[i][j]<< " ";
            cout<<endl;
        }
    }
}