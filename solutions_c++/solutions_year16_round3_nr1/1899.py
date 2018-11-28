#include<bits/stdc++.h>
using namespace std;
#define inf 999999
//#define MAX 100000
#define gcd(a,b) __gcd(a,b)
#define i64 long long
int getInt()
{
    int x;
    scanf("%d",&x);
    return x;
}
long long getLongLong()
{
    long long x;
    scanf("%lld",&x);
    return x;
}
double getDouble()
{
    double x;
    scanf("%lf",&x);
    return x;
}
char  getChar()
{
    char x;
    scanf("%c",&x);
    return x;
}
#define Int getInt()
#define Char getChar()
#define I64 getLongLong()
#define Double getDouble()
#define bug printf("debug\n");
#define $ln printf("\n");
#define rep(i,n) for(int i=0;i<n;i++)
#define lcm(a,b) a*b/gcd(a,b)
#define pb push_back
#define vi vector<int>
#define ii pair<int,int>
#define dd pair<double,double>
#define ll long long
#define ff first
#define ss second
#define all(v) v.begin(),v.end()
#define EPS numeric_limits<double>::epsilon()
template<typename t>
t abs(t a)
{
    if(a>=0)
        return a;
    return -a;
}
//error
/*#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); $ln; }

vector<string> split(const string& s, char c) {
	vector<string> v;
	stringstream ss(s);
	string x;
	while (getline(ss, x, c))
		v.emplace_back(x);
	return move(v);
}

void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
	cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << "  ";
	err(++it, args...);
}*/
void FastIO()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
}
////////////////////////////////////

int main()
{
    freopen("a.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases=Int,caseno=0;
    while(cases--)
    {
        int n=Int;
        vi p;
        int sum=0;
        rep(i,n)
        {
            p.pb(Int);
            sum+=p.back();
        }
        priority_queue<pair<int,int> >pq;
        for(int i=0; i<n; i++)
            pq.push({p[i],i});

        vector<string> ans;
        string tm;
        while(sum!=0)
        {
            auto v=pq.top();
            pq.pop();
            tm.clear();
            sum--;
            v.ff--;
            pq.push(v);
            tm.pb(v.ss+'A');
            if(sum>0&&sum!=2)
            {
                v=pq.top();
                pq.pop();
                sum--;
                v.ff--;
                pq.push(v);
                tm.pb(v.ss+'A');
            }
            ans.pb(tm);
        }


        printf("Case #%d:",++caseno);
        for(auto v:ans)
            cout<<" "<<v;
        cout<<endl;

    }
    return 0;

}

