#include <stdio.h>
#include <stdint.h>
#include <fstream>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int compute_extra_people_invited(char *a){

int total_people=0;
int invited = 0;
int shyness_levels = strlen(a);

for(int i=0; i<shyness_levels; i++){

  if(i==0){
      total_people += a[i]-48;
      //printf("shyness level: %d, total people: %d \n",i, total_people);
  } else {
    
      if(total_people >= i){
        total_people += a[i]-48;
        //printf("shyness level: %d, total people: %d \n",i, total_people);
      } else {
        invited += i-total_people;
        total_people += i-total_people + a[i]-48;
        //printf("shyness level: %d, invited: %d, total_people: %d \n",i, invited, total_people);
      }
  }

 }

  return invited;
}

int main() {
ifstream myFile;
myFile.open("input.txt");
    
int T=0; 
myFile >> T;
printf("No of test cases: %d \n",T);

int no_of_shyness_levels=0;
char *a = NULL;

for(int i=1; i<=T; i++){

myFile >> no_of_shyness_levels;
a = (char *)malloc(no_of_shyness_levels + 1);
myFile >> a;
//cout << "No of shyness levels: "<<no_of_shyness_levels<<endl;
//cout << "shyness character:  "<<a<<endl;

//compute extra people to be invited
int invited = compute_extra_people_invited(a);
cout << "Case #"<<i<<": "<<invited<<endl;

//free(a);
//a=NULL;
}

return 0;
}
