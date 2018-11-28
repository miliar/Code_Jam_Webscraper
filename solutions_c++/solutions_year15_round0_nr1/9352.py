#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>

using namespace std;

int getMinFriends( int, string);

int main()
{
  ifstream file;
  file.open("input.txt");
  int size;
  int maxShy;
  string audString;
  /* char* audString;*/


  if( file.is_open() )
  {
    file >> size;

    int i = 0;
    while( i < size )
    {
      file >> maxShy;
      getline( file, audString );
      /* 
      cout<< "Max shy is " << maxShy << endl;
      */
      int min;
      min = getMinFriends( maxShy, audString );     
      cout << "Case #" << i+1 << ": ";

      cout << min << endl;
      /* cout<< " string is " << audString << endl;*/
      i++;
    }

  }

  file.close();

  /* int clap = 0;*/
  
  return 0;
}

int getMinFriends( int shy, string str )
{
  int i;
  int min = 0;
  int extra = 0;

  if( !shy )
    return 0;

  /* ignore first white space*/
  for( i = 1; i < shy+2; i++ )
  {
    /*
    cout << "String[i] is " << str[i] << endl;
    cout << "its int value is " << str[i] - '0'  << endl;
    */

    // negative
    if( extra < i-1 )
    {
      min++;
      extra++;
    }
    extra += str[i] - '0';
    /*
    cout << "min is " << min << endl;
    */

  }
  return min;
}
