#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define mod 1000000007
int dx[]={1,-1};
int main()
{
    freopen("in2.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int t;
    cin>>t;
    for(int tt=0;tt<t;tt++){
        cout<<"Case #"<<tt+1<<": ";
        string s;
        cin>>s;
        int l=0,r=s.size()-1;
        int cnt=0;
        bool ch=false;
        while(true)
        {
            if(ch)
            {
                    while(l<=r&&s[l]=='+')
                        l++;
                    if(l>r)
                        break;
                    if(s[r]=='+')
                    {
                        int tm=r;
                        while(tm>l&&s[tm]=='+')
                            s[tm--]='-';
                        cnt++;
                    }
                    else
                    {
                        ch=!ch;
                        int tm=r;
                        while(tm>=l){
                            s[tm]=s[tm]=='+'?'-':'+';
                            tm--;
                        }
                        cnt++;
                    }
            }
            else
            {
                    while(r>=l&&s[r]=='+')
                        r--;
                    if(r<l)
                        break;
                    if(s[l]=='+')
                    {
                        int tm=l;
                        while(tm<r&&s[tm]=='+')
                            s[tm++]='-';
                        cnt++;
                    }
                    else
                    {
                        ch=!ch;
                        int tm=l;
                        while(tm<=r){
                            s[tm]=s[tm]=='+'?'-':'+';
                            tm++;
                        }
                        cnt++;
                    }
            }
        }
        cout<<cnt<<endl;
    }
}
