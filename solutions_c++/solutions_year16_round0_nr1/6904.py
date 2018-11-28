#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,p;
    ifstream IF;
    ofstream OF;
    IF.open("input.txt");
    OF.open("output.txt");
    IF>>t;
    for(p=1;p<=t;p++)
    {
        long long int k,i,j,l;
        bool a[10]={0};
        IF>>k;
        if(k==0)
        {
            OF<<"Case #"<<p<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            i=1;
            while(1)
            {
                l=i*k;
                while(l)
                {
                    a[l%10]=1;
                    l/=10;
                }
                for(j=0;j<10;j++)
                {
                    if(!a[j])
                        break;
                }
                if(j==10)
                {
                    l=i*k;
                    break;
                }
                i++;
            }
            OF<<"Case #"<<p<<": "<<l<<endl;
        }
    }
    IF.close();
    OF.close();
    return 0;
}

