#include <iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int m=1;
    while(t>0){
        string s;
        cin>>s;
        int tot=0;
        for(int i=1;i<s.length();++i){
            if(s[i]!=s[i-1]){
                tot++;
            }
        }
        if(s[s.length()-1]=='-'){
            ++tot;
        }
        cout<<"Case #"<<m<<": "<<tot<<endl;
        --t;
    }
    return 0;
}
