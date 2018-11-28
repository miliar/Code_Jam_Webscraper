#include <iostream>
#include <cstdio>
#define MOD 1000002013
using namespace std;

long long entries[1000][3];
pair<long long, pair<long long, long long> > sent[2000];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc;
    cin >> tc;
    for(int nt=0; nt<tc; nt++)
    {
        int N, M;
        cin >> N >> M;
        for(int i=0; i<M; i++)
            cin >> entries[i][0] >> entries[i][1] >> entries[i][2];

        long long totalcost=0;
        for(int i=0; i<M; i++)
        {
            long long k=-entries[i][0]+entries[i][1];
            long long thiscost=(k*N-(k*(k-1))/2)%MOD;
            totalcost+=(thiscost*entries[i][2])%MOD;
            totalcost%=MOD;
        }
        //cout << totalcost << endl;
        for(int i=0; i<M; i++)
        {
            sent[2*i]=make_pair(entries[i][0], make_pair(0, entries[i][2]));
            sent[2*i+1]=make_pair(entries[i][1], make_pair(1, entries[i][2]));
        }
        sort(sent,sent+2*M);
        //for(int i=0; i<2*M; i++)
        //    cout << sent[i].first << " " << sent[i].second.first << " " << sent[i].second.second << endl;
        int len=2*M;
        int changed=1;
        long long fincost=0;
        while(changed)
        {
            changed=0;
            for(int i=0; i<len-1; i++)
            {
                if(sent[i].second.first == 0 && sent[i+1].second.first == 1)
                {
                    long long k=sent[i+1].first-sent[i].first;
                    long long thiscost=(k*N-(k*(k-1))/2)%MOD;
                    long long p=min(sent[i+1].second.second,sent[i].second.second);
                    fincost+=(thiscost*p)%MOD;
                    fincost%=MOD;
                    sent[i+1].second.second-=p;
                    sent[i].second.second-=p;
                    changed=1;
                }
            }
            //cout << fincost << endl;
            int c=0;
            for(int i=0; i<len; i++)
            {
                sent[i-c]=sent[i];
                if(sent[i].second.second == 0)
                    c++;
            }
            len-=c;
        }
        cout << "Case #" << nt+1 << ": " << (totalcost-fincost+MOD)%MOD << endl;
    }
}
