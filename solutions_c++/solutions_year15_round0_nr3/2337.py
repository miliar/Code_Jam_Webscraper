#include <cstdio>
#include <vector>
#include <utility>
#include <set>
#include <map>

#define dprintf if(0)printf 

using namespace std;

typedef pair<int, bool> Quat;

const Quat I('i', 0);
const Quat J('j', 0);
const Quat K('k', 0);
const Quat O('1', 0);

const Quat mI('i', 1);
const Quat mJ('j', 1);
const Quat mK('k', 1);
const Quat mO('1', 1);

typedef pair<Quat, Quat> QMI;

Quat pref[10100];

map<QMI, Quat> mRes = {{QMI(O, O), O}, {QMI(O, I), I}, {QMI(O, J), J}, {QMI(O, K), K}, {QMI(O, mO), mO}, {QMI(O, mI), mI}, {QMI(O, mJ), mJ}, {QMI(O, mK), mK},
                       {QMI(I, O), I}, {QMI(I, I), mO}, {QMI(I, J), K}, {QMI(I, K), mJ}, {QMI(I, mO), mI}, {QMI(I, mI), O}, {QMI(I, mJ), mK}, {QMI(I, mK), J},
                       {QMI(J, O), J}, {QMI(J, I), mK}, {QMI(J, J), mO}, {QMI(J, K), I}, {QMI(J, mO), mJ}, {QMI(J, mI), K}, {QMI(J, mJ), O}, {QMI(J, mK), mI},
                       {QMI(K, O), K}, {QMI(K, I), J}, {QMI(K, J), mI}, {QMI(K, K), mO}, {QMI(K, mO), mK}, {QMI(K, mI), mJ}, {QMI(K, mJ), I}, {QMI(K, mK), O},
                       {QMI(mO, O), mO}, {QMI(mO, I), mI}, {QMI(mO, J), mJ}, {QMI(mO, K), mK}, {QMI(mO, mO), O}, {QMI(mO, mI), I}, {QMI(mO, mJ), J}, {QMI(mO, mK), K},
                       {QMI(mI, O), mI}, {QMI(mI, I), O}, {QMI(mI, J), mK}, {QMI(mI, K), J}, {QMI(mI, mO), I}, {QMI(mI, mI), mO}, {QMI(mI, mJ), K}, {QMI(mI, mK), mJ},
                       {QMI(mJ, O), mJ}, {QMI(mJ, I), K}, {QMI(mJ, J), O}, {QMI(mJ, K), mI}, {QMI(mJ, mO), J}, {QMI(mJ, mI), mK}, {QMI(mJ, mJ), mO}, {QMI(mJ, mK), I},
                       {QMI(mK, O), mK}, {QMI(mK, I), mJ}, {QMI(mK, J), I}, {QMI(mK, K), O}, {QMI(mK, mO), K}, {QMI(mK, mI), J}, {QMI(mK, mJ), mI}, {QMI(mK, mK), mO},
                      };

void print(const Quat& x){
    printf("%s%c",x.second ? "-": "" , x.first);
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;++i)
    {
        long long q, len;
        scanf("%lld %lld",&len, &q);
        char s[len+2];
        scanf("%s",s);
        pref[0] = Quat(s[0],0); 
        for(int j=1;j<len;++j)
        {
            pref[j] = mRes[QMI(pref[j-1], Quat(s[j], 0) )];
        }
        set<Quat> vis;
        vector<Quat> pow;
        pow.push_back(pref[len-1]);
        vis.insert(pref[len-1]);
        int k = 1;
        while (k<q)
        {
            auto nod = mRes[QMI(pow.back(), pref[len-1])];
            if (vis.find(nod) != vis.end()) break;
            vis.insert(nod);
            pow.push_back(nod);
            ++k;
        }

        int w = -1;
        auto pM = O;
        auto lFor = I;
        long long idx = 0;
        bool suc = false;

        if (pow[(q-1)%pow.size()] == mO)

        while (w < (int)pow.size() && !suc)
        {
            for(int j=0; !suc && j<len;++j)
            {
                auto el = mRes[QMI(pM, pref[j])];
                if (el == lFor)
                {
                    if (el == I) lFor = K;
                    else
                    { 
                        idx = (w+1)*len + j + 1;
                        suc = true;
                    }
                }
            }
            ++w;
            pM = w < pow.size() ? pow[w] : O;
        }
        printf("Case #%d: %s\n", i, suc ? "YES" : "NO");
    }
    return 0;
}
