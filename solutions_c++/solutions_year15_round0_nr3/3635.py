#include <iostream>
#include <fstream>
#include <string>
#include <sstream> 
#include <stdlib.h> 
#include <set>

using namespace std; 

enum value{LETTERI, LETTERJ, LETTERK, ONE} ;

bool correct(string a, int reps);
value multiply (value a, value b) ;
bool positiv(value a, value b);
value charToVal(char a);
bool sameRes(string a, int c , int b, value val);
set<int> iPos(string a, int reps);
set<int> kPos(string a, int reps);

int  main(){
  ifstream myfile;
  ofstream ofile;
  string word;

  myfile.open ("C-small-attempt1.in");
  ofile.open("C-small-attempt1.out");
  getline(myfile, word); 
  int count = 1;
  const char* nbcases= word.c_str();
  int cases = atoi(nbcases);

  while (count<=cases){
    ofile << "Case #"  << count << ": ";
    int letters;
    myfile >> letters; 
    int reps;
    myfile >> reps;
    getline(myfile,word);
    getline(myfile, word);
    if(reps*letters<3 ){
      ofile << "NO" << endl;
   }
    else {
      if(correct(word, reps))
	ofile << "YES" << endl;
      else
	ofile << "NO" << endl;
    }
    count++;
  }
  ofile.close();
  myfile.close();
  return 0;
}

bool correct(string a, int reps){
  set<int> positionsI = iPos(a, reps);
  set<int> positionsK = kPos(a, reps);
  if (positionsI.empty() || positionsK.empty())
    return false;
   for(set<int>::iterator it1 = positionsI.begin(); it1!=positionsI.end(); it1++){
     if(sameRes(a, (*it1)+1, a.length()*reps, multiply(LETTERJ, LETTERK)))
     for(set<int>::iterator it2 = positionsK.begin(); it2!=positionsK.end(); it2++){
       if(*it1 < *it2 && sameRes(a, (*it1)+1, *it2, LETTERJ)) 
	return true;
     }
  }
  return false;
}

set<int> iPos(string a, int reps){
  set<int> positions;
  bool sign = true;
  value temp = ONE;
  for(int i = 0; i<a.length()*reps; i++){
    value newval = charToVal(a[i%a.length()]);
    temp = multiply(temp, newval); 
    sign = positiv(temp, newval) ^ sign;
    if(temp == LETTERI && sign){
	 positions.insert(i);
    }
  }
  return positions;
}

bool sameRes(string a, int ind1, int ind2, value val){
  bool sign = true;
  value temp =ONE;
  for(int i = ind1; i<ind2; i++){
    value newval = charToVal(a[i%a.length()]);
    temp = multiply(temp, newval); 
    sign = positiv(temp, newval) ^ sign;
  }
  if(sign && temp == val)
    return true;
  else 
    return false;
}

set<int> kPos(string a, int reps){
  set<int> positions;
  bool sign = true;
  value temp = ONE;
  for(int i = a.length()*reps-1; i>1; i--){
    value newval = charToVal(a[i%a.length()]);
    temp = multiply(newval, temp); 
    sign = positiv(newval, temp) ^ sign;
    if(temp == LETTERK){
      positions.insert(i);
    }
  }
  return positions;
}

value charToVal(char a){
  if(a=='i')
    return LETTERI;
  if(a=='j')
    return LETTERJ;
  if(a=='k')
    return LETTERK;
  if(a=='1')
    return ONE;
}

value multiply (value a, value b) {
  if (a==ONE)
    return b;
  if (b==ONE)
    return a;
  if(a==b)
    return ONE;
  if((a == LETTERJ && b == LETTERK)||(b == LETTERJ && a == LETTERK))
    return LETTERI;
  if((a == LETTERI && b == LETTERK)||(b == LETTERI && a == LETTERK))
    return LETTERJ;
  if((a == LETTERJ && b == LETTERI)||(b == LETTERJ && a == LETTERI))
    return LETTERK;  
}

bool positiv(value a, value b){
  if(a!=ONE && a==b)
    return false;
  if(a == LETTERI && b == LETTERK)
    return false;
  if(a == LETTERJ && b == LETTERI)
    return false;
  if(a == LETTERK && b == LETTERJ)
    return false;
  return true;
}
