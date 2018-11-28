/* coder: Anh Tuan Nguyen */
#include <bits/stdc++.h>
using namespace std;

string ToString(int64_t a)
{
    string res="";
    for(int i=a; i>0;i/=10)
    {
        res=(char)(48+i%10)+res;
    }
    return res;
}

int main()
{
#ifdef gsdt
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // gsdt

    int64_t t,n;
    scanf("%I64d",&t);
    for(int k=1; k<=t; k++)
    {
        scanf("%I64d",&n);
        if(n==0) cout<<"CASE #"<<k<<": "<<"INSOMNIA\n";
        else
        {
            bool numbers[10];
            memset(numbers,false,sizeof(numbers));
            for(int64_t i=1;; i++)
            {
                string tmp=ToString(n*i);
                for(unsigned int j=0; j<tmp.length(); j++)
                    numbers[tmp[j]-48]=true;
                bool stop=true;
                for(int j=0; j<10; j++)
                    if(!numbers[j]) stop=false;
                if(stop)
                {
                    cout<<"CASE #"<<k<<": "<<n*i<<endl;
                    break;
                }
            }
        }
    }

    return 0;
}

