// Counting sheep Google Code Jam 2016

#include <bitset>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <unordered_set>

using namespace std;

void printIt(const vector<bool> & v) {
  string s = "";
  for (bool b : v) {
    s += (b ? "1" : "0");
  }
  cout << s << endl;
}

struct Path {
  vector<bool> bits;
  long count;

  Path(const vector<bool> & b) {
    bits = b;
    count = 0;
  }

  // flip 
  void flip(int num) {
    for (int i = 0; i < ((num + 1)/2); ++i) {
      bool temp = bits[i];
      temp = !temp;
      bits[i] = bits[num - 1 - i];
      bits[i] = !bits[i];
      bits[num - 1 - i] = temp;
    }
    count++;
  }


  bool allFlipped() {
    for (auto i : bits) {
      if (!i) {
	return false;
      }
    }
    return true;
  }

};

typedef deque<Path> Queue;

int FlipIt(Queue & q) {
  unordered_set< vector<bool> > hash;
  while (!q.empty()) {
    Path p = q.front();
    q.pop_front();
    if (p.allFlipped()) {
      return p.count;
    }
    hash.insert(p.bits);
    int len = p.bits.size();
    // Don't need to flip already-up pancakes at end
    while (len > 0 && (p.bits[len-1]==true)) {
      len--;
    }
    for (int i = 0; i < len; ++i) {
      Path next = p;
      next.flip(i + 1);
      if (hash.find(next.bits) != hash.end()) {
	continue;
      } else {
	hash.insert(next.bits);
      }
      q.push_back(next);
    }
    // generate all possibilities
    // push on queu
  }
  return -1; // error
}

void run() {
  string input;
  getline(cin, input);
  long count = atoi(input.c_str());
  for (long i = 0; i < count; ++i) {
    getline(cin, input);
    const size_t len = input.size();
    vector<bool> bits(len, false);
    for (int j = 0; j < len; ++j) {
      bits[j] = ((input[j] == '-') ? false : true);      
    }
    Path p(bits);
    Queue q;
    q.push_back(p);
    int flips = FlipIt(q);
    cout << "Case #" << (i+1) << ": " << flips << endl;
  }
}

int main(int argc, const char* argv[]) {
  run();
}

  
