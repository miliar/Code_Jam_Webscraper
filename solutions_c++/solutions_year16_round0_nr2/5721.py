#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <map>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void flip(string * stack,int begin, int end) {
   string newStack="";
   for(int i = begin ; i< end ;i++)
   {
        char singleChar = (*stack)[end-i-1];
        if       (singleChar == '+') newStack+="-";
        else if  (singleChar == '-') newStack+="+";
        else
        {
            cout << "wat" << endl;
        }
   }
   for(int i =0; i< newStack.length();i++)
   {
        (*stack)[i]=newStack[i];
   }
   //return newStack + stack.substr(end,stack.length()-end);
    return;
}

void recursiveSolve(int &count, string * input, int begin, int size) {
    if(size==0) return;
    int strlen = size;
    int  plusCount = 0;
    char character = (*input)[0];
    while (character == '+')
    {
        plusCount++;
        character = (*input)[plusCount];
    }
    if (plusCount == strlen)
    {
        return;
    }
    else if ( (*input)[strlen-1] == '-')
    {
        if(plusCount != 0)
        {
            flip(input,0,plusCount);
            count++;
        }
        flip(input,0,strlen);
        count++;
        //recursiveSolve(count,input.substr(0,strlen-1) )
        recursiveSolve(count,input,0,strlen-1 );
        return;
    }
    else if( (*input)[strlen-1] == '+' )
    {
        recursiveSolve(count, input,0,strlen-1 );
        return;
    }
    cout << "shouldn't reach here?" << endl;;
    return;
}

int main() {
  long t;
  string N;
  //string * test= new string("-+-");
  //cout << "before: " << *test << endl;
  //int count = 0;
  //recursiveSolve(count,test,0,test->length()); 
  //cout << "after: " << *test << endl;
  //cout << "count: " << count << endl;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> (N) ;  // read n and then m.
    string * testString = new string(N);
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    int count = 0;
    recursiveSolve(count,testString,0,testString->length());
    cout << "Case #" << i << ": " << count << endl;
  }
}
