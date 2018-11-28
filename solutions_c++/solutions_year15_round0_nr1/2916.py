#include <bits/stdc++.h>
#define mp make_pair
#define pii pair<int,int>
#define pb push_back
#define Max(a,b)a>b?a:b
#define Min(a,b)a<b?a:b
#define read() freopen("in.txt","r",stdin)
using namespace std;
template <typename T>
string NumberToString ( T Number )
{
    ostringstream ss;
    ss << Number;
    return ss.str();
}
int Set( int n , int pos)
{
    return ( n=n | 1<<pos );
}
int reset(int N,int pos)
{
    return N= N & ~(1<<pos);
}
bool check(int N,int pos)
{
    return (bool)(N & (1<<pos));
}
typedef long long ll;

//bool comp(const node &lhs, const node &rhs) { return lhs.b < rhs.b; }

#define PI 3.141592653589793
int main()
{
    //read();
    //freopen("out.txt","w",stdout);
    int test , kase=1;
    cin>>test;
    while(test--)
    {
        int k;
        cin>>k;
        string in ;
        cin>>in;

        int need=0, people=0;
        for( int i =0; i<in.size(); i++) {

            if(in[i]!='0')
            {
                if(i>people)
                {
                    need+=(i-people);
                    people+=(i-people);
                    people+=(in[i]-'0');
                }
                else
                {
                    people+=(in[i]-'0');
                }
            }
        }
        printf("Case #%d: %d\n",kase++,need);
    }
}
