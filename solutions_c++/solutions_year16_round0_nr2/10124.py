// Example program
#include <iostream>
#include <string>
#include <set>

using namespace std;
int main()
{
    int t;
    string ss;
    cin>>t;
    for(int i=1;i<=t;++i) {
        cin>>ss;
        int res = 0;
        string s = "";
        for(int j=0;j<ss.size();) {
            char c=ss[j];
            for (int k=j; ss[k] == c; k++,j++);
            s+=c;
        }
        for(int j=s.size()-1;j>=0;--j) {
            bool pos = 0;
            if (s[j]=='-')
            {
                for(int k=j-1;k>=0;k--)
                {
                    if(s[k]=='+'){
                        pos=1;
                        break;
                    }
                }
                if(pos)
                    res+=2;
                else
                    res++;
            }
            
        }
        cout << "Case #"<<i<<": " <<res<<endl;
    }
}

