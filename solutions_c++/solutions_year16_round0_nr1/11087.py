#include <bits/stdc++.h>
using namespace std;

int main()
{
     freopen("input.txt","r",stdin);
     freopen("out.txt","w",stdout);
    int n,number,mod=0,old=0,neww=0,sum=0;
    cin>>n;
    set<int> s;
    set<int>::iterator it;

    for(int i=1; i<=n; i++)
    {
        cin>>number;
        old = number;
        s.clear();
        if(old==0)
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else
        {
            int j = 1;
            while(true)
            {
                neww = j * old;
                number = neww;
                while (neww!=0)
                {
                    mod = neww%10;
                    neww = neww/10;
                    s.insert(mod);
                }
              j++;
            if(s.size() == 10)
            {
             cout<<"Case #"<<i<<": "<<number<<endl;
             break;
            }
            }
        }
    }
    return 0;
}
