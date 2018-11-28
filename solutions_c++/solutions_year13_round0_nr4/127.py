#include<iostream>
#include<vector>
#include<map>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

VI key;
VI TKey;
VVI KKey;

VI ans;

typedef vector<bool> VB;

VB flag;

typedef map<int,bool> MIB;

MIB m;

int cur;

#define dbg(x) cerr<< #x << " = " << x << " "

bool rec(int i)
{
    if ( m.count(cur)>0) return m[cur];
    if ( i==TKey.size())
    {
        return true;
    }

    for (int j=0;j<TKey.size();++j)
    {
        if ( flag[j]) continue;

        if ( key[TKey[j]]>0)
        {
            flag[j]=true;
            key[TKey[j]]--;
            for (int k=0;k<KKey[j].size();++k)
            {
                key[KKey[j][k]]++;
            }
            ans.push_back(j+1);
            cur |= (1ul<<j);
            if ( rec(i+1))
                return true;
            cur ^= (1ul<<j);
            ans.pop_back();
            flag[j]=false;
            key[TKey[j]]++;
            for (int k=0;k<KKey[j].size();++k)
            {
                key[KKey[j][k]]--;
            }
        }
    }

    m[cur]=false;
    return false;
}

void print(int t, bool is_ok)
{
    cout << "Case #" << t << ": ";
    if (is_ok)
    {
        for (int i=0;i<ans.size();++i)
        {
            cout << ans[i] << " ";
        }
        cout << endl;
        return;
    }
        
    cout << "IMPOSSIBLE" << endl;

}

#if 0
bool simple_check()
{
    VB f(TKey.size(),false);
    VI kk = key;
    for (int i=0;i<TKey.size();++i)
    {
        for (int j=0;j<TKey.size();++j)
        {
            if ( kk[TKey[j]]==0)
                continue;
            
            if ( f[j]) continue;

            f[j] = true;
            for (int k=0;k<KKey[j].size();++k)
            {
                kk[KKey[j][k]]++;
            }
        }
    }

    for (int i=0;i<TKey.size();++i)
    {
        if ( !f[i])
            return false;
    }
    return true;
}
#endif

int main()
{
    int T;
    cin >> T;
    for (int t=0;t<T;++t)
    {
        int K, N;
        cin >> K >> N;
        key.assign(201,0);
        TKey.clear();
        KKey.clear();
        for (int i=0;i<K;++i)
        {
            int x;
            cin >> x;
            key[x]++;
        }

        for (int i=0;i<N;++i)
        {
            int Ti, Ki;
            cin >> Ti >> Ki;
            TKey.push_back(Ti);
            KKey.push_back(VI());

            for (int j=0;j<Ki;++j)
            {
                int x;
                cin >> x;
                KKey[i].push_back(x);
            }
        }
        ans.clear();
        flag.assign(N,false);
        cur=0;
        
#if 0
        if ( !simple_check())
        {
            print(t+1,false);
            continue;
        }
#endif
        m.clear();
        print(t+1, rec(0));
    }
}
