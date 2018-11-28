#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>  
#include <climits>
#include <map>

using namespace std;

const char kInputFile[] = "input.txt";

string GetLine(ifstream& file) {
  string line;
  getline(file, line);
  return line;
}

string GetOneChar(const string& a, const int index) {
  if (index >= 0 && index < a.size()) {
    return string(&(a.c_str()[index]), 1);
  } else {
    return "";
  }
}

string RepeatString(const string& a, const int times) {
  string result;
  for (int i = 0; i < times; ++i) {
    result += a;
  }
  return result;
}

bool IsPos(const string& a) {
  return a.c_str()[0] != '-';
}

string Revert(const string& a) {
  if (IsPos(a)) {
    return "-" + a;
  } else {
    return string(a.c_str() + 1, 1);
  }
}

string Abs(const string& a) {
  if (IsPos(a)) {
    return a;
  } else {
    return Revert(a);
  }
}

string MultiPos(const string& a, const string& b) {
  if (a == "1" && b == "1") return "1";
  if (a == "1" && b == "i") return "i";
  if (a == "1" && b == "j") return "j";
  if (a == "1" && b == "k") return "k";

  if (a == "i" && b == "1") return "i";
  if (a == "i" && b == "i") return "-1";
  if (a == "i" && b == "j") return "k";
  if (a == "i" && b == "k") return "-j";

  if (a == "j" && b == "1") return "j";
  if (a == "j" && b == "i") return "-k";
  if (a == "j" && b == "j") return "-1";
  if (a == "j" && b == "k") return "i";

  if (a == "k" && b == "1") return "k";
  if (a == "k" && b == "i") return "j";
  if (a == "k" && b == "j") return "-i";
  if (a == "k" && b == "k") return "-1";

  return "";
}

string Multi(const string& a, const string& b) {
  string result_abs = MultiPos(Abs(a), Abs(b));
  if (IsPos(a) && IsPos(b) ||
      !IsPos(a) && !IsPos(b)) {
    return result_abs;
  }
  if (IsPos(a) && !IsPos(b) ||
      !IsPos(a) && IsPos(b)) {
    return Revert(result_abs);
  }
}

vector<string> ToStringList(const string& a) {
  vector<string> result(a.size());
  for (int i = 0; i < a.size(); ++i) {
    result[i] = GetOneChar(a, i);
  }
  return result;
}

// Start from 1.
bool FindIIndex(const string& a_string, int* i_index) {
  vector<string> a_list = ToStringList(a_string);
  *i_index = 0;
  string result = "1";
  while (result != "i" && *i_index < a_list.size()) {
    //cout << result << " " << *i_index << " " << a_list[*i_index] << endl;
    result = Multi(result, a_list[*i_index]);
    //cout << result << endl;
    if (result == "i") {
      *i_index = *i_index + 1;
      return true;
    }
    *i_index = *i_index + 1;
  }
  return false;
}

// Start from 1
bool FindKReverseIndex(const string& a_string, int* k_reverse_index) {
  vector<string> a_list = ToStringList(a_string);
  *k_reverse_index = 0;
  string result = "1";
  //cout << "a_string " << a_string << endl;
  while (result != "k" && *k_reverse_index < a_list.size()) {
    // cout << result << " " << *k_reverse_index << " " << a_list[a_list.size() - *k_reverse_index - 1] << endl;
    result = Multi(a_list[a_list.size() - *k_reverse_index - 1], result);
    // cout << result << endl;
    if (result == "k") {
      *k_reverse_index = *k_reverse_index + 1;
      return true;
    }
    *k_reverse_index = *k_reverse_index + 1;
  }
  return false;
}

string GetLeftOver(const int i_index,
		   const int k_reverse_index,
		   const int l,
		   const int x,
		   const string line) {
  const int pre_x = i_index / l;
  const int left_over_i_index = i_index % l;

  const int suf_x = k_reverse_index / l;
  const int left_over_k_reverse_index = k_reverse_index % l;

  // cout << i_index << " " << k_reverse_index << endl; 
  // cout << pre_x << " " << suf_x << " " << x << endl;
  if (x - pre_x - suf_x <= 1) {
    // cout << left_over_i_index << " " << left_over_k_reverse_index << endl;
    return string(line.c_str() + left_over_i_index,
		  l - left_over_i_index - left_over_k_reverse_index);
  }

  const string prefix = string(line.c_str() + left_over_i_index,
				l - left_over_i_index);
  const string suffix = string(line.c_str(), l - left_over_k_reverse_index);
  const string middle = RepeatString(line, (x - pre_x - suf_x - 2) % 4);
  // cout << prefix << " " << middle << " " << suffix << endl;
  return prefix + middle + suffix;
}

string Evaluate(const string& a) {
  if (a.size() == 0) return "";
  vector<string> a_list = ToStringList(a);
  string result = a_list[0];
  for (int i = 1; i < a_list.size(); ++i) {
    result = Multi(result, a_list[i]);
  }
  return result;
}

bool Solve(const int l, const int x, string line) {
  const string repeated_string = RepeatString(line, 4);
  int i_index;
  int k_reverse_index;
  if (!FindIIndex(repeated_string, &i_index) ||
      !FindKReverseIndex(repeated_string, &k_reverse_index)) {
    return false;
  }
  // cout << " ford " << i_index << " " << k_reverse_index << " " << l << " " << x << endl;
  if (i_index + k_reverse_index >= l * x) return false;
  
  const string left_over = GetLeftOver(i_index, k_reverse_index, l, x, line);
  // cout << i_index << " " << k_reverse_index << " " << left_over;
  return Evaluate(left_over) == "j";
}

int main() {
  ifstream infile(kInputFile);
  int total_test_cases = stoi(GetLine(infile));

  for (int num_test_cases = 0; num_test_cases < total_test_cases;
       ++num_test_cases) {
    int l = 0;
    int x = 0;
    {
      stringstream ss(GetLine(infile));
      ss >> l;
      ss >> x;
    }

    string line = GetLine(infile);

    bool result = Solve(l, x, line);
    cout << "Case #" << num_test_cases + 1 << ": " << (result ? "YES" : "NO")
	 << endl;
  }

  infile.close();
  return 0;
}
