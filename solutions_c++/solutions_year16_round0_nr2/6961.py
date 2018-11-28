#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t,l;
    cin>>t;
    for(int k=1;k<=t;k++){
        int ans=0,a[2]={0},count1=1;
        string s;
        cin>>s;
        l=s.length();
        for(int i=0;i<l;i++){
            if(s[i]=='-'){
                a[0]++;
            }
            else{
                a[1]++;
            }
            if(s[i]!=s[i+1] && (i+1)!=l){
                count1++;
            }
        }
        if(a[1]==l) ans=0;
        else if(a[0]==l || (count1==2 && s[l-1]=='+'))    ans=1;
        else if(s[l-1]=='+')    ans=count1-1;
        else    ans=count1;
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
