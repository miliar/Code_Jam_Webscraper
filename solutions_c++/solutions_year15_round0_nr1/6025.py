#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream f1("1.txt");
    ofstream f2("2.txt");
    int t;
    f1>>t;
    for(int y=1;y<=t;y++)
    {
        int n;
        string s;
        f1>>n>>s;
        int ans=0,c=0;
        if(s[0]=='0')
        {
            ans+=1;
            c+=1;
        }
        c+=(int)(s[0])-48;
        //cout<<c<<" ";
        for(int i=1;i<s.size();i++)
        {
            //cout<<c<<" ";
            if(i>c && s[i]!='0')
            {
                ans+=i-c;
                c+=i-c;
            }
            c+=(int)(s[i])-48;
        }
        f2<<"Case #"<<y<<": "<<ans<<"\n";
    }
    return 0;
}
