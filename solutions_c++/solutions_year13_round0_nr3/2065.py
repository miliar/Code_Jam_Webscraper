#include<iostream>
#include<cstdio>
#include<vector>
#define s(n) scanf("%d",&n)
#define pb push_back
#define LL long long
using namespace std;
vector<int> vec;
vector<long long> fin;
bool fun(LL n)
{
    //cout<<"fun "<<n<<endl;
    int arr[30];
    int in=1;
    while(n)
    {
        arr[in]=n%10;
        n/=10;
        in++;
    }
    in--;
    for(int i=1;i<=in/2;i++)
    {
        if(arr[i]!=arr[in+1-i])
        {
            return 0;
        }
    }
    return 1;
}
  
int main()
{
    int t,c=0;
    long long g;
    s(t);
    for(int i=1;i<=10000000;i++)
    {
        if(fun(i))vec.pb(i);
    }
    vector<int>::iterator it;
    for(it=vec.begin();it!=vec.end();++it)
    {
        g=1LL*(*it)*(*it);
        if(fun(g))fin.pb(g);
    }
    LL a,b;
    vector<LL>::iterator it2;
    //cout<<"aman";
    while(t--)
    {
        c++;
        cin>>a>>b;
        int ans=0;
        it2=fin.begin();
        //cout<<fin.size()<<endl;
        //for(int i=0;i<39;i++)
//        {
//            cout<<*it2<<endl;
//            it2++;
//        }
            
        while((*it2)<a&&it2!=fin.end())it2++;
        while(*it2<=b&&it2!=fin.end()){ans++;it2++;}
        cout<<"Case #"<<c<<": "<<ans<<endl;
    }
}
    
    
