#include <string>
#include <iostream>
//#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <ios>
#include <vector>
#include <string.h>
//#include <algorithm>
#include <map>
#include <stdlib.h>

char *insert(char c, char *word);
char *append(char c, char *word);

/*
 * 1<=T<=100
 * 
 * 1<=len S<=15
 * 1<=len S<=1000
 * 
 * S=string.
 * 
 * So, we receive the string, as a stream, character-by-character.
 * 
 * Get the biggest one, and put it in front, if not bigger than biggest, put last... lets see.
 */
int main(int argc, char **argv)
{
  std::ifstream in;
  std::ofstream out;
  std::stringstream buf;
  std::string s;
  int T,t=0;  // number of test cases.
  const char *word;
  char buffer[2001];
  char *last_word=&(buffer[1000]);
  
  if(argc==2)
  {
    in.open(argv[1]);
    out.open((std::string(argv[1]) + ".out").c_str(),std::ofstream::out|std::ofstream::trunc);
    std::getline(in,s);  // number of test cases
    buf.str(s);
    buf >> T;  // T test cases
    buf.clear();
    while(t<T)
    {
      t++;
      std::getline(in,s);
      word=s.c_str();
      int i=0;
      char largest=0;
      char *head=last_word;
      char *tail=last_word;
      head[0]=0;
      head[1]=0;
      head[-1]=0;
      while(word[i] && word[i] != '\n')
      {
        if(word[i] >= largest)
        {
          largest=word[i];
          head=insert(word[i],head);
        }
        else
        {
          tail=append(word[i],tail);
        }
        i++;
      }
      out << "Case #" << t << ": " << head << "\n";
    }
    return 0;
  }
  // help.
  std::cout << "Usage: \n\n" << argv[0] << " input_file\n\n Output file will be input_file.out\n" << std::endl;
  return 1;
}

char *append(char c, char *word)
{
  *word = c;
  word++;
  *word = 0; // add the null char.
  return word; // return new tail
}

char *insert(char c, char *word)
{
  word--; // pre-decrement, yes, we start at the same position as the head.
  *word=c;
  return word;
}