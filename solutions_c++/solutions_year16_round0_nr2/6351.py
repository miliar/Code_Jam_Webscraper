#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector < long long > vll;
typedef unsigned long long ull;
typedef pair < long long,  long long > pll;
typedef pair < int,  int > pii;
typedef vector < int > vii;

#define ff first
#define ss second
#define sz size()
#define clr clear()
#define len length()
#define pb push_back
#define mp make_pair

const int N = 1e5 + 500;
const ll mod = 1e9 + 7;
const ll INF = 1LL << 57LL;

//Fast expo

ll expo(ll a , ll b)
{
    if(b==0)
        return 1;
    else if(b%2==0)
        return expo(a*a,b/2);
    else
        return a*expo(a*a,b/2);
}

//comparing pair wrt to 2nd

bool compare(const pii &i, const pii &j)
{
    return i.ss < j.ss;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ifstream infile;
    ofstream outfile;
    infile.open("B-large.in");
    outfile.open("outfile1.txt");
    int t;
    infile>>t;
    //cin>>t;
    int p=t;
    while(t--)
    {
        string s;
        infile>>s;
        int ans=0;
        //int i=0;
        int n=s.size();
        /*while(i<n && s[i]=='-')
        {
            i++;
        }
        if(i!=0)
        {
            ans=1;
            k=-1;
        }*/

        /////part 1

        /*int k=1;
        int i;
        bool positive=false,negative=false;
        for(i=0;i<n;i++)
        {
            if(s[i]=='+')
            {
                positive=true;
                if(k==-1)
                {
                    k=1;
                    ans++;
                }
            }
            else if(s[i]=='-')
            {
                negative=true;
                if(k==1)
                {
                    ans++;
                    k=-1;
                }
            }
        }
        if(n!=1 && s[i-1]=='-' && positive)
        {
            ans++;
        }
        else if(n!=1 && s[i-1]=='+' && negative)
        {
            ans--;
        }*/

        /////////part2
        int pre_state;
        if(s[0]=='-')
        {
            pre_state=-1;
        }
        else
        {
            pre_state=1;
        }
        for(int i=0;i<n;i++)
        {
            if(s[i]=='+')
            {
                if(pre_state==-1)
                {
                    ans++;
                    pre_state=1;
                }
            }
            else if(s[i]=='-')
            {
                if(pre_state==1)
                {
                    ans++;
                    pre_state=-1;
                }
            }
        }
        if(pre_state==-1)
        {
            ans++;
        }
        outfile<<"Case #"<<p-t<<": "<<ans<<endl;
        //cout<<s<<" Case #"<<p-t<<": "<<ans<<endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
