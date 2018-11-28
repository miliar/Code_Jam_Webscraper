#include <iostream>
using namespace std;
int main() {
    
  string s;
    int i,t,j;
    int str,count;
    cin>>t;
    for(i=0;i<t;i++)
        {
         cin>>s;
        count=0;
        if(s[0]=='+')
            str=1;
          if(s[0]=='-')
            str=-1;
        for(j=1;j<s.size();j++)
            {
            if(str==1 && s[j]=='-')
            {
                count++;
                str=-1;
            }
            else if(str==-1 && s[j]=='+')
            {
                count++;
                str=1;
            }
        }
        if(str==-1)count++;
        cout<<"Case #"<<(i+1)<<": "<<count<<endl;
    }
    return 0;
}
