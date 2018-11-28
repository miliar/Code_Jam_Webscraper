#include<iostream>
#include<vector>

using namespace std;

vector <long long> fns;

int ispalindrome(long long n)
{
    long long rev=0,temp=n;
    
    while(n>0)
    {
              rev = rev*10 + n%10;
              n/=10;
    }
    return (temp==rev);
}

void precalc()
{
     long long tmp;
     int i;
     for(i=1;i<10000000;i++)
     {
        tmp=i;
        if(ispalindrome(tmp))
        {
            if(ispalindrome(tmp*tmp))
            {
               fns.push_back(tmp*tmp);
               //cout<<tmp*tmp<<":";
            }
        }
     }
}

int main()
{
    freopen("fnsil1.in","r",stdin);
    freopen("fnsol1.txt","w",stdout);
    int t,tc=1;
    long long a,b;
    precalc();
    scanf("%d",&t);
    while(t--)
    {
              scanf("%lld%lld",&a,&b);
              //int a_i,b_i;
              //cout<<fns.size();
              vector<long long>::iterator ai,bi;
              ai = lower_bound(fns.begin(),fns.end(),a);
              bi = upper_bound(fns.begin(),fns.end(),b);
              printf("Case #%d: ",tc++);
              cout<<bi-ai<<endl;       
    }
    return 0;
}
