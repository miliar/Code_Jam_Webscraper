#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

#define ll long long int
#define MOD 1000002013ll

using namespace std;

typedef pair<ll,ll> ii;

ll T, C=1, n, m;
ll custo[128];
vector<ll> entra[128];
vector<ii> trem;

int main() {
    for(scanf("%lld",&T);T--;) {
        printf("Case #%lld: ",C++);
        scanf("%lld %lld",&n,&m);

        custo[0] = 0;
        for (ll i=1;i<=n;i++)
            custo[i] = (custo[i-1] + (n-i+1))%MOD;


        ll correto = 0;
        for (ll i=0;i<n;i++) entra[i].clear();
        for (ll i=0;i<m;i++) {
            ll a, b, w;
            scanf("%lld %lld %lld",&a,&b,&w); a--; b--;
            for (ll j=0;j<w;j++) {
                entra[a].push_back(b);
                correto = (correto + custo[b-a])%MOD;
            }
        }
        ll soma = 0;
        trem.clear();
        for (ll i=0;i<n;i++) {
            // pra cada estacao
            // entra td mnd
            for (ll j=0;j<(ll)entra[i].size();j++)
                trem.push_back(ii(i, entra[i][j]));
            // pra cada cara que sai do trem nessa estacao
            vector<ii> ntrem;
            vector<ii> saindo;
            for (ll j=0;j<(ll)trem.size();j++) if (trem[j].second == i) {
                saindo.push_back(trem[j]);
            } else ntrem.push_back(trem[j]);

            int k = (int)saindo.size();
            vector<int> todos;
            for (ll j=0;j<(ll)ntrem.size();j++)
                todos.push_back(ntrem[j].first);
            for (ll j=0;j<(ll)saindo.size();j++)
                todos.push_back(saindo[j].first);
            sort(todos.begin(),todos.end());

            for (ll j=0;j<(int)todos.size();j++) {
                ll i1 = (int)todos.size()-j-1;
                if (j < k) saindo[j].first = todos[i1];
                else ntrem[j-k].first = todos[i1];
            }

            for (ll j=0;j<k;j++)
                soma = (soma + custo[ i-saindo[j].first ])%MOD;

            trem = ntrem;
        }
        printf("%lld\n",(correto-soma+MOD)%MOD);
    }

    return 0;
}
