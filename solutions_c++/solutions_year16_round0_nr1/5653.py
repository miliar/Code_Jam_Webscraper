#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <map>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  long t, N;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> N ;  // read n and then m.
    //cout << N << endl;
    if(N == 0)
    {
        cout << "Case #" << i << ": " << "INSOMNIA" << endl;
        continue;
    }
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    string numbersFound="";
    int j=0;
    while(true)
    {
        long current      = N * (j+1);
        string numString = to_string(current);
        for(int k =0; k< numString.length();k++)
        {
            char character = numString[k];
            std::size_t found = numbersFound.find(character);
            if(found == std::string::npos)
            {
                numbersFound += character;
                //cout << numbersFound<< endl;
            }
    
        }
        if (numbersFound.length() == 10)
        {
            cout << "Case #" << i << ": " << current << endl;
            break;
        }
        j++;
    }
  }
}
