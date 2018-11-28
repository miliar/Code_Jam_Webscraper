#include<bits/stdc++.h>

using namespace std;

int main()
{   ifstream f1;
    ofstream f2;
    f1.open("inp.in",ios::in);
    f2.open("out",ios::out);
    long int n,t,smax,a[100],f;
    char s[100];
    f1>>n;
    cout<<n;
    t=n;
    while(t)
    {   long int sum=0;
        f=0;
            f1>>smax>>s;
            for(int i=0; i<smax+1;i++)
            a[i]=s[i]-'0';

            for(int i=1; i<smax+1;i++)
            {   sum+=a[i-1];
                if(sum<i)
                {   f=f+i-sum;
                    sum+=i-sum;
                }
            }
        f2<<"Case #"<<n-t+1<<":"<<" "<<f<<endl;
        t--;
    }
    f1.close();
    f2.close();
}
