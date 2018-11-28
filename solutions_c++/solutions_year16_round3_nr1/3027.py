#include<bits/stdc++.h>
using namespace std;
#define ll long long

multiset< pair<ll,char> > ms;
multiset< pair<ll,char> > ::iterator it , pit , fi;

pair<ll,char> p;

int main()
{
        freopen("inp.in","r",stdin);
    freopen("opt.out","w",stdout);

    ll t,n,i,a;
    char ch;
    cin>>t;
    ll z = 0;
    while(z < t)
    {
        ms.clear();
        cout<<"Case #"<<z+1<<": ";
        cin>>n;
        ch = 'A';
        for(i=0;i<n;i++)
        {
            cin>>a;
            p = make_pair(a,ch);
            ms.insert(p);
            ch++;
        }

        while(ms.size() > 0)
        {
            it = pit = ms.end();
            it--;pit--;pit--;
            if((*it).first <= 0)
                break;
            if( (*it).first -2 >= (*pit).first )
            {
                cout<<(*it).second<<(*it).second<<" ";
                a = (*it).first - 2;
                ch = (*it).second;
                fi = ms.find((*it));
                ms.erase(fi);
                if(a > 0)
                ms.insert(make_pair(a,ch));
            }
            else
            if( (*it).first -1 > 0 && (*pit).first-1 > 0)
            {
                cout<<(*it).second<<(*pit).second<<" ";
//                (*it).first--;
                a = (*it).first - 1;

                ch = (*it).second;
                fi = ms.find((*it));
                ms.erase(fi);
                if(a > 0)
                ms.insert(make_pair(a,ch));

//                (*pit).first--;
                a = (*pit).first - 1;
                ch = (*pit).second;
                fi = ms.find((*pit));
                ms.erase(fi);
                if(a >0)
                ms.insert(make_pair(a,ch));
            }
            else
            {
                if( ms.size() %2==1 && ms.size() > 1  && (*it).first == 1 && (*pit).first == 1)
                {
                    cout<<(*it).second<<" ";
//                    (*it).first--;
                    a = (*it).first - 1;
                    ch = (*it).second;
                    fi = ms.find((*it));
                    ms.erase(fi);
                    if(a > 0)
                    ms.insert(make_pair(a,ch));
                }
                else
                if(  ms.size() > 1  && (*it).first == 1 && (*pit).first == 1 )
                {
                    cout<<(*it).second<<(*pit).second<<" ";
//                (*it).first--;
                    a = (*it).first - 1;

                    ch = (*it).second;
                    fi = ms.find((*it));
                    ms.erase(fi);
                    if(a > 0)
                    ms.insert(make_pair(a,ch));

    //                (*pit).first--;
                    a = (*pit).first - 1;
                    ch = (*pit).second;
                    fi = ms.find((*pit));
                    ms.erase(fi);
                    if(a >0)
                    ms.insert(make_pair(a,ch));

                }
                else
                {
                    cout<<(*it).second<<" ";
//                    (*it).first--;
                    a = (*it).first - 1;
                    ch = (*it).second;
                    fi = ms.find((*it));
                    ms.erase(fi);
                    if(a > 0)
                    ms.insert(make_pair(a,ch));
                }
            }

        }
       cout<<endl;
       z++;
    }
    return 0;
}
