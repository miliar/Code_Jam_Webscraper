#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>

#define N 100009
#define ll long long

using namespace std;

vector<string> res;
char digit[30];
char result[120];
void check(string &s)
{
    int n=s.size();
    memset(result,0,sizeof(result));
    reverse(s.begin(),s.end());
    for(int i=0;s[i];i++)
    {
        for(int j=0;s[j];j++)
        {
            result[i+j]+=(s[j]-'0')*(s[i]-'0');
            result[i+j+1]+=result[i+j]/10;
            result[i+j]%=10;
        }
    }
    int len=2*n-1;
    if(result[len]) len++;
    string t;
    for(int i=len-1;i>=0;i--){
        t.append(1,'0'+result[i]);
        if(result[i]!=result[len-1-i]) return;
    }
    res.push_back(t);
}
void go(int d,int r1,int r2)
{
    if(d==27) return;
    if(d){
        digit[d]=0;
        string s=digit;
        for(int i=0;i<d;i++){
            s.append(1,digit[d-1-i]);
        }
        check(s);
        s=digit;
        for(int i=1;i<d;i++){
            s.append(1,digit[d-1-i]);
        }
        check(s);
    }
    if(d){
        digit[d]='0';
        go(d+1,r1,r2);
    }
    if(r1){
        digit[d]='1';
        go(d+1,r1-1,r2);
    }
    if(r2){
        digit[d]='2';
        go(d+1,r1,r2-1);
    }
}
bool cmp(const string &a,const string &b)
{
    if(a.size()!=b.size()) return a.size()<b.size();
    return a<b;
}
int bin(string a)
{
    int l=0,r=res.size()-1,mid,ret;
    while(l<=r)
    {
        mid=(l+r)>>1;
        if(!cmp(res[mid],a)) ret=mid,r=mid-1;
        else l=mid+1;
    }
    return ret;
}
int main()
{
    freopen("c.txt","r",stdin);
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        res.push_back(s);
    }
    fclose(stdin);
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    /*go(0,5,1);
    res.push_back("9");
    sort(res.begin(),res.end(),cmp);
    cout<<res.size()<<endl;
    for(int i=0;i<res.size();i++) cout<<res[i]<<endl;
    */
    int T,cas=0;
    cin>>T;
    while(T--)
    {
        string a,b;
        cin>>a>>b;
        int l=bin(a);
        int r=bin(b);
        if(res[r]==b) r++;
        //cout<<cmp(a,res[0])<<endl;
        //cout<<l<<' '<<r<<endl;
        printf("Case #%d: %d\n",++cas,r-l);
    }

    fclose(stdout);
    return 0;
}
