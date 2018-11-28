#include<bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
freopen("Input.txt","r",stdin);
 freopen("Output.txt","w",stdout);
int t;
cin>>t;
string str;
for(int te=0;te<t;te++){
    cin>>str;int ans=0,siz=str.size();
    cout<<"Case #"<<te+1<<": ";
    while(true){
        bool flag=1;
    for(int i=0;i<siz&&flag;i++)
    if(str[i]=='-')
    flag=0;
    if(flag){
        cout<<ans<<endl;
        break;
    }
    ans++;
       char ch=str[0];
        for(int i=0;i<siz;i++)
        {
           if(str[i]==ch) {
            if(ch=='+')
            str[i]='-';
           else
            str[i]='+';
           }
           else
            break;
        }
        }
}
return 0;
}

