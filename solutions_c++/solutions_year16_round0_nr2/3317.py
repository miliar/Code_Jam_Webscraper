

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

unsigned numChanges(string&seq)
{
  unsigned numC = 0;
  char last = '.';
  for(char a : seq){
    numC += a != last ? 1 : 0;
    last = a;
  }
  return numC;
}

int main()
{
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');//for removing trailing spaces to endof line
  for(int i = 1; i <= t; ++i) {

    string seq;
    getline(cin, seq);
    while(seq.size() > 0 && seq.back() == '+')
      seq.pop_back();
    //cin >> m;  // read n and then m.
    unsigned numC = numChanges(seq);



    cout << "Case #" << i << ": " << numC << endl;
  }

  return 0;
}

