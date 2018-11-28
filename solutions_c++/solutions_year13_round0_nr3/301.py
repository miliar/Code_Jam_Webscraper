#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


using namespace std;
const int MAXHALF = 25;
char digits[] = "0123456789";


string square(const string& num)
{
  int numSz = num.length();
  string::size_type maxlen = 0;
  vector<string> sums;
  for (int i = 0; i < numSz; i++) {
    int carry = 0;
    string sum;
    for (int j = 0; j < numSz; j++) {
      int sub = (num[numSz-i-1]-'0')*(num[numSz-j-1]-'0') + carry;
      sum.push_back(digits[sub%10]);
      carry = sub/10;
    }

    if (carry) {
      sum.push_back(digits[carry]);
    }

    for (int j = 0; j < i; j++) {
      sum.push_back('0');
    }

    rotate(sum.begin(), sum.begin()+(sum.length()-i), sum.end());
    sums.push_back(sum);
    maxlen = max(maxlen, sum.length());
  }

  int carry = 0;
  string result;
  for (string::size_type col = 0; col < maxlen; col++) {
    int sub = carry;
    for (int row = 0; row < numSz; row++) {
      sub += (col < sums[row].length() ? sums[row][col]-'0' : 0);
    }

    carry = sub/10;
    result.push_back(digits[sub%10]);
  }

  if (carry) {
    result.push_back(digits[carry]);
  }

  reverse(result.begin(), result.end());
  return result;
}


bool compare(const string& lhs, const string& rhs)
{
  if (lhs.length() == rhs.length()) {
    return (lhs < rhs);
  }

  return (lhs.length() < rhs.length());
}


