#include<bits/stdc++.h>

using namespace std;

vector<int> insertinvector(vector<int> a ,int what)
{
    int c;
    for(c=0;c<a.size();c++)
    {
        if (what >= a[c])
        {
            break;
        }
    }
    a.insert(a.begin()+c,what);
    return a;
}

vector<int> timelapse(vector<int> a)
{
    for(int c=0;c<a.size();c++)
    {
    	if (a[c] >= 1)
    	{
    		a[c]--;
    	}    
    }
    return a;
}

void print_vector(vector<int> x)
{
    for(int q = 0;q<x.size();q++)
    {
        cout<<x[q]<<" ";
    }
    cout<<endl;
}

int solve(vector<int> x , int stall , int ans)
{
    /*print_vector(x);
    cout<<"STALLS : "<<stall<<endl;
    cout<<"ANS    : "<<ans<<endl;*/
    if((x[0] == 0) or (x[0] == 1)) return stall+1;
    else
    {
        //x.erase(x.begin());
        for(int i=1;i<=x[0]/2;i++)
        {
            vector<int> y = insertinvector(x,i);
            y = insertinvector(y,x[0]-i);
            y.erase(y.begin());
            int a = y[0] + stall;
            //print_vector(x);
            //print_vector(y);
            vector<int> z = timelapse(x);
            int b = z[0] + stall;
            //print_vector(z);
            a = min(ans,a);
            b = min(ans,b);
            if((b <= stall + 1 + (z[0]/2)) && (a <= stall + 1 + (y[0]/2))) ans = min(b,a);
            else if((b > stall + 1 + (z[0]/2)) && (a <= stall + 1 + (y[0]/2))) ans = min(solve(z,stall+1,a) ,a);
            else if((b <= stall + 1 + (z[0]/2)) && (a > stall + 1 + (y[0]/2))) ans = min(b,solve(y,stall+1,a));
            else ans = min(solve(z,stall+1,a) ,solve(y,stall+1,a));
        }
        return ans;
    }
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);

    int T;
    cin>>T;
    for(int a=1;a<=T;a++)
    {
        int D;
        cin>>D;
        vector<int> maina(0,0);
        for(int b=0;b<D;b++)
        {
            int x;
            cin>>x;
            maina = insertinvector(maina , x);
        }
        int ans;
        if (maina[0] == 1) ans = 1;
        else ans = solve(maina , 1 , maina[0]);
        cout<<"Case #"<<a<<": "<<ans<<endl;
    }
    return 0;

}
