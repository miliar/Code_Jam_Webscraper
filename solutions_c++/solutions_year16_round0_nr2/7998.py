#include <bits/stdc++.h>
using namespace std;
long long int func(string s,int pos,int what)
{
    if (what==1){
        if (pos==0){
            if (s[pos]=='+')
                return 0;
            else
                return 1;
        }
        if (s[pos]=='+')
            return func(s,pos-1,1);
        else{
            if (s[0]=='-'){
                int i,j;
                for (i=0,j=pos;i<j;j--,i++){
                    char temp;
                    if (s[i]=='-')
                        temp='+';
                    else
                        temp='-';
                    if (s[j]=='-')
                        s[i]='+';
                    else
                        s[i]='-';
                    s[j]=temp;
                }
                if (i==j)
                    s[i]=(s[i]=='+')?'-':'+';
                return (func(s,pos-1,1)+1);
            }
            else {
                return (func(s,pos-1,0)+1);
            }
        }
    }
    else {
        if (pos==0){
            if (s[pos]=='-')
                return 0;
            else
                return 1;
        }
        if (s[pos]=='-')
            return func(s,pos-1,0);
        else{
            if (s[0]=='+'){
                int i,j;
                for (i=0,j=pos;i<j;j--,i++){
                    char temp;
                    if (s[i]=='-')
                        temp='+';
                    else
                        temp='-';
                    if (s[j]=='-')
                        s[i]='+';
                    else
                        s[i]='-';
                    s[j]=temp;
                }
                if (i==j)
                    s[i]=(s[i]=='+')?'-':'+';
                return (func(s,pos-1,0)+1);
            }
            else {
                return (func(s,pos-1,1)+1);
            }
        }
    }
}
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while (t--){
        string s;
        cin>>s;
        int n=s.size();
        int i,j;
        long long int ans=func(s,n-1,1);  // 1 for + 0 for -
        cout<<"Case #"<<cas++<<": "<<ans<<endl;
    }
    return 0;
}
