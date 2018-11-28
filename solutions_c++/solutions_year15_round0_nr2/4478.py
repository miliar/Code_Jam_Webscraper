/*
By : Yash Kumar
Dhirubhai Ambani Institute Of Information And Communication Technology, Gandhinagar (DA-IICT GANDHINAGAR)
1st Year ICT BTECH student
*/
#include<bits/stdc++.h>

#define lli long long int
#define llu unsigned long long int

const double EPS = 1e-24;
const lli MOD = 1000000007ll;
const double PI = 3.14159265359;
int INF = 2147483645;

template <class T>T Max2(T a,T b){return a<b?b:a;}
template <class T>T Min2(T a,T b){return a<b?a:b;}
template <class T>T Max3(T a,T b,T c){return Max2(Max2(a,b),c);}
template <class T>T Min3(T a,T b,T c){return Min2(Min2(a,b),c);}
template <class T>T Max4(T a,T b,T c,T d){return Max2(Max2(a,b),Max2(c,d));}
template <class T>T Min4(T a,T b,T c,T d){return Min2(Min2(a,b),Max2(c,d));}
template <class T>void Swap(T& a,T& b){T temp;temp=a;a=b;b=temp;}

using namespace std;

int N;
int ans;

void solve(int d,vector<int> v)
{
    if(d>ans)
        return;
    /*cout<<d<<"-> ";
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<" ";
    cout<<endl;*/
    if(v.size()==0)
    {
       ans=Min2(ans,d);
       return;
    }

    sort(v.begin(),v.end());
    vector<int> v1;

    for(int i=0;i<v.size();i++)
    {
        if(v[i]>1)
            v1.push_back(v[i]-1);
    }
    solve(d+1,v1);

    for(int i=v.size()-1;i>=0;i--)
    {
        vector<int> v2(v);
        if(v[i]>1)
        {
            int x=v[i];
            v2.erase(v2.begin()+i);

            for(int j=1;j<=x/2;j++)
            {
                vector<int> v3(v2);
                v3.push_back(j);
                v3.push_back(x-j);
                solve(d+1,v3);
            }

            break;
        }
    }
}

int main()
{
    std::ios::sync_with_stdio(false);
    //cin.tie(NULL);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>N;
        vector<int> v;
        for(int i=0;i<N;i++)
        {
            int x;
            cin>>x;
            v.push_back(x);
        }
        ans=20;

        solve(0,v);

        cout<<"Case #"<<t<<": "<<ans<<"\n";
    }

    return 0;
}

