#include <cstdint>
#include <vector>
#include <string>
#include <iostream>
#include <ostream>
#include <alib/textfile.h>
#include <alib/properties.h>

using namespace std;

class counter_t
{
public:

  counter_t() : data_(10, false) {
  }

  void add(uint32_t);
  uint32_t count() const;

private:
  vector<bool> data_;
};

void counter_t::add(uint32_t x)
{
  auto str = to_string(x);
  for (auto c : str) {
    data_[c - '0'] = true;
  }
}

uint32_t counter_t::count() const
{
  uint32_t ret = 0;
  for (auto d : data_) {
    if (d) {
      ret++;
    }
  }
  return ret;
}

string calculate(uint32_t x)
{
  counter_t counter;

  for (uint32_t mult = 1; mult < 100; mult++)
  {
    uint32_t curval = x * mult;
    counter.add(curval);
    if (counter.count() == 10) {
      return to_string(curval);
    }
  }
  return "INSOMNIA";
}

string next_line(alib::textfile_t& in)
{
  if (!in.more()) {
    throw exception("missing line");
  }
  return string(in.gets());
}

void run(alib::textfile_t& in)
{
  uint32_t test_count = stoul(next_line(in));
  for (uint32_t i = 1; i <= test_count; i++) {
    cout << "Case #" << i << ": " << calculate(stoul(next_line(in))) << endl;
  }
}

int main(int argc, const char *argv[])
{
  alib::cmdline_t cmd(argc, argv);
  try {
    run(
      alib::textfile_t(cmd.getString("IN"))
    );
  }
  catch (const exception& e) {
    cout << "error" << e.what();
  }
}
