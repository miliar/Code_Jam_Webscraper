#include<iostream>
#include<vector>
#include<algorithm>


using namespace std;

long long int compute(long long int N,long long int i)
{
    long long int val=((i*N)-((i*(i-1))/2))%1000002013;
    while(val<0)
        val+=1000002013;
    return val;
}

int main()
{
    int T;
    int N,M;
    int o,e,p,no;
    long long int sum1,sum2,val;
    int flag;
    vector< pair <int, pair<int,int> > > v; // stno,(type,no.)
    cin>>T;
    int y=T;
    while(T--)
    {
        cin>>N>>M;
        sum1=0;
        for(int i=0;i<M;i++)
        {
            cin>>o>>e>>p;
            sum1+=(((p)%1000002013)*compute(N,e-o))%1000002013;
            v.push_back(pair <int, pair<int,int> > (o, pair<int,int> (0,p) ) );
            v.push_back(pair <int, pair<int,int> > (e, pair<int,int> (1,p) ) );
        }
        sort(v.begin(),v.end());
        sum2=0;
            typeof(v.begin()) x= v.begin();

            for( typeof(v.begin()) it=v.begin(); it!=v.end();)
            {
//                cout<<(it->first)<<" "<<(it->second).first<<" "<<(it->second).second<<endl;
                if((it->second).first==0)
                {
                    x=it;
                    it++;
                }
                else
                {
                    val=compute(N,(it->first)-(x->first));
                    if((it->second).second>(x->second).second)
                    {
                        no=(x->second).second;
                        (it->second).second-=(x->second).second;
                        v.erase(x);       
                    }
                    else if((it->second).second<(x->second).second)
                    {
                        no=(it->second).second;
                        (x->second).second-=(it->second).second;
                        v.erase(it);
                    }       
                    else
                    {
                        no=(it->second).second;
                        v.erase(it);
                        v.erase(x);
                    }
                    it=x=v.begin();
                    sum2+=(no%1000002013*val%1000002013)%1000002013;
                }
            }
            val=(sum1-sum2)%1000002013;
            while(val<0)
                val+=1000002013;
            cout<<"Case #"<<y-T<<": "<<val<<endl;
    }
    return 0;
}
