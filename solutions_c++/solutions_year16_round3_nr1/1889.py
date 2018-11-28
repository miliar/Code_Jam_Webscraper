/// ///////////////////// ///
///                       ///
///      Tamanna_24       ///
///                       ///
///         JU            ///
///                       ///
/// ///////////////////// ///

#include<iostream>
#include<sstream>
#include<cstring>
#include<cstdio>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cstdlib>
#include<cctype>

typedef long long ll;
typedef unsigned long long ull;

#define pi 2.0*acos(0.0)

template <class T> T _diff(T a,T b) {return (a<b?b-a:a-b);}
template <class T> T _abs(T a) {return(a<0?-a:a);}
template <class T> T _max(T a, T b) {return (a>b?a:b);}
template <class T> T _min(T a, T b) {return (a<b?a:b);}
template <class T> T max3(T a, T b, T c) {return (_max(a,b)>c ? _max(a,b) : c);}
template <class T> T min3(T a, T b, T c) {return (_min(a,b)<c ? _min(a,b) : c);}
template< class T>T GCD(T a,T b) {
    a=_abs(a);b=_abs(b);T tmp;while(a%b){ tmp=a%b; a=b; b=tmp; } return b;
}
template< class T>T LCM(T a,T b) {
    a=_abs(a);b=_abs(b);return (a/GCD(a,b))*b;
}
template<class T> T toRad(T deg) { return (deg*pi)/(180.0) ;}
template<class T> T toDeg(T rad) { return (rad*180.0)/(pi) ;}

#define pb(a) push_back(a)
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define S(a) scanf("%d",&a)
#define P(a) printf("%d",a)
#define PN() puts("")
#define PCASE() printf("Case #%d:",kk++)
#define eps 1e-9
#define inf 2000000000
#define mod 1000000007
#define MX  1000000
using namespace std;

struct data{
    int cnt,pos;

    bool operator <(const data &b)const{
        return b.cnt>cnt;
    }
};

priority_queue<data>Q;

int t,kk=1,i,j,k,n;

void giveOut(data x, data y){
    string s="AA";
    s[0]+=x.pos;
    s[1]+=y.pos;
    cout<<" "<<s;
}

void  giveOut(data x, int y){
    string s="";
    s+=('A'+x.pos);
    if(y==2){
        s+=('A'+x.pos);
    }
    cout<<" "<<s;
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.txt","w",stdout);
    data a,b;
    cin>>t;
    while(t--){
        cin>>n;
        while(!Q.empty()) Q.pop();
        for(i=0;i<n;i++){
            cin>>a.cnt;
            a.pos=i;
            Q.push(a);
        }
        bool f=0;
        PCASE();
        while(!Q.empty()){
            a=Q.top();
            Q.pop();
            b=Q.top();
            Q.pop();
            if(a.cnt==0) break;

            if(a.cnt==1 && f==0 && n%2){
                giveOut(a,1);
                a.cnt--;
                f=1;
                Q.push(a);
                Q.push(b);
            }
            else if(a.cnt==b.cnt+1){
                giveOut(a,1);
                a.cnt--;
                Q.push(a);
                Q.push(b);
            }
            else if(a.cnt==b.cnt){
                giveOut(a,b);
                a.cnt--;
                b.cnt--;
                Q.push(a);
                Q.push(b);
            }
            else{
                giveOut(a,2);
                a.cnt-=2;
                Q.push(a);
                Q.push(b);
            }
        }
        cout<<endl;

    }

return 0;
}





