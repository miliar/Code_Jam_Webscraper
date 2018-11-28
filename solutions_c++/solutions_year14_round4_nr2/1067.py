#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <deque>
#include <cstdio>

using namespace std;
#define ll long long

ll srt(deque<ll>& left, deque<ll>& right, deque<ll>& out) {
    int l=0, r=0, o=0;
    ll ans = 0;
    while (l<left.size() && r<right.size()) {
        if (left[l] < right[r]) {
            out[o] = left[l];
            ++o;
            ++l;
        } else {
            out[o] = right[r];
            ans += left.size() - l;
            o++;
            r++;
        }
    }
    for (;l<left.size();++l) {
        out[o++] = left[l];
    }
    for (;r<right.size();++r) {
        out[o++] = right[r];
    }
    return ans;
}

ll insw(deque<ll>& v) {
/*
    ll ans2 = 0;
    for (int i =0;i<v.size();++i) {
        for (int j=i+1;j<v.size();++j) {
            if (v[i] > v[j]) {
                ++ans2;
            }
        }
    }
    */
    if (v.size() <= 1) return 0;
    int p = v.size()/2;
    ll ans = 0;
    deque<ll> left(v.begin(), v.begin()+p);
    deque<ll> right(v.begin()+p, v.end());
    ans += insw(left);
    ans += insw(right);
    ans += srt(left, right, v);
    /*
    if (ans != ans2) {
        printf("Diff: %lld, %lld\n", ans, ans2);
    }
    */
    return ans;
}
ll nsw(deque<ll> v) {
    return insw(v);
}


ll ms2(vector<ll> v, ll infp) {
    deque<ll> left, right;
    for (int i=0;i<infp;++i) {
        left.push_back(v[i]);
    }
    for (int i=infp+1;i<v.size();++i) {
        right.push_back(v[i]);
    }

    deque<ll> rright = deque<ll>(right.rbegin(), right.rend());
    ll ans = nsw(left) + nsw(rright);
    //printf("Orig answer is %lld\n", ans);
    ll as = 0;

    for (int i =0;i<right.size();++i) {
        deque<ll> nl, nr;
        nl = left;
        nl.push_back(right[i]);
        nr = right;
        nr.erase(nr.begin() + i);
        deque<ll> rnr = deque<ll>(nr.rbegin(), nr.rend());
        ll nans = nsw(nl) + nsw(rnr) + as + i + 1;
        //printf("Shifting right %d gives %lld (%lld)\n", i, nans, as);
        if (nans < ans) {
            left = nl;
            right = nr;
            ans = nans;
            as += i + 1;
            --i;
        }
    }
    for (int i =left.size()-1;i>=0;--i) {
        deque<ll> nl, nr;
        nl = left;
        nl.erase(nl.begin() + i);
        nr = right;
        nr.push_front(left[i]);
        deque<ll> rnr = deque<ll>(nr.rbegin(), nr.rend());
        ll nans = nsw(nl) + nsw(rnr) + as + left.size() - i;
        //printf("Shifting left (%d) %d gives %lld (%lld)\n", (int)nl.size(), i, nans, as);
        if (nans < ans) {
            as += left.size() - i;
            left = nl;
            right = nr;
            ans = nans;
        }
    }

    return ans;
}

ll ms(vector<ll> v, ll inflect, int originfpos) {
    ll ans = abs(inflect - originfpos);
    while (originfpos != inflect) {
        if (originfpos > inflect) {
            swap(v[originfpos], v[originfpos-1]);
            originfpos--;
        } else {
            swap(v[originfpos], v[originfpos+1]);
            originfpos++;
        }
    }
    if (true) {
        return ms2(v, inflect) + ans;
    }
    deque<ll> left, right;
    for (int i=0;i<inflect;++i) {
        left.push_back(v[i]);
    }

    for (int i=inflect+1;i<v.size();++i) {
        right.push_back(v[i]);
    }

    ans += nsw(left);
    reverse(right.begin(), right.end());
    ans += nsw(right);
    return ans;
}

int main() {
    ll T;
    cin>>T;
    for (ll t=1;t<=T;++t) {
        ll N;
        cin>>N;
        vector<ll> v;
        for (ll i=0;i<N;++i) {
            ll a;
            cin>>a;
            v.push_back(a);
            //printf("%lld ", a);
        }
        //printf("\n");
        int infpos = 0;
        ll mv = -1000;
        for (int i=0;i<v.size();++i) {
            if (v[i] > mv) {
                infpos = i;
                mv = v[i];
            }
        }
        ll ans = ms2(v, infpos);
        
        /*
        ll ans = ms(v, 0, infpos);
        for (ll i=0;i<v.size();++i) {
            ll cur = ms(v, i, infpos);
            //printf("%d gives %lld\n", i, cur);
            ans = min(ans, cur);
        }*/

        printf("Case #%lld: %lld\n", t, ans);
    }
}
