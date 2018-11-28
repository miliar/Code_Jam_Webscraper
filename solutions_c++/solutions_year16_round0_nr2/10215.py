// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <map>
#include <stdlib.h>

#include<stdio.h>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;

FILE *stream;


int shortestSweetestPath(const string &str) {
  int len = str.length(), numbers = pow(2, len);
  //cout << "len:"<< len << ", " << numbers << endl;
  std::string happy = std::string(len, '1');
  //cout << "happy->" << happy << endl;
  vector<string> stack;
  stack.push_back(happy);
  map<int, int> allPermutes;
  allPermutes[stoull(happy, 0, 2)] = 0;
  //cout << "stack:" << stack.size() << endl;
  int distance = 1, jStart = 0, jEnd = 1;
  bool flag = true;
  do {
    for(int j = jStart; j < jEnd; ++j) {
      string s(stack[j]);
      for( int i = 1; i <= len; ++i) {
		  string s(stack[j].substr(0, i));
		  //cout << "before:" << s <<  endl;
		  std::reverse(std::begin(s), std::end(s));
          //cout << "after:" << s <<  endl;
		  std::replace( s.begin(), s.end(), '1', '2');
		  std::replace( s.begin(), s.end(), '0', '1');
		  std::replace( s.begin(), s.end(), '2', '0');
		  //cout << "reversed:" << s <<  endl;
		  string restacked(s+stack[j].substr(i));
		  if ( allPermutes.find(stoull(restacked, 0, 2)) == allPermutes.end() ) {
			  stack.push_back(restacked);
			  allPermutes[stoull(restacked, 0, 2)] = distance;
			  //cout << "restacked:" << restacked <<  endl;
			  if ( allPermutes.size() == numbers ) {
				  flag = false;
			  }
		  }
      }
    }
	jStart = jEnd;
	jEnd = stack.size();
	distance++;
  } while(flag);
  /*for(map<int, int>::iterator itr = allPermutes.begin(); itr != allPermutes.end(); ++itr) {
	  cout << itr->first << ": " << itr->second << endl;
  }*/
  return allPermutes[stoull(str, 0, 2)];
}

void Pancakes() {
  freopen_s(&stream, "C:\\Users\\jnambiar\\Downloads\\Pancakes\\B-small-attempt0.in", "r", stdin);
  freopen_s(&stream, "C:\\Users\\jnambiar\\Downloads\\Pancakes\\B-small-attempt0.out", "w", stdout);

  int t;
  cin >> t;

  string stream;
  getline (std::cin, stream);

  for(int i = 1; i <= t; ++i) {
    getline (std::cin, stream);
    //cout << stream << endl;

    std::replace( stream.begin(), stream.end(), '+', '1');
    std::replace( stream.begin(), stream.end(), '-', '0');

	//cout << shortestSweetestPath(stream) << endl;

    cout << "Case #" << i << ": " << shortestSweetestPath(stream) << endl;
  }
}


int main(int argc, const char *argv[]) {
  //cout << "Hello World" << endl;
  Pancakes();
  return(EXIT_SUCCESS);
}
