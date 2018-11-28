#include<iostream>
#include<cstdio>
#include<iomanip>

using namespace std;

double solve(double C,double F,double X)
{
        double prev,cur;
        double farm_cost=0.0;
        double rate=2.0;
        cur=X/rate;
        prev=cur+1;
        while(cur<prev)
        {
            prev=cur;
            farm_cost+=C/rate;
            rate+=F;
            cur=farm_cost+X/rate;
        }
        return prev;

}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	int c=1;
    double C,F,X;
    double ans;
    cin>>t;
    while(t--)
    {
        cin>>C;
        cin>>F;
        cin>>X;
        ans=solve(C,F,X);
        cout<<"Case #"<<c<<": "<<std::fixed<<std::setprecision(7)<<ans<<"\n";
        c++;
    }
	return 0;
}
