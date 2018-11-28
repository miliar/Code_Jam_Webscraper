#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
  bool check_palindrome(unsigned long int temp_int);
  int square(unsigned long int);
 ofstream output_large ("out_large.txt");
 ifstream given_input("test.in");
 int T, palindrome_count = 0; ;

 unsigned long int a,b, a_intv, b_intv;
 given_input >> T;

for(int tc_count=1; tc_count<= T; tc_count++){
    given_input >>a >>b;
    palindrome_count = 0;

    //check if A and B are palindrome
    //if(check_palindrome(a))
   // {
   //     palindrome_count+=1;

    //}
   // if(check_palindrome(b)) palindrome_count+=1;

    a_intv = static_cast<int>(std::ceil(std::sqrt(a)));
    b_intv = static_cast<int>(std::floor(std::sqrt(b)));

    cout << a_intv <<endl;
    cout << b_intv <<endl;
   // if() b_intv++;
    cout << "range Used" <<" "<< square(a_intv) <<"->" << square(b_intv) << endl;
 for(unsigned long int intv = a_intv; intv <=b_intv; intv++){
  if(check_palindrome(intv)){
      if(check_palindrome(square(intv))){
          palindrome_count+=1;
          cout << square(intv)<<"-------->pali" << endl;
      }
  }
 }

output_large << "Case #"<< tc_count <<": "<< palindrome_count<< endl;
}
return 0;
 }
bool check_palindrome(unsigned long int temp_int){
    stringstream str_temp_stream;
    str_temp_stream << temp_int;
    string str_temp = str_temp_stream.str();
    if(str_temp.length()== 1) return true;
   for(int temp_i=0; temp_i< str_temp.length(); temp_i++){
       if(str_temp[temp_i] != str_temp[str_temp.length()-temp_i-1]){
         return false;
       }
   }
return true; //palindromic
}

int square(unsigned long int no_to_square){
    return no_to_square * no_to_square;
}
