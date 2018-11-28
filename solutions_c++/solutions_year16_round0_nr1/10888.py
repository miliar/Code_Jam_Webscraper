#include <bits/stdc++.h>
using namespace std;
int main()
{
   // easy < sample.txt
   ios::sync_with_stdio(false);
   cin.tie(NULL);
    int t;
    cin>>t;
    int z;
    for(z=1;z<=t;z++)
    {
       // cout<<z<<" sdsdf "<<t<<"\n";
        long long n,tn,i;
        cin>>n;
        //tn=n;
        bool mark[10];
        for(i=0;i<=9;i++)
            mark[i]=false;
        int c=0;
            for(i=1;i<=100;i++)
            {
                long long tmp=i*n;
                while(tmp)
                {
                    if(!mark[tmp%10])
                    {
                        mark[tmp%10]=true;
                        c++;
                    }
                    tmp/=10;
                }
                if(c==10)
                    break;
            }
                if(c==10)
            	cout<<"Case #"<<z<<": "<<i*n<<"\n";
                else
            	cout<<"Case #"<<z<<": INSOMNIA"<<"\n";
    }
    return 0;
}
