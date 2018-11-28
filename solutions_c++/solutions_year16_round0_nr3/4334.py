#include<bits/stdc++.h>
using namespace std;

#define SIZE_N 131072
#define SIZE_P 131072

bool flag[SIZE_N+5];
int primes[SIZE_P+5];
int n,j,solve=0,tt;

int seive()
{
    int i,j,total=0,val;
    for(i=2; i<=SIZE_N; i++) flag[i]=1;
    val=sqrt(SIZE_N)+1;
    for(i=2; i<val; i++)
        if(flag[i])
            for(j=i; j*i<=SIZE_N; j++)
                flag[i*j]=0;
    for(i=2; i<=SIZE_N; i++)
        if(flag[i])
            primes[total++]=i;

    return total;
}
long long int baseb(string s, int b){
    //cout<<s<<"   sb  "<<b<<endl;
    long long ans=0;
    long long temp=1;
    for(int j=s.size()-1;j>=0;j--){
        ans+=(s[j]-'0')*temp;
        temp*=b;
    }
    return ans;
}

void dfs(string s){
    //cout<<"dfs : "<<s<<endl;
    if(solve==j) return;
    if(s.size()<(n-1)){
        dfs(s+'1');
        dfs(s+'0');
    }
    else if(s.size()<n) dfs(s+'1');
    else{
        bool yes=1;
        vector<int> mv;
        for(int i=2;i<=10;i++){
            long long int a=baseb(s,i);
            //cout<<i<<"   i   a: "<<a<<endl;
            for(int j=0;primes[j]<a && j<tt;j++){
                if(a%primes[j]==0){
                    mv.push_back(primes[j]);
                    a=0;
                    break;
                }
            }
            if(a>0) yes=0;
        }
        if(yes==0) return;
        else{
            cout<<s<<" ";
            for(int j=0;j<mv.size();j++) cout<<mv[j]<<" ";
            cout<<"\n";
            solve++;
            return;
        }
    }
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    tt=seive();
    cin>>T;
    for(int t_c=1;t_c<=T; t_c++)
    {

        cin>>n>>j;
        string s="1";
        cout<<"Case #"<<t_c<<":"<<"\n";
        dfs(s);

    }
    return 0;
}
