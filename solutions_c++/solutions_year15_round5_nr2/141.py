#include <iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#define X first
#define Y second

using namespace std;

typedef pair<int,int> pii;
long long n,k,s[2000],y,MIN,MAX,ans,sum;
vector<pii>vec;

int main()
{
    ifstream cin("B-large.in");
    ofstream cout("B-large.out");
    int qw;
    cin>>qw;
    for(int q=1;q<=qw;q++)
    {
        cin>>n>>k;
        vec.clear();
        for(int i=0;i<n-k+1;i++)
            cin>>s[i];
        ans=sum=0;
        for(int i=0;i<k;i++)
        {
            int x=i;
            y=MIN=MAX=0;
            while(x+k<n)
            {
                y+=s[x+1]-s[x];
                MIN=min(MIN,y);
                MAX=max(MAX,y);
                x+=k;
              //  cout<<x<<" "<<y<<endl;
            }
           // cout<<i<<" "<<MIN<<" "<<MAX<<endl;
            vec.push_back(pii(MIN,MAX-MIN));
            sum+=MIN;
            ans=max(ans,MAX-MIN);
        }
        sum/=k;
        for(int i=0;i<vec.size();i++)
            s[0]-=sum-vec[i].X;
        if(s[0]<0)
            s[0]=(k-(-s[0])%k)%k;
        else
            s[0]%=k;
        for(int i=0;i<vec.size();i++)
            s[0]-=min(s[0],ans-vec[i].Y);
        if(s[0]>0)
            ans++;
        cout<<"Case #"<<q<<": "<<ans<<endl;
    }
}
