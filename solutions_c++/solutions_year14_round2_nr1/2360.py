#include <iostream>
#include <vector>

using namespace std;

typedef vector<string> sv;

bool cmp_char_at_pos(sv &arr, int pos)
{
  char ch = arr[0][pos];
  for(int i=1; i<arr.size(); i++) {
    if(ch != arr[i][pos]) {
      return false;
    }
  }
  return true;
}


int distinct_ch(string &str)
{
  int cnt = 0;

  char ch[26] = {0};

  for(int i=0; i<str.length(); i++) {
    ch[str[i] - 'a'] = 1;
  }

  for(int i=0; i<26; i++)
    cnt += ch[i];

  return cnt;
}


bool check_chars(sv &arr)
{
  int cnt1 = distinct_ch(arr[0]);
  for(int i=1; i<arr.size(); i++) {
    if(cnt1 != distinct_ch(arr[i])) {
      return false;
    }
    
  }
  return true;
}


int str_prev_repest_at_pos(sv &arr, int pos)
{
  for(int i=0; i<arr.size(); i++) {
    if(arr[i][pos] == arr[i][pos-1])
      return i;
  }
  return -1;
}


/*
int del_prev_dup_pos(sv &arr, int pos)
{
  int step = 0;
  int max_step = 0;

  string &str = arr[i];
  for(int j=pos; j<str.length(); j++) {
    if(str[pos-1] == str[pos])
  }
    char ch = arr[start_str][pos];
    for(int i=0; i<arr.size(); i++) {
      if(i==start_str)
	continue;
      //    for(
      if(ch != arr[i][pos]) {
	arr[i].insert(pos, 1, arr[i][pos-1]);
	added = 1;
      }
    }
  }
  else if(!cmp_char_at_pos(arr, pos)) {
    added = -1;
  }
  return added;
}
*/
int add_char_at_pos(sv &arr, int pos)
{
  //  cout << "pos=" << pos << endl;
  int step = 0;
  int start_str = str_prev_repest_at_pos(arr, pos);

  //  cout << "pos=" << pos << ", start=" << start_str << endl;
  if(start_str >= 0) {
    char ch = arr[start_str][pos];
    for(int i=0; i<arr.size(); i++) {
      if(ch != arr[i][pos]) {
	arr[i].insert(pos, 1, arr[i][pos-1]);
	step = 1;
      }
    }
  }
  else if(!cmp_char_at_pos(arr, pos)) {
    //    cout << "here%%%%\n";
    step = -1;
  }

  return step;
}


int get_max_len(sv &arr)
{
  int max_len = 0;
  for(int i=0; i<arr.size(); i++) {
    if(max_len < arr[i].length())
      max_len = arr[i].length();
  }
  return max_len;
}


void print(sv &arr)
{
  cout << "***" << endl;
  for(int i=0; i<arr.size(); i++)
    cout << arr[i] << endl;
}

void process(sv &arr)
{
  // verify if all strings have the same char sets
  if(!check_chars(arr)) {
    cout << "Fegla Won";
    return;
  }

  // verify that all have same first char
  if(!cmp_char_at_pos(arr, 0)) {
    cout << "Fegla Won";
    return;
  }

  // length of biggest string
  int max_len = get_max_len(arr);

  int step=0;
  for(int i=1; i<max_len; i++) {
    //    cout << "#pos:" << i << endl;
    int changed = add_char_at_pos(arr, i);
    if(changed == 0) {
    }
    else if(changed > 0) {
      step++;
      //    print(arr);

      max_len = get_max_len(arr);
      //      cout << "**" << max_len << endl;
    }
    else {
      cout << "Fegla Won";
      return;
    }
  }

  cout << step;
}



int main(int argc, char** argv)
{
  int T;
  cin >> T;
  for(int i=1; i<=T; i++) {

    cout << "Case #" << i << ": ";

    int N;
    cin >> N;
    string str;
    sv arr;

    for(int j=0; j<N; j++) {
      
      cin >> str;
      arr.push_back(str);
    }

    //    print(arr);
    process(arr);
    //    print(arr);

    cout << endl;
  }

  return 0;
}
