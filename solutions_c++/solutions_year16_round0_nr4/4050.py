#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
int main()
{
   /* char line[255];
    ifstream infile("test.txt");
    getline(infile, line);
   // long long n = atoi();
    cout<<line;*/
   #include <stdio.h>

  char filename[] = "g1.txt";
  FILE *file = fopen ( filename, "r" );

  if (file != NULL) {
    char line [100];
    while(fgets(line,100,file)!= NULL) /* read a line from a file */ {
      printf("%s",line); //print the file contents on stdout.
    }
    long long n = atoi(line);
    cout<<n;

    fclose(file);
  }


  return 0;


}
