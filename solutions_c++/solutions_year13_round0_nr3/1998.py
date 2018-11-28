#include <cstdio>
#include <set>

static unsigned long long int s_aPalindromes[] = {
  1,             4,             9,           121,           484, 
  10201,         12321,         14641,         40804,         44944, 
  1002001,       1234321,       4008004,     100020001,     102030201, 
  104060401,     121242121,     123454321,     125686521,     400080004, 
  404090404,   10000200001,   10221412201,   12102420121,   12345654321, 
  40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 
  1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 
  1232346432321, 1234567654321, 4000008000004, 4004009004004
};

static unsigned long long int _read_number(void) {
  unsigned long long int _n = 0;
  int                    _c;

  while(((_c = getchar()) >= '0') &&
        (_c <= '9'))
    _n = _n * 10 + (_c - '0');

  return _n;
}

int main(int _argc, char *_argv[]) {
  int                              _t = (int)_read_number();
  std::set<unsigned long long int> _palindromes;
  unsigned long long int           _min, _max;
  int                              _c;

  for(unsigned int _i(0); _i < (sizeof(s_aPalindromes) / sizeof(unsigned long long int)); ++_i)
    _palindromes.insert(s_aPalindromes[_i]);

  for(int _i(0); _i < _t; ++_i) {
    _min = _read_number();
    _max = _read_number();
    _c   = 0;

    for(std::set<unsigned long long int>::iterator _it(_palindromes.lower_bound(_min));
        _it != _palindromes.upper_bound(_max); ++_it)
      ++_c;

    fprintf(stdout, "Case #%d: %d\n", _i + 1, _c);
  }

  return 0;
}
