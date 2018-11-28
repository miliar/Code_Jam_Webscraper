#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
using namespace std;
vector<int>v;
ll mn;
string V1,V2;
int Int(string s)
{
	int t=0;
	istringstream (s)>>t;
	return t;
}
void solve(string a,string b)
{
    bool A=0,B=0;
    for(int i=0 ; i<a.size() ; i++)
        if(a[i]=='?')    A=1;
    for(int i=0 ; i<a.size() ; i++)
        if(b[i]=='?')    B=1;
    if(!A&&!B)
    {
        if(abs(Int(a)-Int(b))<mn)
        {
            V1=a,V2=b;
            mn=abs(Int(a)-Int(b));
        }
        return;
    }
    if(A)
    {
        for(int j=0 ; j<a.size() ; j++)
            if(a[j]=='?')
                for(int i='0' ; i<='9' ; i++)
                {
                    a[j]=i;
                    solve(a,b);
                }
    }
    if(B)
    {
        for(int j=0 ; j<a.size() ; j++)
            if(b[j]=='?')
                for(int i='0' ; i<='9' ; i++)
                {
                    b[j]=i;
                    solve(a,b);
                }
    }

}
int main(){
    freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,k=1;
	cin>>t;
	string s1,s2;
	while(t--)
    {
        mn=999999999;
        cin>>s1>>s2;
        solve(s1,s2);
        cout<<"Case #"<<k++<<": ";
        cout<<V1<<" "<<V2<<endl;
        V1=V2="";
    }

}
