#ifndef _MY_LIB_
#define _MY_LIB_

#include "mylib.cpp" // templates -.-

// returns the number of 1's in num
int count_ones(long long num);
// returns true if the array contains the given number
template <class T> bool contains(T element, T *array, int size);
bool contains(char c, char *string);
// min and max
template <class T> bool min(T a, T b);
template <class T> bool max(T a, T b);
// mallocs
template <class T> T **malloc_2d(int rows, int columns);
template <class T> T ***malloc_3d(int X, int Y, int Z);
template <class T> void free_2d(T **matrix, int rows);
template <class T> void free_3d(T ***matrix, int X, int Y);
// read N elements from stdin into an array
template <class T> T *read(int N);
// read up to N words from stdin 
vector<string> read_words(int N);
string read_word(void);

#endif
