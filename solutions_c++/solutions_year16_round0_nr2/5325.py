#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin>>T;
    for(int t_c=1;t_c<=T;t_c++){
        string s;
        cin>>s;
        int len=s.size();
        int i=0;
        long long int num=0;
        while(1){
            bool flag=1;
            for(int i=0;i<len;i++) if(s[i]=='-') flag=0;
            if(flag==1) break;
            char ch=s[0];
            int i=0;
            while(s[i]==ch && i<len) i++;
            for(int j=0;j<i;j++){
                if(s[j]=='+') s[j]='-';
                else s[j]='+';
            }
            num++;
        }
        cout<<"Case #"<<t_c<<": "<<num<<"\n";
    }
    return 0;
}
