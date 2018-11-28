#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
using namespace std;

string s;

int main()
{
    freopen("gcj_16_qua_2_in.txt","r",stdin);
    freopen("gcj_16_qua_2_out.txt","w",stdout);
    int t;
    cin>>t;
    for(int qq=1;qq<=t;qq++) {
        cout<<"Case #"<<qq<<": ";
        int i,j,n,m,temp,ans=0,p1,p2;
        cin>>s;
        n=s.length();
        for(i=n-1;i>=0;i--) {
            if(s[i]=='-') {
                if(s[0]=='-') ans++;
                else {
                    ans+=2;
                    for(j=0;j<=i;j++) {
                        if(s[j]=='+') s[j]='-';
                        else break;
                    }
                }
                p1=0; p2=i;
                while(p1<p2) swap(s[p1],s[p2]),p1++,p2--;
                for(j=i;j>=0;j--) (s[j]=='+')?(s[j]='-'):(s[j]='+');
            }
        }
        cout<<ans<<"\n";
    }
    return 0;
}
