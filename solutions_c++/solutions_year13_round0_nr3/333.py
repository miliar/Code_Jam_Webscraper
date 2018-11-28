#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>

using namespace std;

#define INF 1<<28
#define SIZE 1000

#define REP(i,n) for (i=0;i<n;i++)
#define REV(i,n) for (i=n;i>=0;i--)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define FOR(i,p,k) for (i=p; i<k;i++)
#define Reverse(x) reverse(x.begin(),x.end())

#define bug(x)    cout<< "->" <<#x<<": "<<x<<endl   //debug(x) variable
#define Sort(x) sort(x.begin(),x.end())
#define MP(a,b) make_pair(a,b)
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define COPY(c,r)   memcpy(c,r,sizeof(r))
#define SZ(x) (int)x.size()
#define PB push_back
#define popcount(i) __builtin_popcount(i)
#define gcd(a,b)    __gcd(a,b)
#define fs first
#define sc second
#define pb push_back

typedef long long ll;

string Multiplication(string a,string b); //Multiplication between a and b
string cut_leading_zero(string a);  //leading zero cut 001 -> 1
bool    comp(string a,string b);  //(1 means a>b) (-1 means a<b) (0 means a=b)
string Addition(string a,string b);
string Subtraction(string a,string b);

template<class T1> void deb(T1 e){cout<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}


vector<string>store;
//vector<string>store2;

string num,now;

int is_pal()
{
    for(int i=0;i<SZ(now)/2;i++)
    {
        if(now[i]!=now[SZ(now)-1-i]) return 0;
    }
    return 1;
}


void rec(int left,int right, int one)
{
    if(one>9) return;

    if(left>right)
    {
        now=Multiplication(num,num);
        {
            store.pb(now);
//            store2.pb(num);
        }
        return ;
    }

    int mx;
    if(left==right && one<6) mx=2;
    else mx=1;

    for(int i=0;i<=mx;i++)
    {
        num[left]=i+'0';
        num[right]=i+'0';

        rec(left+1,right-1,one + ( (left!=right) ? i*2 : i ) );
    }
    return ;
}

void rec2(int left, int right)
{
    if(left>right)
    {
        now=Multiplication(num,num);

        if(is_pal()) {
            store.pb(now);
//            store2.pb(num);
        }
        return ;
    }

    int mx=( (left==right) ? 2: 0 );
    for(int i=0;i<=mx;i++)
    {
        num[left]=i+'0';
        num[right]=i+'0';
        rec2(left+1,right-1);
    }
    return ;
}

void generate()
{
    store.pb("1");
    store.pb("4");
    store.pb("9");

    for(int i=2;i<=50;i++)
    {
        num.clear();
        for(int j=0;j<i;j++) num+='0';

        num[0]='1';
        num[SZ(num)-1]='1';
        rec(1,SZ(num)-2,2);


        num[0]='2';
        num[SZ(num)-1]='2';

        rec2(1,SZ(num)-2);
    }

    sort(store.begin(),store.end(),comp);

//    sort(store2.begin(),store2.end(),comp);
//    for(int i=0;i<SZ(store2);i++) cout<<"found "<<i<<" "<<store2[i]<<endl;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    generate();
    char arr[2000];
    string low,high;

    vector<string>::iterator it;
    int cas,loop=0;
    ll pos1,pos2;
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%s",arr);low=arr;
        low=Subtraction(low,"1");
        scanf("%s",arr);high=arr;

        it=lower_bound(store.begin(),store.end(),low,comp);
        pos1=(it-store.begin());

        it=lower_bound(store.begin(),store.end(),high,comp);
        pos2=(it-store.begin());

//        cout<<"pos1 "<<pos1<< " pos2 "<<pos2<<endl;
        printf("Case #%d: %lld\n",++loop,pos2-pos1);

    }
    return 0;
}

string Multiplication(string a,string b)
{
    long long  i,j,multi,carry;
    string ans,temp;

    ans="0";
    REV(j,SZ(b)-1)
    {
        temp="";
        carry=0;
        REV(i,SZ(a)-1)
        {
            multi=(a[i]-'0')*(b[j]-'0')+carry;
            temp+=(multi%10+'0');
            carry=multi/10;
        }
        if(carry)   temp+=(carry+'0');
        Reverse(temp);
        temp+=string(SZ(b)-j-1,'0');
        ans=Addition(ans,temp);
    }
    ans=cut_leading_zero(ans);
    return ans;
}
string Addition(string a,string b)
{
    long long  carry=0,i;
    string ans;

    if(SZ(a)>SZ(b)) b=string(SZ(a)-SZ(b),'0')+b;
    if(SZ(b)>SZ(a)) a=string(SZ(b)-SZ(a),'0')+a;
    ans.resize(SZ(a));
    REV(i,SZ(a)-1)
    {
        int sum=carry+a[i]+b[i]-96;
        ans[i]=(char)(sum%10+'0');
        carry=sum/10;
    }
    if(carry)   ans.insert(0,string(1,carry+'0'));
    ans=cut_leading_zero(ans);
    return ans;
}

bool comp(string a,string b)
{
    int i;
    a=cut_leading_zero(a);
    b=cut_leading_zero(b);
    if(SZ(a)>SZ(b)) return false;   //bigger
    if(SZ(a)<SZ(b)) return true;  //smaller
    REP(i,SZ(a))
        if(a[i]>b[i])   return false;   //bigger
        else if(a[i]<b[i])  return true; //smaller
}

string cut_leading_zero(string a)
{
    string s;
    int i;
    if(a[0]!='0')   return a;
    REP(i,SZ(a)-1)  if(a[i]!='0')   break;
    FOR(i,i,SZ(a))  s+=a[i];
    return s;
}

string Subtraction(string a,string b)
{
    int borrow=0,i,sub;
    string ans;
    if(SZ(b)<SZ(a)) b=string(SZ(a)-SZ(b),'0')+b;
    REV(i,SZ(a)-1)
    {
        sub=a[i]-b[i]-borrow;
        if(sub<0)
        {
            sub+=10;
            borrow=1;
        }
        else borrow=0;
        ans+=sub+'0';
    }
    Reverse(ans);
    ans=cut_leading_zero(ans);
    return ans;
}


