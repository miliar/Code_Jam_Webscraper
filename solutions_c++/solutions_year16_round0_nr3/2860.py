#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#define ll long long
using namespace std;

int main()
{	ll x,y,z,i,j,k;
    cin>>x>>y>>z;
    cout<<"Case #1:\n";
    vector<ll> v;
    v.push_back(2);
    v.push_back(3);
    for(i=5;i<=10000000;i+=2)
    {	ll l=sqrt(i),c=0;
        for(j=0;v[j]<=l;j++)
        {	if(i%v[j]==0)
            {	c=1;
                break;
            }
        }
        if(!c)
        	v.push_back(i);
    }
    ll c=0;
    for(i=32769;i<65526;i+=2)
    {	ll d=0,i1=i;
        vector<ll> v1;
        vector<bool> str;
        while(i1)
        {	str.push_back(i1%2);
            i1/=2;
        }
        for(j=2;j<=10;j++)
        {	ll s=0,p;
            for(p=0;p!=str.size();p++)
				s+=(pow(j,p)*str[p]);
            p=0;
            for(k=0;k!=v.size() && v[k]<=sqrt(s);k++)
            {	if(s%v[k]==0)
                {	p=1;
                    v1.push_back(v[k]);
                    break;
                }
            }
            if(!p)
            {	d=1;
                break;
            }
        }
        if(!d)
        {	for(k=str.size()-1;k>=0;k--)
				cout<<str[k];
            for(k=0;k!=v1.size();k++)
				cout<<" "<<v1[k];
            cout<<endl;
            c++;
        }
        if(c==50)
			break;
    }
    return 0;
}
