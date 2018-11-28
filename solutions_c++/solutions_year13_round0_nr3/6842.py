#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>

using namespace std;

bool palindromeCheck(string str ) {
     int len =str.size();
     for(int i=0;i<len/2;i++)
     if (str[i]!=str[len-i-1]) return false;
     return true;
     }

 int fairSquare(long min,long max){
     int start=ceil(sqrt(min));
     int end=floor(sqrt(max));
     int count=0;
      char buffer [sizeof(long)*8+1];
     for (int i=start;i<=end;i++)
     if(palindromeCheck(ltoa (i,buffer,10))&& palindromeCheck(ltoa (i*i,buffer,10))) count++;
     return count;
     }


int main() {
    ifstream infile("in.txt");
        ofstream outfile("out.txt");
    int T,count=0;
    long min,max;
    string line;
    const char * arr ;
    infile >> T;
    for (int i = 1; i <= T; i++) {      
           infile >> min >> max;  
           outfile << "Case #"<<i<<": ";
           outfile<< fairSquare(min,max);
           outfile << endl;                
    }
    return 0;
}
