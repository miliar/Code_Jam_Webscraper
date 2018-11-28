#include<bits/stdc++.h>
using namespace std;

int mark[100000];
std::vector<int>prime;
std::vector<int>vec;

void solve()
{
    long long i,j;
    for(i=4; i<=9999; i+=2)
        mark[i]=1;
    prime.push_back(2);
    for(i=3; i<=9999; i+=2)
    {
        if(mark[i])
            continue;
        prime.push_back(i);
        for(j=i*i; j<=9999; j+=2*i)
            mark[j]=1;
    }

}

long long int power(int x,int y,int z)
{
    if(y==0)
        return (1%z);
    long long int ans;
    if(y&1)
    {
        ans=x;
        ans=(ans*power(x,y-1,z))%z;
        return ans;
    }
    ans= power(x,y/2,z);
    return (ans*ans)%z;
}

bool isprime(long long int val)
{
    for(int i=0; i<prime.size() && prime[i]*prime[i]<=val; i++)
        if((val%prime[i])==0)
            return false;
    return true;
}

int rem;

bool func()
{
    int i,j,k,mar[11];
    for(i=0;i<=10;i++)
        mar[i]=0;

    for(i=0; i<prime.size(); i++)
    {
        for(j=2; j<=10; j++)
        {
            rem=power(j,31,prime[i]);
            rem=(rem+1)%prime[i];
            for(k=0; k<vec.size(); k++)
                rem=(rem+ power(j,vec[k],prime[i]))%prime[i];
            if(rem==0)
                mar[j]=prime[i];
        }
        for(j=2; j<=10; j++)
            if(mar[j]==0)
                break;
        if(j==11)
            break;
    }
    if(j==11)
    {
        string str="00000000000000000000000000000000";
        str[0]='1';
        str[31]='1';
        for(i=0; i<vec.size(); i++)
            str[vec[i]]='1';
        reverse(str.begin(),str.end());
        cout<<str<<" ";
        for(i=2; i<=10; i++)
            cout<<mar[i]<<" ";
        printf("\n");
        return true;
    }

    return false;
}

int X,no,cnt,n,J,t,i,j;
long long int ans,val,temp,x;
std::map<string,int>m;
std::set<int>s;
std::set<int>::iterator it;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    solve();
    scanf("%d",&t);
    while(t--)
    {
        X++;
        cnt=0;
        printf("Case #%d:\n",X);
        scanf("%d %d",&n,&J);
        n=n-2;
        while(1)
        {
        no= (rand()%n)+1;
       // cout<<no<<"\n";

        s.clear();
        while(s.size()<no)
            s.insert((rand()%n)+1);

        vec.clear();

        for(it=s.begin(); it!=s.end(); it++)
            vec.push_back(*it);

        string str="";

        for(i=0;i<vec.size();i++)
            str.push_back(vec[i]+48);

       // cout<<str<<"\n";

        if(m.find(str)!=m.end())
            continue;
        else
            m[str]=1;

        if(func())
            cnt++;

        if(cnt==J)
            break;
        }
    }
    return 0;
}
