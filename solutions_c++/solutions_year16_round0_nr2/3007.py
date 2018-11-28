#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    int t,n,i,j,k,flips,c=1;
    char top;
    string s;
    //ofstream out;
    //out.open("revout1.out");
    cin>>t;
    while(t--)
    {
        cin>>s;
        top=s[0];
        flips=0;
        for(i=0;i<s.length();i++)
        {
            while(i<s.length()&&s[i]==top)
            {
                i++;
            }
            if(i<s.length()&&s[i]!=top)
            {
                flips++;
                top=s[i];
            }
        }
        if(top=='-') flips++;
        cout<<"Case #"<<c<<": "<<flips<<endl;
        c++;
    }
    return 0;
}
