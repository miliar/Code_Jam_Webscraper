#include<bits/stdc++.h>
#include <stdio.h>

using namespace std;

#define mod 1000000007LL
#define pi 3.141592653589793238462643383279;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define f first
#define s second
#define pic pair<char,long long >
void scan(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        scanf("%d",&v[i]);
}

void print(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        printf("%d ",v[i]);
}
// a large
void fun()
{
    string s;
    int k;
    cin>>s>>k;
    int ans=0;
    for(int i=0;i<=s.length()-k;i++)
    {
        if(s[i]=='-')
        {
            ans++;
            s[i]='+';
            for(int j=i+1;j<i+k;j++)
            {
                if(s[j]=='+')
                    s[j]='-';
                else
                    s[j]='+';
            }
        }
    }
    for(int i=s.length()-k;i<s.length();i++)
    {
        if(s[i]=='-')
        {
            cout<<"IMPOSSIBLE";
            return;
        }
    }
    cout<<ans;
}
int main()
{

    bool test=1;
    if(test==1)
    {
        freopen("input_file_name.txt","r",stdin);
        freopen("output_file_name.txt","w",stdout);
    }
    int t;
    scanf("%d",&t);
    //cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        fun();
        cout<<endl;
    }
    int acc;cin>>acc;
    return 0;
}
