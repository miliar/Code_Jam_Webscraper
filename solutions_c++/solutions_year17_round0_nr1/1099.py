#include<bits/stdc++.h>
//#include <boost/multiprecision/cpp_int.hpp>
#define PI acos(-1)
#define fast() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define ll long long int
#define mem(a,b) memset(a,b,sizeof(a))
#define MX 100005
#define MXX 1000005
#define  s second
#define f first
#define mod 1000000007
#define inf 200000000000
//int ex[]={1,-1,0,0};
//int wye[]={0,0,1,-1};
using namespace std;
int t,k,siz,an=0,tmp;
string s;
bool flag;

int main()
{
    //fast();
    freopen("A-large.in","r",stdin);
    freopen("output_large_file.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>s>>k;
        flag=true;
        an=0;
        siz=s.size();
        for(int j=0;j<=siz-k;j++){
            tmp=j;
            if(s[j]=='-'){
                while(tmp<j+k){
                    if(s[tmp]=='-') s[tmp]='+';
                    else s[tmp]='-';
                    tmp++;
                }
                an++;
            }
        }
        for(int j=siz-k+1;j<siz;j++) if(s[j]=='-') flag=false;
        cout<<"Case #"<<i<<": ";
        if(flag) cout<<an<<endl;
        else cout<<"IMPOSSIBLE"<<endl;



    }
    return 0;
}

