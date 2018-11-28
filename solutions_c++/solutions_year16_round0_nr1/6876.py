#include<bits/stdc++.h>

using namespace std;

int main()
{

    set<int> s;

    long long int t , n , val ,it,no,r;
    cin>>t;
    for(int i =0;i<t;i++)
    {
        it = 2;
        cin>>n;
        val = n;
        if(n == 0)
        {
           cout<<"Case #"<<i+1<<":"<<" "<<"INSOMNIA"<<endl;
           continue;
        }
        while(s.size() != 10)
        {
            no = n;
           while(n>0)
            {
                r = n%10;
                n = n/10;
                s.insert(r);
                if(s.size() == 10)
                {
                    break;
                }
            }
            if(s.size() == 10)
            {
                break;
            }
            n = val*it;
            it++;
            //cout<<n<<endl;

        }
       cout<<"Case #"<<i+1<<":"<<" "<<no<<endl;
       s.erase(s.begin() ,s.end());
    }

    return 0;
}
