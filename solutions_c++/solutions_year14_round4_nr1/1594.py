#include <string>
#include <cstddef>
#include <vector>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <cassert>
#include <algorithm>

struct noncopyable {
  noncopyable(const noncopyable&) = delete;
  noncopyable& operator=(const noncopyable&) = delete;
  noncopyable() {}
};

struct Files : noncopyable {
  std::fstream in;
  std::fstream out;

  static std::string name_to_out(const std::string& s) {
    if (s.substr(s.size()-3) == ".in") {
      return s.substr(0, s.size()-3)+".out";
    } else {
      return s+".out";
    }
  }

  Files(const std::string& name) : in(name.c_str(), std::ios_base::in),
    out(name_to_out(name).c_str(), std::ios_base::out) {
  }

  size_t get_numline() {
    size_t N;
    in >> N;
    std::string es;
    std::getline(in, es);
    if (!es.empty()) {
      assert(false);
    }
    return N;
  }

  template<class T> std::vector<T> get_vec(size_t n) {
    std::vector<T> v;
    v.reserve(n);
    while (n-- > 0) {
      T tmp;
      in >> tmp;
      v.push_back(std::move(tmp));
    }
    return v;
  }

  template<class T> T get() {
    T tmp;
    in >> tmp;
    return tmp;
  }
};

size_t solve(size_t disc, std::vector<size_t>& files) {
  std::sort(files.begin(), files.end());
  auto b = files.begin();
  auto e = files.end();
  size_t count = 0;
  if (b != e) {
    --e;
    while (b < e) {
      if (*b + *e <= disc) {
	++count;
	++b;
	--e;
      } else if (*b > *e && *b <= disc) {
	++count;
	++b;
      } else if (*e <= disc) {
	++count;
	--e;
      } else {
	assert(false);
      }
    }
    if (b == e) {
      assert(*b <= disc);
      ++count;
    }
    return count;
  } else {
    return 0;
  }
}

size_t solve(size_t disc, std::initializer_list<size_t> files) {
  std::vector<size_t> f(files.begin(), files.end());
  return solve(disc, f);
}

void test() {
  assert(2 == solve(100, {10, 20, 70}));
  assert(2 == solve(100, {30, 40, 60, 70}));
  assert(3 == solve(100, {10, 20, 30, 40, 60}));
}

int main(int argc, char** argv) {
  if (argc < 2) {
    //std::cerr << "Use ./a.out <file>" << std::endl;
    test();
    return 1;
  }

  Files f(argv[1]);
  size_t T;
  f.in >> T;
  for (size_t t = 1; t <= T; ++t) {
    size_t disc, N;
    f.in >> N >> disc;
    auto files = f.get_vec<size_t>(N);
    auto res = solve(disc, files);
    f.out << "Case #" << t << ": " << res << std::endl;
  }
}
