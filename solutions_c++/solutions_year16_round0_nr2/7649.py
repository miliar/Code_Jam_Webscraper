#include <cstdint>
#include <vector>
#include <string>
#include <iostream>
#include <ostream>
#include <alib/textfile.h>
#include <alib/properties.h>

using namespace std;

bool flip(vector<bool>& data) // return true if flipped
{
  bool v = data[0];
  for (auto i = 1; i < data.size(); i++)
  {
    if (data[i] != v)
    {
      for (size_t j = 0; j < i; j++) {
        data[j] = !data[j];
      }
      return true;  // flipped
    }
  }
  return false;
}

uint32_t count_flips(vector<bool>& data)
{
  uint32_t flip_count = 0;
  while (flip(data)) {
    flip_count++;
  }
  if (!data[0]) { // all face down
    flip_count++;
  }
  return flip_count;
}

vector<bool> string_to_data(const string& str)
{
  vector<bool> ret(str.size(), false);
  size_t idx = 0;
  for (auto c : str) {
    if (c == '+') {
      ret[idx] = true;
    }
    idx++;
  }
  return ret;
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
  for (uint32_t i = 1; i <= test_count; i++)
  {
    cout << "Case #" << i << ": " << count_flips(string_to_data(next_line(in))) << endl;
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