int main(void)
{
  // generate all possible fair and square numbers
  // the square root follow the following rule:
  // sum of each digit^2 is less than 10
  vector<string> numbers;
  // 1 x '1'
  numbers.push_back("1");
  // 2 x '1'  ('1' only appears at head or tail)
  vector<pair<string, string> > two_one;
  for (int i = 1; i <= MAXHALF; i++) {
    string left(i, '0');
    left[0] = '1';
    string right = left;
    reverse(right.begin(), right.end());
    two_one.push_back(pair<string, string>(left, right));
  }
  for (vector<pair<string, string> >::const_iterator it
         = two_one.begin(); it != two_one.end(); ++it) {
    numbers.push_back(it->first+"0"+it->second);  // odd length
    numbers.push_back(it->first+it->second);  // even length
  }
  // 3 x '1'  (length must be odd, middle is '1')
  for (vector<pair<string, string> >::const_iterator it
         = two_one.begin(); it != two_one.end(); ++it) {
    numbers.push_back(it->first+"1"+it->second);  // odd length
  }
  // 1 x '2'  (2^2 = 4 <= 10)
  numbers.push_back("2");
  // 4 x '1'
  vector<pair<string, string> > four_one;
  for (int i = 2; i <= MAXHALF; i++) {
    string half(i, '0');
    half[0] = '1';
    for (int j = 1; j < i; j++) {
      string left = half;
      left[j] = '1';
      string right = left;
      reverse(right.begin(), right.end());
      four_one.push_back(pair<string, string>(left, right));
    }
  }
  for (vector<pair<string, string> >::const_iterator it
         = four_one.begin(); it != four_one.end(); ++it) {
    numbers.push_back(it->first+"0"+it->second);  // odd length
    numbers.push_back(it->first+it->second);  // even length
  }
  // 1 x '2' with 1 x '1'  (IMPOSSIBLE)
  // 5 x '1'  (length must be odd, middle is '1')
  for (vector<pair<string, string> >::const_iterator it
         = four_one.begin(); it != four_one.end(); ++it) {
    numbers.push_back(it->first+"1"+it->second);  // odd length
  }
  // 1 x '2' with 2 x '1'  (length must be odd, middle is '2')
  for (vector<pair<string, string> >::const_iterator it
         = two_one.begin(); it != two_one.end(); ++it) {
    numbers.push_back(it->first+"2"+it->second);  // odd length
  }
  // 6 x '1'
  vector<pair<string, string> > six_one;
  for (int i = 3; i <= MAXHALF; i++) {
    string half(i-1, '0');
    half[i-2] = half[i-3] = '1';
    do {
      string left = "1" + half;
      string right = left;
      reverse(right.begin(), right.end());
      six_one.push_back(pair<string, string>(left, right));
    } while (next_permutation(half.begin(), half.end()));
  }
  for (vector<pair<string, string> >::const_iterator it
         = six_one.begin(); it != six_one.end(); ++it) {
    numbers.push_back(it->first+"0"+it->second);  // odd length
    numbers.push_back(it->first+it->second);  // even length
  }
  // 1 x '2' with 3 x '1'  (IMPOSSIBLE)
  // 7 x '1'  (length must be odd, middle is '1')
  for (vector<pair<string, string> >::const_iterator it
         = six_one.begin(); it != six_one.end(); ++it) {
    numbers.push_back(it->first+"1"+it->second);  // odd length
  }
  // 2 x '2'  (refer 2 x '1', replace '1' to '2')
  for (vector<pair<string, string> >::const_iterator it
         = two_one.begin(); it != two_one.end(); ++it) {
    string str = it->first+"0"+it->second;  // odd length
    str[0] = str[str.length()-1] = '2';
    numbers.push_back(str);
    str = it->first+it->second;  // even length
    str[0] = str[str.length()-1] = '2';
    numbers.push_back(str);
  }
  // 1 x '2' with 4 x '1'  (length must be odd, middle is '2')
  for (vector<pair<string, string> >::const_iterator it
         = four_one.begin(); it != four_one.end(); ++it) {
    numbers.push_back(it->first+"2"+it->second);  // odd length
  }
  // 8 x '1'
  vector<pair<string, string> > eight_one;
  for (int i = 4; i <= MAXHALF; i++) {
    string half(i-1, '0');
    half[i-2] = half[i-3] = half[i-4] = '1';
    do {
      string left = "1" + half;
      string right = left;
      reverse(right.begin(), right.end());
      eight_one.push_back(pair<string, string>(left, right));
    } while (next_permutation(half.begin(), half.end()));
  }
  for (vector<pair<string, string> >::const_iterator it
         = eight_one.begin(); it != eight_one.end(); ++it) {
    numbers.push_back(it->first+"0"+it->second);  // odd length
    numbers.push_back(it->first+it->second);  // even length
  }
  // 1 x '2' with 5 x '1'  (IMPOSSIBLE)
  // 2 x '2' with 1 x '1' (refer 2 x '1', must be odd length)
  for (vector<pair<string, string> >::const_iterator it
         = two_one.begin(); it != two_one.end(); ++it) {
    string str = it->first+"1"+it->second;  // odd length
    str[0] = str[str.length()-1] = '2';
    numbers.push_back(str);
  }
  // 9 x '1'  (length must be odd, middle is '1')
  for (vector<pair<string, string> >::const_iterator it
         = eight_one.begin(); it != eight_one.end(); ++it) {
    numbers.push_back(it->first+"1"+it->second);  // odd length
  }
  // 1 x '3'  (3^3 = 9 <= 10)
  numbers.push_back("3");

  sort(numbers.begin(), numbers.end(), compare);
  vector<string> fairs;
  fairs.reserve(numbers.size());
  for (vector<string>::const_iterator it = numbers.begin();
       it != numbers.end(); ++it) {
    fairs.push_back(square(*it));
  }

  int testcase;
  cin >> testcase;
  for (int tc = 1; tc <= testcase; tc++) {
    string a, b;
    cin >> a >> b;

    vector<string>::const_iterator tail = upper_bound(fairs.begin(), fairs.end(), b, compare);
    cout << "Case #" << tc << ": "
         << tail - lower_bound(fairs.begin(), fairs.end(), a, compare) << endl;
  }

  return 0;
}

