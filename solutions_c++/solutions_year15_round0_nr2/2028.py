#include <iostream>
#include <vector>
#include <list>
#include <cassert>
#include <algorithm>

using namespace std;

/*unsigned optimalk(unsigned p, unsigned n){
    unsigned tmin = p;
    unsigned kmin = 1;
    for(unsigned k=1; k<p; ++k){
        if((p+k-1)/k+n*(k-1) < tmin){
            kmin = k;
            tmin = (p+k-1)/k+n*(k-1);
        }
    }
    return kmin;
}*/

struct pancs{
    unsigned p, n, k, t;
};

bool operator<(const pancs& p1, const pancs& p2){
    return p1.t < p2.t;
}

bool pancsgt(const pancs& p1, const pancs& p2){
    return p1.t > p2.t;
}

int main(){
    unsigned t;
    cin >> t;
    for(unsigned tc = 1; tc <= t; ++tc){
        unsigned d;
        cin >> d;
        vector<unsigned> pl(d);
        for(unsigned i = 0; i < d; ++i)
            cin >> pl[i];
        sort(pl.begin(), pl.end());
        list<pancs> pv;
        unsigned i = 0;
        while(i < d){
            unsigned j;
            for(j = i; j < d && pl[j] == pl[i]; j++);
            pancs tmpp;
            tmpp.p = pl[i];
            tmpp.n = j-i;
            tmpp.k = 1;
            tmpp.t = tmpp.p;
            pv.push_back(tmpp);
            i = j;
        }
        //unsigned N = pv.size();
        unsigned nkmin1sum = 0;
        pv.sort(pancsgt);
        unsigned tmin = pv.front().t;
        unsigned noprog = 0;
        while(true){
            unsigned nextmax = (pv.front().p+pv.front().k)/(pv.front().k+1);
            list<pancs>::iterator second = pv.begin();
            ++second;
            if(pv.size() > 1)
                nextmax = max(nextmax, second->t);
            nkmin1sum += pv.front().n;
            pv.front().k++;
            if(pv.front().t - nextmax >= pv.front().n){
                tmin = min(tmin, nextmax + nkmin1sum);
                noprog = 0;
            }
            else{
                noprog++;
                if(noprog == pv.size())
                    break;
            }
            pv.front().t = (pv.front().p+pv.front().k-1)/pv.front().k;
            //sort it again
            list<pancs>::iterator i = second;
            while(i->t > pv.front().t)
                ++i;
            pv.insert(i, pv.front());
            pv.erase(pv.begin());
        }

        /*for(unsigned i = 0; i < pv.size(); ++i){
            cout << "(p=" << pv[i].p << ", n=" << pv[i].n << ", k=" << pv[i].k << ", t=" << pv[i].t << ") ";
        }*/

        cout << "Case #" << tc << ": " << tmin << endl;


        /*for(unsigned i = 0; i < N; ++i){
            if(i == maxi)
                continue;
            while(true){
                unsigned knext = ki[i]-1;
                if(knext == 0)
                    break;
                unsigned tnext = (pi[i]+knext-1)/knext;
                if(tnext > maxt)
                    break;
                ki[i] = knext;
                ti[i] = tnext;
                nkmin1sum -= ni[i];
            }
        }*/

        /*cout << "DEBUG: ki: ";
        for(unsigned i = 0; i < N; ++i)
            cout << ki[i] << " ";
        cout << endl << "ti: ";
        for(unsigned i = 0; i < N; ++i)
            cout << ti[i] << " ";
        cout << endl;
        cout << maxt << " " << nkmin1sum << endl;*/
        //cout << "Case #" << tc << ": " << maxt+nkmin1sum << endl;
    }
    return 0;
}
