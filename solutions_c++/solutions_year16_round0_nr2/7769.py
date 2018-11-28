#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int main()
{
  //  string s;
    int t;
    int n,i;
    ifstream fp("read.txt");
    ofstream out("write.txt");
 //   cin>>t;
    fp>>t;
    int l=1;
    while(t--)
    {
        //cin>>s;
        string s;
        fp>>s;
        int length=s.length();
        if(length==1)
        {
            if(s[0]=='+')
                //cout<<"0"<<"\n";
                out<<"Case #"<<l++<<":"<<" ""0"<<"\n";
            else
                //cout<<"1"<<"\n";
                out<<"Case #"<<l++<<":"<<" ""1"<<"\n";
        }
        else
        {
            int count=0;
            for(i=1;i<s.length();i++)
            {
                if(s[i]!=s[i-1])
                    count++;
            }
            if(s[i-1]=='-')
                count++;
//        cout<<count<<"\n";
        out<<"Case #"<<l++<<":"<<" "<<count<<"\n";
        }
    }
    return 0;
}
