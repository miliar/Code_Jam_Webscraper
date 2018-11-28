#include <stdio.h>
#include <map>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(){
ifstream inpfile("input.txt");
int Tee, S;
inpfile >> Tee;
string str;

for(int l=1; l<=Tee; l++){

inpfile >> str;
std::map<int,int> myMap;
myMap[0] = 0;
myMap[1] = 0;
myMap[2] = 0;
myMap[3] = 0;
myMap[4] = 0;
myMap[5] = 0;
myMap[6] = 0;
myMap[7] = 0;
myMap[8] = 0;
myMap[9] = 0;


std::map<char,int> strMap;

//Find instances of Z i.e for ZERO. If found eleminate Z,E,R,O for every count
size_t Z = std::count(str.begin(), str.end(), 'Z');
myMap[0] = Z;
//Remove Z, E, R, O exactly count number of times
if(Z != 0){
  for(int i=0;i<Z;i++){
     std::size_t found = str.find_first_of("Z");
    //cout << found <<endl;
     str.erase (found, 1);
    //cout << str << endl;
     found = str.find_first_of("E");
    //cout << found <<endl;
     str.erase (found, 1);
    //cout << str << endl;
     found = str.find_first_of("R");
    //cout << found <<endl;
     str.erase (found, 1);
    //cout << str << endl;
     found = str.find_first_of("O");
    //cout << found <<endl;
     str.erase (found, 1);
    //cout << str << endl;
   }
}

//Find instances of W  i.e for TWO. If found eleminate T, W,O for every count
size_t W = std::count(str.begin(), str.end(), 'W');
myMap[2] = W;
//Remove T, W, O exactly count number of times
if(W != 0){
  for(int i=0;i<W;i++){
     std::size_t found = str.find_first_of("T");
    str.erase (found, 1);
     found = str.find_first_of("W");
     str.erase (found, 1);
     found = str.find_first_of("O");
    str.erase (found, 1);
   }
}


//Find instances of U  i.e for FOUR. If found eleminate FOUR for every count
size_t U = std::count(str.begin(), str.end(), 'U');
myMap[4] = U;
//Remove FOUR exactly count number of times
if(U != 0){
  for(int i=0;i<U;i++){
     std::size_t found = str.find_first_of("F");
    str.erase (found, 1);
     found = str.find_first_of("O");
     str.erase (found, 1);
     found = str.find_first_of("U");
    str.erase (found, 1);
     found = str.find_first_of("R");
    str.erase (found, 1);
   }
}

//Find instances of X  i.e for SIX. If found eleminate SIX for every count
size_t X = std::count(str.begin(), str.end(), 'X');
myMap[6] = X;
//Remove SIX exactly count number of times
if(X != 0){
  for(int i=0;i<X;i++){
     std::size_t found = str.find_first_of("S");
     str.erase (found, 1);
     found = str.find_first_of("I");
     str.erase (found, 1);
     found = str.find_first_of("X");
     str.erase (found, 1);
   }
}

//Find instances of G  i.e for EIGHT. If found eleminate EIGHT for every count
size_t G = std::count(str.begin(), str.end(), 'G');
myMap[8] = G;
//Remove EIGHT exactly count number of times
if(G != 0){
  for(int i=0;i<G;i++){
     std::size_t found = str.find_first_of("E");
    str.erase (found, 1);
     found = str.find_first_of("I");
    str.erase (found, 1);
     found = str.find_first_of("G");
    str.erase (found, 1);
     found = str.find_first_of("H");
  str.erase (found, 1);
     found = str.find_first_of("T");
    str.erase (found, 1);
   }
}


//Find instances of T  i.e for THREE. If found eleminate THREE for every count
size_t T = std::count(str.begin(), str.end(), 'T');
myMap[3] = T;
//Remove THREE exactly count number of times
if(T != 0){
  for(int i=0;i<T;i++){
     std::size_t found = str.find_first_of("T");
    str.erase (found, 1);
     found = str.find_first_of("H");
     str.erase (found, 1);
     found = str.find_first_of("R");
     str.erase (found, 1);
     found = str.find_first_of("E");
     str.erase (found, 1);
     found = str.find_first_of("E");
     str.erase (found, 1);
   }
}

//Find instances of F  i.e for FIVE. If found eleminate FIVE for every count
size_t F = std::count(str.begin(), str.end(), 'F');
myMap[5] = F;
//Remove FIVE exactly count number of times
if(F != 0){
  for(int i=0;i<F;i++){
     std::size_t found = str.find_first_of("F");
     str.erase (found, 1);
     found = str.find_first_of("I");
     str.erase (found, 1);
     found = str.find_first_of("V");
     str.erase (found, 1);
     found = str.find_first_of("E");
    str.erase (found, 1);
   }
}

//Find instances of V  i.e for SEVEN. If found eleminate SEVEN for every count
size_t V = std::count(str.begin(), str.end(), 'V');
myMap[7] = V;
//Remove SEVEN exactly count number of times
if(V != 0){
  for(int i=0;i<V;i++){
     std::size_t found = str.find_first_of("S");
     str.erase (found, 1);
     found = str.find_first_of("E");
     str.erase (found, 1);
     found = str.find_first_of("V");
     str.erase (found, 1);
     found = str.find_first_of("E");
     str.erase (found, 1);
     found = str.find_first_of("N");
    str.erase (found, 1);
   }
}

//Find instances of O  i.e for ONE. If found eleminate ONE for every count
size_t O = std::count(str.begin(), str.end(), 'O');
myMap[1] = O;
//Remove ONE exactly count number of times
if(O != 0){
  for(int i=0;i<O;i++){
     std::size_t found = str.find_first_of("O");
     str.erase (found, 1);
     found = str.find_first_of("N");
    str.erase (found, 1);
     found = str.find_first_of("E");
     str.erase (found, 1);
   }
}

//Find instances of N  i.e for NINE. If found eleminate NINE for every count
size_t N = std::count(str.begin(), str.end(), 'N');
myMap[9] = N/2;
//Remove NINE exactly count number of times
if(N/2 != 0){
  for(int i=0;i<N/2;i++){
     std::size_t found = str.find_first_of("N");
     str.erase (found, 1);
     found = str.find_first_of("I");
     str.erase (found, 1);
     found = str.find_first_of("N");
     str.erase (found, 1);
     found = str.find_first_of("E");
     str.erase (found, 1);
   }
}

//Iterate the map and print the numbers in ascending order
cout << "Case #"<<l<<": ";
for(int i=0;i<10;i++){
          for(int k=0; k<myMap[i]; k++){
              cout<<i;
           }
}
printf("\n");

} 
return 0;
}




