#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void InsertWords(set<string>* words,
                 const string& sentence) {

  string word;
  stringstream sentence_stream(sentence);
  while (sentence_stream >> word) {
    words->insert(word);
  }
}

int NumBothEnFr(const set<string>& english_words,
                const set<string>& french_words) {
  set<string> intersect;
  set_intersection(english_words.begin(), english_words.end(),
                   french_words.begin(), french_words.end(),
                   inserter(intersect, intersect.begin()));
  return intersect.size();
}

int global_min;

int MinNumBothEnFr(int depth,
                   const vector<string>& sentences,
                   set<string>* english_words,
                   set<string>* french_words) {
  int current_num = NumBothEnFr(*english_words, *french_words);
  if (global_min <= current_num) {
    // Already found better answer, exit.
    return global_min;
  }
  if (depth >= sentences.size()) {
    global_min = current_num;
    // New answer!
    return current_num;
  }
  set<string> if_english_words(*english_words);
  set<string> if_french_words(*french_words);
  InsertWords(&if_english_words, sentences[depth]);
  InsertWords(&if_french_words, sentences[depth]);
  int min_num = min(MinNumBothEnFr(depth + 1, sentences,
                                   english_words, &if_french_words),
                    MinNumBothEnFr(depth + 1, sentences,
                                   &if_english_words, french_words));
  return min_num;
}

int main() {
  // Read test case size.
  string input;
  int test_case_size;
  cin.clear();
  getline(cin, input);
  stringstream input_stream(input);
  input_stream >> test_case_size;
  for (int test_case_num = 0; test_case_num < test_case_size; ++test_case_num) {
    // Read sentences size.
    int sentence_size;
    cin.clear();
    getline(cin, input);
    stringstream input_stream(input);
    input_stream >> sentence_size;
    // Read all sentences.
    vector<string> sentences;
    for (int i = 0; i < sentence_size; i++) {
      string sentence;
      cin.clear();
      getline(cin, sentence);
      sentences.push_back(sentence);
    }
    // Init first sentence into English words, second into French words.
    set<string> english_words;
    set<string> french_words;
    InsertWords(&english_words, sentences[0]);
    InsertWords(&french_words, sentences[1]);
    // Calculate the min number of words for both English and French.
    global_min = 100000000;
    cout << "Case #" << test_case_num + 1 << ": "
         << MinNumBothEnFr(2, sentences, &english_words, &french_words)
         << endl;
  }
  return 0;
}
