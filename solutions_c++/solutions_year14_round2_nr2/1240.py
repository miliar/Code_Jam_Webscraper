#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("input.cpp","r",stdin);
        freopen("output.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    int test,a,b,k,i,j,res,t,temp;
    cin >> test;
    t=1;
    while(t<=test)
    {
        res=0;
        cin >> a >> b >> k;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                temp=i & j;
                if(temp<k)
                    res++;
            }
        }
        cout << "Case #" << t << ": " << res << endl;
        t++;
    }
    return 0;
}
