#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
typedef long long ll;typedef unsigned long long ull;
template <typename T>struct iindex {T data;iindex() = default;iindex(long long i) : data(i) {}iindex(int       i) : data(i) {}iindex(size_t    i) : data(i) {}operator T &       () { return data; }/* operator long long () { return data; } *//* operator int       () { return data; } *//* operator size_t    () { return data; } */typedef T value_type;};template <typename T>std::istream & operator >> (std::istream & input, iindex<T> & i) { input >> i.data; i.data -= 1; return input; }template <typename T>std::ostream & operator << (std::ostream & output, iindex<T> const & i) { return output << i.data+1; }typedef iindex<long long> index;
template <typename T>class irange {public:class iterator {public:iterator(T value) : value(value), step(1) {}iterator(T value, T step) : value(value), step(step) {}bool operator != (const iterator & other) const {return value != other.value;}T const & operator * () const {return value;}iterator & operator ++ () {value += step;return *this;}private:T value;T step;};public:irange(T last) : first(0), last(last), step(1) {}irange(T first, T last) : first(first), last(last), step(1) {}irange(T first, T last, T step) : first(first), last(last), step(step) {}iterator begin() const {return iterator(first, step);}iterator end() const {if (step == 0) return iterator(last, step);if (0 < step and last < first) return iterator(first, step);if (step < 0 and first < last) return iterator(first, step);return iterator(first + ((last - first + (0 < step ? -1 : 1)) / step + 1) * step, step);}typedef T value_type;private:T const first;T const last;T const step;};typedef irange<long long> lrange;inline lrange range(lrange::value_type last) { return lrange(last); }inline lrange range(lrange::value_type first, lrange::value_type last) { return lrange(first, last); }inline lrange range(lrange::value_type first, lrange::value_type last, lrange::value_type step) { return lrange(first, last, step); }template <typename T> lrange index_of(const T & a) { return range(a.size()); }inline lrange range(std::istream & input) { lrange::value_type i; input >> i; return range(i); }inline lrange reverse_range(lrange::value_type last) { return range(last-1,-1,-1); }inline lrange reverse_range(lrange::value_type first, lrange::value_type last) { return range(last-1,first-1,-1); }inline lrange inclusive_range(lrange::value_type last) { return range(last+1); }inline lrange inclusive_range(lrange::value_type first, lrange::value_type last) { return range(first,last+1); }template <typename T> lrange reverse_index_of(const T & a) { return range(a.size()-1,-1,-1); }
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    for (int testcase : range(cin)) {
        int smax; string s; cin >> smax >> s;
        int acc = 0;
        int friends = 0;
        for (int i : index_of(s)) {
            int sn = s[i] - '0';
            if (sn and acc < i) {
                friends += i - acc;
                acc = i;
            }
            acc += sn;
        }
        cout << "Case #" << testcase+1 << ": " << friends << endl;
    }
    return 0;
}
