#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
typedef long long ll;typedef unsigned long long ull;
template <typename T>struct iindex {T data;iindex() = default;iindex(long long i) : data(i) {}iindex(int       i) : data(i) {}iindex(size_t    i) : data(i) {}operator T &       () { return data; }/* operator long long () { return data; } *//* operator int       () { return data; } *//* operator size_t    () { return data; } */typedef T value_type;};template <typename T>std::istream & operator >> (std::istream & input, iindex<T> & i) { input >> i.data; i.data -= 1; return input; }template <typename T>std::ostream & operator << (std::ostream & output, iindex<T> const & i) { return output << i.data+1; }typedef iindex<long long> index;
template <typename T>std::istream & operator >> (std::istream & input, std::vector<T> & a) {for (int i = 0; i < a.size(); ++i) {input >> a[i];}return input;}template <typename T>std::ostream & operator << (std::ostream & output, const std::vector<T> & a) {for (int i = 0; i < a.size(); ++i) {if (i != 0) output << ' ';output << a[i];}return output;}
template <typename T>class irange {public:class iterator {public:iterator(T value) : value(value), step(1) {}iterator(T value, T step) : value(value), step(step) {}bool operator != (const iterator & other) const {return value != other.value;}T const & operator * () const {return value;}iterator & operator ++ () {value += step;return *this;}private:T value;T step;};public:irange(T last) : first(0), last(last), step(1) {}irange(T first, T last) : first(first), last(last), step(1) {}irange(T first, T last, T step) : first(first), last(last), step(step) {}iterator begin() const {return iterator(first, step);}iterator end() const {if (step == 0) return iterator(last, step);if (0 < step and last < first) return iterator(first, step);if (step < 0 and first < last) return iterator(first, step);return iterator(first + ((last - first + (0 < step ? -1 : 1)) / step + 1) * step, step);}typedef T value_type;private:T const first;T const last;T const step;};typedef irange<long long> lrange;inline lrange range(lrange::value_type last) { return lrange(last); }inline lrange range(lrange::value_type first, lrange::value_type last) { return lrange(first, last); }inline lrange range(lrange::value_type first, lrange::value_type last, lrange::value_type step) { return lrange(first, last, step); }template <typename T> lrange index_of(const T & a) { return range(a.size()); }inline lrange range(std::istream & input) { lrange::value_type i; input >> i; return range(i); }inline lrange reverse_range(lrange::value_type last) { return range(last-1,-1,-1); }inline lrange reverse_range(lrange::value_type first, lrange::value_type last) { return range(last-1,first-1,-1); }inline lrange inclusive_range(lrange::value_type last) { return range(last+1); }inline lrange inclusive_range(lrange::value_type first, lrange::value_type last) { return range(first,last+1); }template <typename T> lrange reverse_index_of(const T & a) { return range(a.size()-1,-1,-1); }
using namespace std;
enum UQ {
    Q1, QI, QJ, QK,
};
struct Q {
    bool sign;
    UQ quot;
};
Q plusq(UQ q) {
    return (Q) { false, q };
}
Q minusq(UQ q) {
    return (Q) { true, q };
}
UQ ctouq(char c) {
    if (c == '1') return Q1;
    if (c == 'i') return QI;
    if (c == 'j') return QJ;
    if (c == 'k') return QK;
    return Q1;
}
Q ctoq(char c) {
    return plusq(ctouq(c));
}
Q operator - (Q const & a) {
    return a.quot == Q1 ? a : (Q) { not a.sign, a.quot };
}
bool operator == (Q const & a, Q const & b) {
    return a.sign == b.sign and a.quot == b.quot;
}
bool operator != (Q const & a, Q const & b) {
    return not (a == b);
}
Q operator + (Q const & a, Q const & b) {
    static const bool s[4][4] = {
        // * 1 i j k
        { false, false, false, false }, // 1 *
        { false,  true, false,  true }, // i *
        { false,  true,  true, false }, // j *
        { false, false,  true,  true }, // k *
    };
    static const UQ t[4][4] = {
        // * 1 i j k
        { Q1, QI, QJ, QK }, // 1 *
        { QI, Q1, QK, QJ }, // i *
        { QJ, QK, Q1, QI }, // j *
        { QK, QJ, QI, Q1 }, // k *
    };
    return (Q) { (a.sign != b.sign) != s[a.quot][b.quot], t[a.quot][b.quot] };
}
Q operator * (int a, Q const & b) {
    if (a < 0) return - ((-a) * b);
    if (a == 0) return plusq(Q1);
    // Q result = plusq(Q1);
    // for (int i : range(a)) result = result + b;
    int n = 1; while (2*n <= a) n *= 2;
    vector<Q> acc(n);
    acc[0] = b; for (int i : range(1,n)) acc[i] = acc[i-1] + acc[i-1];
    Q result = plusq(Q1);
    for (int i : range(n)) {
        if (a & (1 << i)) {
            result = result + acc[i];
        }
    }
    return result;
}
int nto1(Q const & a) {
    static int table[2][4] = {
        // 1 i j k
        { 1, 4, 4, 4 }, // +
        { 2, 4, 4, 4 }, // -
    };
    return table[a.sign][a.quot];
}
bool solve(ll l, ll x, string const & s) {
    vector<Q> acc(s.size()+1);
    acc[0] = plusq(Q1); for (int i : index_of(s)) acc[i+1] = acc[i] + ctoq(s[i]);
    Q total = x * acc[l];
    for (int ia : range(nto1(acc[l]))) for (int ib : range(l)) {
        if (not (ia < x)) continue;
        Q iq = ia * acc[l] + acc[ib];
        if (iq != plusq(QI)) continue;
        for (int ka : range(nto1(acc[l]))) for (int kb : range(l)) {
            if (not (ia + (ib + kb)/l + ka < x)) continue;
            Q kq = ((- acc[l-kb-1]) + acc[l]) + ka * acc[l];
            if (kq != plusq(QK)) continue;
            if ((- iq) + total + (- kq) == plusq(QJ)) return true;
        }
    }
    return false;
}
int main() {
    ios_base::sync_with_stdio(false);
    for (int testcase : range(cin)) {
        ll l, x; string s; cin >> l >> x >> s;
        cout << "Case #" << testcase+1 << ": " << (solve(l,x,s) ? "YES" : "NO") << endl;
    }
    return 0;
}
