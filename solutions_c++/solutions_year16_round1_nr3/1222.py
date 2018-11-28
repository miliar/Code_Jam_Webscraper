#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int kras=1; kras<=tc; kras++)
    {
        printf("Case #%d: ", kras);
        //printf("\n");
        int n;
        scanf("%d", &n);
        vector<int> bff(n);
        for(int i=0; i<n; i++)
        {
            scanf("%d", &bff[i]);
            bff[i]--;
        }
        int ans=0;
        for(int bs=1; bs<(1LL<<n); bs++)
        {
            vector<int> v;
            for(int i=0; i<n; i++)
            {
                if((1LL<<i)&bs)
                {
                    v.push_back(i);
                }
            }

            do
            {
                bool good = true;
                for(int i=0; i<v.size(); i++)
                {
                    int V = v.size();
                    int prev = v[(i-1+5*V)%V];
                    int next = v[(i+1)%V];
                    if(!(bff[v[i]] == prev || bff[v[i]]==next))
                    {
                        /*if(kras==2 && v.size()==3 && v[0]==1 && v[1]==2 && v[2]==3)
                        {
                            cerr << i << " " << bff[i] << " " << prev << " " << next << endl;
                        }*/
                        good = false;
                        break;
                    }
                }
                /*if(kras==2 && v.size()==3 && v[0]==1 && v[1]==2 && v[2]==3)
                        {
                            cerr << good << endl;
                        }*/
                if(good)
                {
                    int V = v.size();
                    ans = max(ans, V);
                }
            }while(next_permutation(v.begin(), v.end()));
        }
        printf("%d\n", ans);
    }
    return 0;
}
