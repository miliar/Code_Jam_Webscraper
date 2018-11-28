#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
        int t;
        cin>>t;
        ll i=0;
        while(t--)
        {
               cout<<"Case #"<<i+1<<": ";
               ll p;
                cin>>p;
                if(p==0)
                {
                        cout<<"INSOMNIA"<<endl;
                        i++;
                        continue;
                }
                ll m=1;
                ll a[10]={};
                ll o;
                while(true)
                {
                o=p*m;
                stringstream ss;
                ss << o;
                string str = ss.str();
                int  l=str.length();
                for(int j=0;j<l;j++)
                        a[char(str[j])-'0']++;
                int k=0;
                for(int j=0;j<10;j++)
                        if(a[j]!=0)
                                k++;
                if(k==10)
                        break;
                m++;
                }
                cout<<o<<endl;
                i++;
        }
}
