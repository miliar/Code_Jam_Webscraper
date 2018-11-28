#include <stdio.h>
#include <map>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
ifstream inpfile("input.txt");
int T;
inpfile >> T;
int i;

for(int l=1; l<=T; l++){

inpfile >> i;
if(i == 0){
   printf("Case #%d: INSOMNIA\n",l);
   continue;
}

map<char, int> myMap;
for(int k=0; k<10; k++)
  myMap[k + '0'] = 0;

int count = 1;
char buffer[100];
bool repeat = false;
int temp = i;

while(1){

sprintf(buffer, "%d", temp);

for(int j=0; j<strlen(buffer); j++){
    myMap[buffer[j]]++;
}

map<char,int>::iterator it=myMap.begin();

for (; it!=myMap.end(); ++it) {
    if(it->second == 0){
        count++;
        temp = i*count;
        break;
     }
}

if(it == myMap.end()){
  printf("Case #%d: %d\n",l,temp);
  break;
}

}

}
return 0;
}




