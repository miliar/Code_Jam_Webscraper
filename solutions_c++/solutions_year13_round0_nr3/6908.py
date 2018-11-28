#include <iostream> 
#include <fstream> 
#include <sstream> 
#include <cstdlib> 
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std; 

bool isPalindrome (string a){
  string b = string ( a.rbegin(), a.rend() );
  if ( b == a ){
    return true;
  }
  else
    return false;
}

bool isSquare (int a){
  float b = sqrt(a);
  int c = b;
  stringstream ss;
  ss << c;
  if ( c == b && isPalindrome( ss.str() ) ){
    return true;
  }
    
  else
    return false;
}

int main(int argc, char** argv){ 
    int file[10000];
    int repeat;

    ifstream filein; 
    filein.open(argv[1]); 

    if(filein){
        //cout << "File read" << endl;
        int i = 0;
        while ( !filein.eof() ){
            if ( i == 0 ){
                filein >> repeat;
                //cout << repeat << endl;
            }
            filein >> file[i];
            //cout << file[i] << endl;
            i++;
        }
    }

    else{
        cout << "File cannot be read" << endl;
    }

    int i,k;
    int j = 0;
    int count[repeat];
    int v1,v2,tmp;
    for ( i=0; i < repeat; i++ ){
        count[i] = 0;
        v1 = file[j];
        v2 = file[j+1];
        
        //cout << "v1: " << v1 << endl;
        //cout << "v2: " << v2 << endl;
        //cout << endl;
        j+=2;        
        for( k=v1; k <= v2; k++ ){
            
            stringstream ss;
            ss << k;
            if ( isSquare(k) && isPalindrome(ss.str()) ){
                //cout << "K: " << k << endl;
                count[i]++;
                //cout << "i: " << i << endl;
            }
        }
        cout << "Case #" << i+1 << ": " << count[i] << endl;
    }
    
    filein.close(); 
    system("pause"); 
    return 0; 
}
