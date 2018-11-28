#include <iostream>
#include <string>
#include <vector>
using namespace std;

int count_a (vector<char> & s, char a){
  int r = 0;
  for (int i = 0; i < s.size(); ++i){
    if (s[i] == a)
      r++;
  }

  //cout << "count " << a << "=" << r << endl;
  return r;
}

void remove_a (vector<char> & s, char a, int num){
   for (int i = s.size() - 1; i >= 0; --i){
     if (num != 0 && s[i] == a){
       num--;
       s.erase(s.begin() + i);
     }
   }

   /*for (int i = 0; i < s.size(); ++i){
     cout << s[i];
   }
   cout << endl;*/
}

int main (){
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t){
    int res;
    string s;
    cin >> s;
    //cout << s << endl;
    vector<int> digits(10);
    vector<char> letters;

    for (int i = 0; i < s.size(); ++i)
      letters.push_back(s[i]);
   /*for (int i = 0; i < letters.size(); ++i){
     cout << s[i];
   }
   cout << endl;*/

    /*zero z*/
    int n = count_a (letters, 'Z');
    remove_a (letters, 'Z', n); 
    remove_a (letters, 'E', n); 
    remove_a (letters, 'R', n); 
    remove_a (letters, 'O', n); 
    digits[0] = n;


    /*two w*/
    n = count_a (letters, 'W');
    remove_a (letters, 'T', n); 
    remove_a (letters, 'W', n); 
    remove_a (letters, 'O', n); 
    digits[2] = n;

    /*six x*/
    n = count_a (letters, 'X');
    remove_a (letters, 'S', n); 
    remove_a (letters, 'I', n); 
    remove_a (letters, 'X', n); 
    digits[6] = n;

    /*seven s*/
    n = count_a (letters, 'S');
    remove_a (letters, 'S', n); 
    remove_a (letters, 'E', n); 
    remove_a (letters, 'V', n); 
    remove_a (letters, 'E', n); 
    remove_a (letters, 'N', n); 
    digits[7] = n;
    /*five v*/

    n = count_a (letters, 'V');
    remove_a (letters, 'F', n); 
    remove_a (letters, 'I', n); 
    remove_a (letters, 'V', n); 
    remove_a (letters, 'E', n); 
    digits[5] = n;

    /*four f*/
    n = count_a (letters, 'F');
    remove_a (letters, 'F', n); 
    remove_a (letters, 'O', n); 
    remove_a (letters, 'U', n); 
    remove_a (letters, 'R', n); 
    digits[4] = n;

    /*three r*/
    n = count_a (letters, 'R');
    remove_a (letters, 'T', n); 
    remove_a (letters, 'H', n); 
    remove_a (letters, 'R', n); 
    remove_a (letters, 'E', n); 
    remove_a (letters, 'E', n); 
    digits[3] = n;

    /*one o*/
    n = count_a (letters, 'O');
    remove_a (letters, 'O', n); 
    remove_a (letters, 'N', n); 
    remove_a (letters, 'E', n); 
    digits[1] = n;

    /*eight t*/
    n = count_a (letters, 'T');
    remove_a (letters, 'E', n); 
    remove_a (letters, 'I', n); 
    remove_a (letters, 'G', n); 
    remove_a (letters, 'H', n); 
    remove_a (letters, 'T', n); 
    digits[8] = n;
    
    /*nine E*/
    n = count_a (letters, 'E');
    digits[9] = n;

    cout << "Case #" << t << ": ";
    for (int i=0; i <10; ++i){
      while (digits[i] != 0){
        cout << i;
        digits[i]--;
      }
    }
    cout << endl;
  }


}
