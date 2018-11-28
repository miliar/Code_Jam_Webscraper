#include<bits/stdc++.h>
using namespace std;

int main()
{
    ofstream myfile;
    myfile.open ("example.txt");
    int a,i=0,t,x,val,q,res;
    while(cin>>t)
    {
        int cs=0;
        while(t--)
        {
            i++;
            cs++;
            cin>>x;

            if(x==0)
            {
                cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
                myfile<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            }
            else{
            set<int> SET;
            q=0;
            while(SET.size()!=10)
            {
                q++;
                val=x*q;
                res=val;

                while(val!=0)
            {
                SET.insert(val%10);
                val/=10;
            }
           // cout<<SET.size()<<endl;
            }

                cout<<"Case #"<<i<<": "<<res<<endl;
                myfile<<"Case #"<<i<<": "<<res<<endl;

            }


            }

        }


    }

