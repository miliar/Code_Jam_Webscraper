#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define intialize(a)  memset(a,0,sizeof(a));
#define I  int
#define F  float
#define D  double
#define S  string
#define C  char
#define END  return 0;
#define SORT(v)  sort(v.begin(),v.end())
#define RSORT(v) sort(v.rbegin(),v.rend())
#define SZ(X) (int)(X).size()
typedef long long ll;
typedef vector<ll> integr;
typedef vector<char> character;
typedef vector <string> strings;
//---------------------------------------
int main()
{
freopen("A-large.in","r",stdin);
freopen("output.txt","w",stdout);
long long t ;
cin>>t;
for(int i=0;i<t;i++)
{
    long long int  sm ;
    cin>>sm;
    string input ;
    cin>>input;
    long long int cnt =0 ,cnt2=0,cur=0;
    for(long int i=0;i<input.size();i++)
    {
        long int temp = int(input[i])-48;
        if(cur<i && temp!=0)
        {
            cnt2+=(i-cur);
            cur+=temp+cnt2;
            cnt+=cnt2;
            cnt2=0;
        }
        else
        {
            cur+=temp ;
        }
       // cout<<cur << "  "<<cnt<<endl;
    }
    //cout<<input<<endl;
    cout<<"Case #"<<i+1<<": "<<cnt<<endl;
}
    return 0;
}
/*
bool isp (long long  x)
{
    if (x%2==0&&x!=2 || x==1)return false;
    for (long long  i=3; i*i<=x; i+=2)
    {
        if (x%i==0)return false;
    }
    return true;
}
//========================
cout.setf(ios::fixed);
cout.precision(10);
//==========================
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
*/
