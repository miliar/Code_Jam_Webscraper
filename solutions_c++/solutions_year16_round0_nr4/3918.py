#ifndef matrix_h
#define matrix_h

#include <iostream>
#include <iomanip>
#include <valarray>
#include <cassert>
#include <initializer_list>

using namespace std;

// А-ля Страуструп: http://www.stroustrup.com/matrix.c
template<typename T> class slice_iter {
    typedef valarray<T> VT;
    VT& v;
    slice s;
    T& ref(size_t i) const { return (v)[s.start() + i * s.stride()]; }
public:
    slice_iter( VT& v, slice s ) : v(v), s(s) {}
    
    // Заменитель конструктора для константных экземпляров. Обычный конструктор "возвратил бы" не const итератор.
    static const slice_iter ct(const VT& v, slice s) { return slice_iter( const_cast<VT&>(v), s ); }
    
    size_t size() const { return s.size(); }
    const T& operator[](size_t i) const { return ref(i); }
    T& operator[](size_t i) { return ref(i); }
    
    // Перемножение соотв. элементов со сложением результатов.
    T operator*(const slice_iter& si) const {
        assert(size() == si.size());
        T res = 0;
        for( size_t i = 0, s = size(); i < s; i++ ) {
            res += ref(i) * si[i];
        }
        return res;
    }
};

template <typename T>
class matrix {
    valarray<T> _m;
    size_t _w;
    size_t _h;
public:
    using vector = slice_iter<T>;
    
    matrix(size_t w, size_t h) : _w(w), _h(h), _m(w * h) {}
    
    matrix(initializer_list<initializer_list<T>> l) {
        _h = l.size();
        _w = _h > 0 ? l.begin()->size() : 0;
        _m.resize( _w * _h );
        size_t pos = 0;
        for( initializer_list<T> const& rowList : l ) {
            assert(rowList.size() == _w);
            for( const T& value : rowList) {
                _m[pos] = value;
                pos++;
            }
        }
    }
    
    size_t w() const { return _w; }
    size_t h() const { return _h; }
    
    T& operator () (size_t x, size_t y) { return _m[ _w * y + x ]; }
    
    vector col(size_t x) { return vector( _m, slice(x, _h, _w) ); }
    const vector col(size_t x) const { return vector::ct( _m, slice(x, _h, _w) ); }
    
    vector row(size_t y) { return vector( _m, slice( y * _w, _w, 1) ); }
    const vector row(size_t y) const { return vector::ct( _m, slice( y * _w, _w, 1) ); }
    
    vector operator[] (size_t y) { return row(y); }
    const vector operator[] (size_t y) const { return row(y); }
    
    matrix transpond() const {
        auto m = matrix(_h, _w);
        for ( int i = 0; i < _h; i++ ) {
            int j = 0; j < _w; j++;
            m(j, i) = *this(i, j);
        }
        return m;
    }
    
    matrix operator*( const matrix& m ) const {
        assert( m.h() == _w );
        auto res = matrix(m.w(), _h);
        for( size_t y = 0, h = res.h(); y < h; y++ ) {
            for( size_t x = 0, w = res.w(); x < w; x++ ) {
                res(x, y) = row(y) * m.col(x);
            }
        }
        return res;
    }
};

template <typename T>
std::ostream& operator << (std::ostream& os, const matrix<T>& m) {
    using namespace std;
    for (size_t y = 0, nY = m.h(); y  < nY; y++) {
        for (size_t x = 0, nX = m.w(); x < nX; x++) {
            cout << setw(4) << m[y][x] << ", ";
        }
        cout << endl;
    }
    cout << "\n\n";
    return os;
}

inline void testMatrix() {
    
    auto m0 = matrix<int> {};
    cout << m0;
    
    auto m1 = matrix<int> {
        {1, 2, 3},
        {2, 2, 3}
    };
    cout << m1;
    
    auto m2 = matrix<int> {
        {2, 3},
        {3, 3},
        {4, 4}
    };
    cout << m2;
    
    cout << m1 * m2;
    cout << m2 * m1;
}

#endif /* matrix_h */
