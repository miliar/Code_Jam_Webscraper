#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main ()
{

    freopen("A-large.txt","r",stdin);
    freopen("output2.txt","w",stdout);
    vector <int> num;
    long long t,n,a,b,i,j,cas,store;

    num.push_back(0);
    num.push_back(1);
    num.push_back(2);
    num.push_back(3);
    num.push_back(4);
    num.push_back(5);
    num.push_back(6);
    num.push_back(7);
    num.push_back(8);
    num.push_back(9);

    scanf("%lld", &t);
    cas = 1;
    while(t--)
    {
        scanf("%lld", &n);
        if(n==0)
        {
                      cout<<"Case #"<<cas<<": "<<"INSOMNIA"<<endl;
        }

        else
        {
                i = 1;
        while(num.size()!=0)
        {

            a = n*i;
            store = a;
            while(a!=0)
            {

                b = a%10;
                for(j=0; j<num.size(); j++)
                {
                    if(num[j]==b)
                    {
                           num.erase(num.begin()+j);
                    }
                }
                a=a/10;
            }
            i++;
        }
        cout<<"Case #"<<cas<<": "<<store<<endl;
          num.push_back(0);
            num.push_back(1);
            num.push_back(2);
                    num.push_back(3);
            num.push_back(4);
                        num.push_back(5);
                num.push_back(6);
            num.push_back(7);
                    num.push_back(8);
                    num.push_back(9);

    }
            cas++;
        }
            return 0;
}
