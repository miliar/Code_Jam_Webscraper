#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
using namespace std;
ll x,n,ans,c=1,l,r,d,cnt,t;
string s;
int main(){
	freopen("B-large.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    cin>>t;
    while(t--)
    {
        cin>>s;
        cout<<"Case #"<<c++<<": ";
        bool P=0,N=0;
        cnt=0;
        for(int i=0 ; i<s.size() ; i++)
        {
            if(s[i]=='+')
            {
                P=1;
                N=0;
            }
            else
            {
                r=i+1;
                if(P)   cnt+=2;
                else    cnt++;
                for(int j=i+1 ; j<s.size() ; j++)
                {
                    r=j;
                    if(s[j]=='+')   {P=1;break;}
                }
                i=r;
            }
        }
        cout<<cnt<<endl;
    }

}
