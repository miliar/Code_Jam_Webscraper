#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
using namespace std;
ifstream fin("in.in");
ofstream fout("out.out");
#define cin fin
#define cout fout
int input()
{
    int m;
    int ans=0;
    int c=0;
    cin>>m;
    string temp;
    cin>>temp;
    stringstream ss(temp);
    for(int i=0;i<=m;i++)
    {
        char a;
        ss>>a;
        if(c<i&&a!='0')
        {
            ans+=i-c;
            c=i;
        }
        c+=a-'0';
    }
    return ans;
}
int main()
{
    int t;
    cin>>t;
    for(int v=1;v<=t;v++)
        cout<<"Case #"<<v<<": "<<input()<<endl;
    return 0;
}
