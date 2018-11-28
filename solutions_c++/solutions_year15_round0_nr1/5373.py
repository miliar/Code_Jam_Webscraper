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
        int S;
        cin>>S;
        string s;
        cin>>s;
        int p=0;
        p+=(s[0]-'0');
        int ans=0;
        for(int i=1;i<=S;i++)
        {
            if(p>=i)
                p+=(s[i]-'0');
            else
            {
                ans+=i-p;
                p=i+(s[i]-'0');
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<"\n";
    }

    return 0;
}

