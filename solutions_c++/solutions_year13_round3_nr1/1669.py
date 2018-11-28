#include <iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<vector>
#include<string>
#include<map>
#include<string>
#include<math.h>
using namespace std;

string s;
int cnt=0,i,j;
void evalute(string t)
{int ans=0,a;
char ch='.';
    for(i=0;i<t.size();i++)
    {
        if(t[i]>='0'&&t[i]<='9')
        a=a+(t[i]-'0');
        else if(ch=='+') ans=ans+a;
        else if(ch=='-' ) ans=ans-a;
        else ans=a;
    }
    if(ans%3==0||ans%5==0||ans%7==0||ans%9==0) cnt++;
}
void func(int pos, string st)
{if(pos==st.size()-1) {
evaluate(st);
}
    string str;
    str= st.substr (0,pos);
    str=str+"+";
    str=str+st.substring(pos+1,st.size());
    func(pos+1,str);
}
int main()
{
freopen("A.in","r", stdin);
freopen("output.in","w", stdout);
   int   test,tt;
   cin>>test;
   for(tt=1;tt<=test;tt++) {
     cout<<"Case #"<<tt<<':'<<' ';

     cin>>s;
     func();
   }
}


