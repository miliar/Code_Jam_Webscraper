#include "Bleatrix.hh"

Bleatrix::Bleatrix(int n, int id) {
    _id = id;
    _n = n;
    _i = 1;
    for (int i = 0; i < 10; i++)
        _list.push_front(i);
}

Bleatrix::~Bleatrix() {}

void            Bleatrix::startCounting() {
    if (_n == 0)
        return;

    while (!_list.empty()) {
        breakNumber();
        _i++;
    }
    _i--;
}

void            Bleatrix::writeResult() {
    if (_n == 0)
        std::cout << "Case #" << _id << ": INSOMNIA" << std::endl;
    else
        std::cout << "Case #" << _id << ": " << (long)_i * (long)_n << std::endl;
}

void            Bleatrix::breakNumber() {
    long        n;

    n = _i * _n;
    while (n != 0) {
        _list.remove(n % 10);
        n =  n / 10;
    }
}
