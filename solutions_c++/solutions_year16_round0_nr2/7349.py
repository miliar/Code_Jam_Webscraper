#include<bits/stdc++.h>
using namespace std;
int check_front(string s,int sp,int ep)
{
    int count=sp;
    while(sp<=ep &&s[sp]=='-')
    {
        sp++;
    }
    return sp-count;;
}
int check_end(string s,int sp,int ep)
{
    int count=ep;
    while(ep>=sp && s[ep]=='-')
    {
        ep--;
    }
    return count-ep;
}
string invert(string s,int sp,int ep)
{
    for(int i=sp;i<=ep;i++)
    {
        if(s[i]=='-')s[i]='+';
        else s[i]='-';
    }
    return s;
}
int solve(string s,int sp,int ep)
{
    int a,b;int count=0;
    while(sp<=ep)
    {
        a=check_front(s,sp,ep);
        b=check_end(s,sp,ep);
        //cout << a << " " << b << endl;
        if(a>=b && a>0)
        {
            sp+=a;count++;
        }
        else if(b>a && b>0)
        {
            ep-=b;count++;s=invert(s,sp,ep);//cout << s << endl;
        }
        if(sp==ep && s[sp]=='+')break;
    }
    return count;
}
int main()
{
   freopen("B-large.in","r",stdin);
   freopen("output_file1.in","w",stdout);
    int t;
    cin >> t;
    string s;
    int sp,ep;
    int x=1;
    while(t--)
    {
        cin >> s;ep=0;
        for(int i=s.length()-1;i>=0;i--)
        {
            if(s[i]=='-'){ep=i;break;}
        }
        sp=0;
        int ans=solve(s,sp,ep);
        cout << "Case #"<< x << ": " <<ans << "\n";
      x++;
    }
}
