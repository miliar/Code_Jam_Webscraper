#include<iostream>
using namespace std;
int f(int st, int len) {
    if(len==0) return 0;
    if(len==1) return st;

    if(st==1) {
        if(len%2==0)
            return f(1,len-1);
        else
            return 1 + f(0, len);
    }
    else
    {
        if(len%2==1)
            return f(0, len-1);
        else
            return 1 + f(1, len-1);
    }
}
int main()
{
    int t;
    cin>>t;
    for(int kase=1;kase<=t;kase++) {
        cout<<"Case #"<<kase<<": ";
        string s;
        cin>>s;
        int st = 0;
        int pre = 0;
        if(s[0] == '-') {
          st = 1;
          pre = 1;
        }
        int cnt = 1;
        for(int i=1;i<(int)s.size();i++) {
          int cur = 0;
          if(s[i]=='-')
              cur = 1;
          if(cur==pre) continue;
          pre = cur;
          cnt++;
        }
        cout<<f(st, cnt)<<endl;
    }

}
