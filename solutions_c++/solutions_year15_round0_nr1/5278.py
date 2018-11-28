#include <iostream>
#include <cstring>
#include <cstdio>

#define REP(i,a) for(int i=0;i<a;i++)

using namespace std;

int main()
{
    freopen("f1l.in","r",stdin);
    freopen("o1l.txt","w",stdout);
    int T;
    cin>>T;
    REP(t,T){
        int N,tmp;
        cin>>N;
        char s;
        int sum=0,res=0;
        cin>>s;
      //  cout<<"char : "<<s<<endl;
        sum+=s-'0';
        REP(i,N){
            cin>>s;
          //  cout<<"char : "<<s<<endl;
            tmp=max(0,i+1-sum);
            res+=tmp;
            sum+=s-'0'+tmp;
        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
}

