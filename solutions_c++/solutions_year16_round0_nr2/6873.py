#include <stdio.h>
#include <map>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
ifstream inpfile("input.txt");
int T;
inpfile >> T;
string str;

for(int l=1; l<=T; l++){

inpfile >> str;

if((str.length() == 1) && (str.c_str()[0] == '-')) {
   printf("Case #%d: 1\n",l);
   continue;
} else if((str.length() == 1) && (str.c_str()[0] == '+')){
   printf("Case #%d: 0\n",l);
   continue;
}

int level_edge=0;
for(int i=0; i < (str.length() - 1); i++){
  if( str.c_str()[i] != str.c_str()[i+1] ) level_edge++;
}

if((str.c_str()[0] == '-') && (str.c_str()[str.length() - 1] == '-'))
  printf("Case #%d: %d\n",l,level_edge+1);
else if((str.c_str()[0] == '-') && (str.c_str()[str.length() - 1] == '+'))
  printf("Case #%d: %d\n",l,level_edge);
else if((str.c_str()[0] == '+') && (str.c_str()[str.length() - 1] == '+'))
  printf("Case #%d: %d\n",l,level_edge);
else if((str.c_str()[0] == '+') && (str.c_str()[str.length() - 1] == '-'))
  printf("Case #%d: %d\n",l,level_edge+1);

}
return 0;
}




