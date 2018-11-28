#include<bits/stdc++.h>

using namespace std;

int main()
{

    freopen("A-large.txt", "r" ,stdin);
    freopen("sabbiroutput.txt", "w" ,stdout);

    long long int g,b,c,i,j;

    map<long long int ,long long int >m;
    cin>>g;

    for(i=1; i<=g; i++)
    {
        cin>>b;
        m.clear();
        if(b==0)cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
        {
            j=b;
            while(j)
            {

                if(m.size()==10)
                {
                    cout<<"Case #"<<i<<": "<<j-b<<endl;
                    break;
                }
                else if(j<10)m[j]++;
                else if(j>9)
                {

                    c=j;
                    while(c)
                    {
                        m[c%10]++;
                        c/=10;
                    }
                }
                j+=b;
            }

        }
    }
}
