#include <iostream>
#include <bits/stdc++.h>
using namespace std;
vector<int> v;
void solve(int l,int h,int a[]){
    if(l>h)
        return;
int m=a[l],index=l;
for(int i=l;i<=h;i++){
    if(a[i]>=m){
        m=a[i];
        index=i;
    }
}
   v.push_back(m);
   solve(l,index-1,a);
   for(int i=index+1;i<=h;i++)
        v.push_back(a[i]);

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);

    int t;
    cin>>t;
    for(int u=0;u<t;u++){
            cout<<"Case #"<<u+1<<": ";
        string s;
        cin>>s;
        int len=s.length();
        int a[len];
        for(int i=0;i<len;i++){
            a[i]=s[i];
        }

        solve(0,len-1,a);
        for(int i=0;i<v.size();i++){
            char c=v[i];
            cout<<c;
        }
        cout<<endl;
        int l=v.size();
        while(l--){
            v.pop_back();
        }

    }
    return 0;
}
