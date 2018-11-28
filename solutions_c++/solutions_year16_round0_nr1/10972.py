#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int y=1;y<=t;y++)
    {
        long long n,i,res;
        unsigned long long q,rem,flag=0,num;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<y<<": INSOMNIA"<<endl;
        }
        else
        {
        set<int> s;
        for(i=1;;i++)
        {
            q=n*i;
            res=q;
            while(q)
            {
                rem=q%10;
                s.insert(rem);
                  q/=10;
                if(s.size()==10)
                {
                    flag=1;
                    num=res;
                    break;
                }

            }
            if(flag==1)
            {
                break;
            }
        }
        cout<<"Case #"<<y<<": "<<num<<endl;
        }
    }
    return 0;
}
