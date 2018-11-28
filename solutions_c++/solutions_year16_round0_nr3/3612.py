#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
ll power(int x, unsigned int y)
{
    ll temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}
int main()
{
    ios_base::sync_with_stdio(0);
    ll n,sum=0,count=0,t,m;
    ifstream f("C-small-attempt0.in");
    ofstream o("Cout.out");
    f>>t;
    int z=t;
    while(t--)
    {
       f>>n>>m;
       //cout<<t<<" "<<n<<" "<<m<<endl;;
       ull p=pow(2,n-1)+1;
       int flag=0;
        o<<"Case #"<<z-t<<": "<<endl;
        count=0;
       for(ull i=p,j=2;;i=i+2)
       {
            vi v;
            ull num=i,fu=0;
            while(num)
            {
                fu=fu*10+num%2;
                num=num/2;
            }
            num=0;
            while(fu)
            {
               num=num*10+fu%10;
               fu=fu/10;
            }
            //cout<<num<<" num "<<endl;
            j=2;
           while(j<11)
           {
               ull k=num,rev=0,ori=0;
               int pp=0;
               while(k>0)
               {
                   ll op=((k%10)*(power(j,pp)));
                   //cout<<op<<" "<<" op "<<" "<<rev<<" ";
                   rev=(rev+op);
                   k=k/10;
                   pp++;
               }
               //cout<<rev<<" "<<j<<" rev"<<endl;
                j++;
                ori=rev;
               int flag=0;
               for(int q=2;q*q<=ori;q++)
               {
                   if(ori%q==0)
                   {
                       flag=1;
                       break;
                   }
               }
               //cout<<ori<<endl;
               if(flag==1)
                v.push_back(ori);
           }
           //cout<<v.size()<<endl;
           if(v.size()==9)
           {
               count++;
              o<<num<<" ";
               for(int i=0;i<v.size();i++)
                {
                    for(int j=2;j<v[i];j++)
                    {
                        if(v[i]%j==0)
                        {
                            o<<j<<" ";
                            break;
                        }
                    }
                }
                o<<endl;
            }
            //cout<<endl;
        if(count==m)
            break;
        }
    }
	return 0;
}



