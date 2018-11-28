#include<iostream>
#include<vector>
using namespace std;
long long gcd(long long a,long long b)
{
 if(b == 0)
       return a;
 else
     return gcd(b, a%b);
}
struct {
    bool operator() ( pair<int,long long> i, pair<int,long long> j){
        if(i.second > j.second)
            return true;
        if(i.second == j.second && i.first > j.first)
            return true;
        return false;
    }
}compare;
int main()
{
    freopen("/Users/saravanakumars/program0.txt","r",stdin);
     freopen("/Users/saravanakumars/program0.out","w",stdout);
    long long t;
    cin>>t;
    for(long long i=0;i<t;i++)
    {
        long long n,b;
        long long lcm = 1LL;
        cin>>b>>n;
        vector< pair<long long,long long> > c(b);
        vector <long long> v(b);
        for(long long j=0;j<b;j++)
        {
            c[j].first = j;
            cin>>c[j].second;
            v[j] = c[j].second;
            lcm = (lcm * c[j].second)/gcd(lcm,c[j].second);
        }
        long long nof = 0;
        for(long long j=0;j<b;j++)
        {
            nof += lcm/v[j];
        }
        n=n%nof;
        if(n==0)
        {
            n=nof;
        }
       // cout<<"lcm is "<<lcm<<endl;
       // cout<<"nof is "<<nof<<endl;
        if(n<=b)
        {
            if(n!=0)
            cout<<"Case #"<<(i+1)<<": "<<n<<endl;
            else
                cout<<"Case #"<<(i+1)<<": "<<b<<endl;
            continue;
        }
        n-=b;
        //cout<<"n is "<<n<<endl;
        make_heap(c.begin(),c.end(),compare);
        long long in;
        for(long long j=0;j<n;j++)
        {
            pair<int,long long> temp = c.front();
            in = temp.first + 1;
          //  cout<<"inside "<<temp.first<<" "<<temp.second<<endl;
            pop_heap(c.begin(),c.end(),compare);
            c.pop_back();
            c.push_back(make_pair(temp.first, temp.second + v[temp.first]));
            push_heap(c.begin(),c.end(),compare);
        }
        cout<<"Case #"<<(i+1)<<": "<<in<<endl;
    }
}
