#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;

struct Person {
  int shy;
  struct Person *next;
};

int main() {

  string read;
  int tests;

  //get how many lines we have to read
  //ifstream file ("ov_in.txt", ifstream::in);

  //getline(file, read);
  getline(cin, read, '\n');
  tests = stoi(read);

  struct Person *list = NULL;

  //go through the lines
  int cas = 1;
  while (tests > 0) {
    //get line and go to important data
    //getline(file, read);
    getline(cin, read, '\n');

    int i = 0;
    while (read[i] != ' ') i++;
    i++;
    int temp = i;

    //for each number
    for (i = i; i < read.length(); i++) {
      //add a person with i-temp shyness in order each time
      int times = read[i]-'0';
      while (times > 0) {
        struct Person *p = list, *prev = NULL;

        while (p != NULL && p->shy < i-temp) { prev = p; p = p->next; }
        if (prev == NULL) {
          list = (struct Person *)malloc(sizeof(struct Person));
          list->next = p;
          list->shy = i-temp;
        } else {
          struct Person *p2 = (struct Person *)malloc(sizeof(struct Person));
          p2->shy = i-temp;
          p2->next = p;
          prev->next = p2;
        }

        times--;
      }
    }

    //people to keep track of how many we need to add
    int people = 0;
    int standing = 0;

    //output here
    while (list != NULL) {
      if (standing < list->shy) { //if the next person won't stand
        people += list->shy - standing;
        standing += list->shy - standing;
      }
      standing++;
      list = list->next;
    }
    cout << "Case #"<< to_string(cas) << ": " << to_string(people) << "\n";

    tests--;
    cas++;
  }
}
