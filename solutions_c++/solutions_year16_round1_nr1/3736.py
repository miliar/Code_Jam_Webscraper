#include <iostream>
#include <string>

using namespace std;

string *lastWord;

void add(char a){
  if (lastWord->length() && a >= lastWord->at(0))
      lastWord->insert(0,1,a);
    else
      lastWord->append(1,a);
}

void clean(){
  lastWord = new string();
}

int main(){
  int testCases=0,cas=0;
  string s;

  cin>>testCases;
  while(testCases>0){
    cin>>s;
    clean();
    int tam = s.length();
    for (int i=0; i<tam; i++) {
      add(s.at(i));
    }

    cas++;
    cout << "Case #" << cas << ": ";
    cout << *lastWord << endl;
    testCases--;
  }
}
