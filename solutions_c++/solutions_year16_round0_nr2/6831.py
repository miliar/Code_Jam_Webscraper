#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,i,c=1,groups,len;
    string str;
    cin>>t;
    while(t--){
        cin>>str;
        groups=0;
        len=str.length();
        for(i=0;i<len;i++){
            if(str[i]=='-'){
                i++;
                while(i<len && str[i]=='-')
                i++;
                i--;
                groups++;
            }
        }
        if(groups==0)
        {
            cout<<"Case #"<<c++<<": 0\n";
        }
        else if(str[0]=='+'){
            cout<<"Case #"<<c++<<": "<<2*groups<<"\n";
        }
        else{
            cout<<"Case #"<<c++<<": "<<2*groups-1<<"\n";
        }
    }
    return 0;
}
