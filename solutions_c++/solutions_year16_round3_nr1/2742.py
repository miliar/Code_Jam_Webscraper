#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define sv() int t; scanf("%d",&t); while(t--)
struct data{
ll v;
char p;
};

bool compareByLength(const data &a, const data &b)
{
    return a.v < b.v;
}

int main(){
    ll te; scanf("%lld",&te); for(int j=0;j<te;j++){
    ll n,t,sum=0; scanf("%lld",&n);
    vector<data> arr;
    for(int i=0;i<n;i++){
        scanf("%lld",&t); arr.push_back({t,(char)(65+i)}); sum+=t;
    }
    std::sort(arr.begin(), arr.end(), compareByLength);
    stack<char> s;
    for(int i=0;i<n && sum!=0;i=(i+1)%n)
    if(arr[i].v!=0) {s.push(arr[i].p); sum-=1; arr[i].v-=1;}
    cout<<"Case #"<<j+1<<": ";
    while(!s.empty()){
        if(!s.empty())  {cout<<s.top(); s.pop();}
        if(s.size()==2) {}
        else if(!s.empty())  {cout<<s.top(); s.pop();}
        printf(" ");
    }
    printf("\n");
    }
return 0;
}
