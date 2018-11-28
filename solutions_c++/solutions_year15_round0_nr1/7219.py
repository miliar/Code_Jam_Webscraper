#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

int main()  {
    //freopen("A-large.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    string str;
    int _smax, _test, _li, _lj, _lk, _no, _nof, _noa;
    cin >> _test;
    for( _li = 0; _li < _test; _li++ )   {
        _nof = _noa = 0;
        cin >> _smax;
        cin >> str;
        for( _lj = 0; _lj <= _smax; _lj++ )   {
            _no = str[_lj] - 48;
            if( _no == 0 ) continue;
            else if( _lj <= _noa ) {
                _noa += _no;
            }else    {
                _nof += (_lj-_noa);
                _noa += _no+(_lj-_noa);
            }
        }
        cout << "Case #" << _li+1 << ": " << _nof << endl;
    }



    return 0;
}
