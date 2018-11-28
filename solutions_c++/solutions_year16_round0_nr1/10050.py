/*Header file starts here*/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cmath>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <string>
#include <cstring>
#include <ctime>

/*Header File ends here*/

/*Macro starts here*/

#define f(i,j,n) for(int i=0; i<n; i++)
#define fu(i,j,n) for(int i=j; i>n; i--)
#define c(x, t) x t; cin>>t
#define ft int t; scanf("%d", &t); for(int c=1; c<=t; c++)
#define w(n) while(n--)
#define visited 1
#define unvisited -1
#define debug printf("\n<<CameHere<<\n")
#define mem(x,y) memset(x, y, sizeof(x))
#define pal(temp) pali(temp, 0, temp.size()-1)
#define nl printf("\n")
#define eps 1e-9
#define inf 1<<30
#define cases cout<<"Case #"<<c<<": "
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define min3(a,b,c) min(min(a,b),c)
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max3(a,b,c) max(max(a,b),c)
#define max4(a,b,c,d) max(max(a,b),max(c,d))
#define fin(prob) freopen("prob.in", "r", stdin)
#define fout(prob) freopen("prob.out", "w+", stdout)
#define pi (double)3.141592653589793
#define deb(x) cerr<< #x <<"="<<x<<endl;

/*Macro Ends here*/

using namespace std;

/*typedef start here*/

typedef string st;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector< pair <int, int> > vii;

/*typedef ends here*/

/*Important functions starts here */

template <class T> T abs (T a, T b=0)
{
    if(b==0) return (a<0) ? -a : a;
    return (a>b) ? (a-b) : (b-a);
}

template <class T> inline T gcd(T a, T b)
{
    if(a<0) return gcd(-a, b);
    if(b<0) return gcd(a,-b);
    return (b==0) ? a : gcd(b, a%b);
}

template <class T> inline ll pow(T a, T b)
{
    if(b==1) return a;
    ll t=pow(a, b/2);
    t*=t;
    if(!(b%2)) return t;
    return a*t;
}

bool pali(string temp, int i, int j)
{
    if(i>=j) return true;
    if(temp[i]==temp[j]) return pali(temp, i+1, j-1);
    return false;
}

/*Important functions ends here*/

/*Debug Extension ends here*/

template <typename F, typename S>
ostream& operator << (ostream& os, const pair< F, S>& p)
{
    return os<<"(" <<p.first<<", "<<p.second<<")";
}

template<typename T> ostream &operator << (ostream &os, const vector<T> &v)
{
    os<<"{";
    typename vector<T> :: const_iterator it;
    for(it= v.begin(); it!=v.end(); it++)
    {
        if(it!=v.begin()) os<<",";
        os<<*it;
    }
    return os<<"}";
}

template <typename T> ostream &operator << (ostream & os, const set<T>&v)
{
    os<<"[";
    typename set<T> :: const_iterator it;
    for(it=v.begin(); it!=v.end(); it++)
    {
        if(it!=v.begin()) os<<",";
        os<<*it;
    }
    return os<<"]";
}

template <typename F, typename S> ostream &operator << (ostream & os, const map<F,S>&v)
{
    os<<"[";
    typename map<F,S>::const_iterator it;

    for(it=v.begin(); it!=v.end(); it++)
    {
        if(it != v.begin()) os<<",";
        os<< it ->first<<"="<<it->second;
    }
    return os<<"]";
}


int main()
{
   fin(A-small-attempt0);
   fout(prob);
    ft
    {
        set<int>uSet;
        c(st, num);
        if(num=="0"){
            cases; cout<<"INSOMNIA\n";
            continue;
        }
        st asli=num;
        int mul=1;
        while(uSet.size()!=10)
        {
            num=asli;
            st tempstr;
            ll carry=0;
            for(int i=num.size()-1; i>=0; i--)
            {
                ll temp=mul*(num[i]-'0')+carry;
                int tnum=(char)((temp%10)+'0');
                uSet.insert(tnum);
                tempstr+=(char)tnum;
                if(temp>9) carry=temp/10;
                else carry=0;
            }
            if(carry)
            {
                tempstr+=(char)carry+'0';
                uSet.insert(carry+'0');
            }
            reverse(tempstr.begin(), tempstr.end());
            num=tempstr;
            mul++;
        }
        cases;
        cout<<num<<endl;
    }
    return 0;
}
