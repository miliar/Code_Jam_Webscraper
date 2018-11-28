#include <iostream>  
#include <sstream>
#include <string>
#include <algorithm>
using namespace std; 

int plus_streak(const string &s)
{
    int i=0;
    for(char c:s) {
	if(c == '-')
	    return i;
	else ++i;
    }
    return i;
}

int plus_streak_from_back(string s)
{
    reverse(begin(s), end(s));
    return plus_streak(s);
}

int flipN(string &s, int num_elements)
{
   if(num_elements == 0) return 0;

   reverse(begin(s), begin(s)+num_elements);
   for(auto it = begin(s); it != begin(s) + num_elements; ++it){
       if(*it=='-') *it='+';
       else *it='-';
   }
   return 1;
}

int main() {
    int t;
    string s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
	cin >> s;
	int count = 0;
	int foundation = plus_streak_from_back(s);
	while(foundation < s.length()) {
	    int ps = plus_streak(s);
	    count += flipN(s, ps);
	    count += flipN(s, s.length() - foundation);
	    foundation = plus_streak_from_back(s);
	}
	cout << "Case #" << i << ": " <<count<<endl;
    }
    return 0;
}
