#include<iostream>
#include<malloc.h>

using namespace std;

int intersection(int *x, int *y){
int c=0, num;
for(int i=0 ; i < 4; i++){
for(int j=0 ; j < 4; j++){
  if(x[i]==y[j]){
       c++;
       num=x[i];
}
  if(c==2)
    return -1;
}}
if(c==1)
  return num;
return c;
}
int main(){ 
int s,test, ans1, ans2, *arr1, *arr2;
cin >> test;
for(int i=0 ; i < test; i++){
cin >> ans1;
arr1=(int *)malloc(sizeof(int)*16);
for(int j=0 ; j< 16; j++){
   cin >> arr1[j];
}
cin >> ans2;
arr2=(int *)malloc(sizeof(int)*16);
for(int j=0 ; j < 16; j++){
   cin >> arr2[j];
}
s=intersection(arr1 + (ans1-1)*4, arr2+(ans2-1)*4);
if(s==0)
  cout << "Case #"<<i+1 << ": Volunteer cheated!" << endl;
else if(s>0)
  cout << "Case #"<<i+1<<": " <<s<< endl;
else
cout << "Case #"<<i+1<<": Bad magician!" << endl;
}
return 0;
}
