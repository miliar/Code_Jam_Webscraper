#include<iostream>

using namespace std;

int main() {
 int tes,cases;
 int a,b;
 int count;

 cin>>tes;
 
 for(cases=1; cases<=tes; cases++) {
  cin>>a>>b;

  count = 0;
  if(1>=a && 1<=b)
   count++;

  if(4>=a && 4<=b)
   count++;
  
  if(9>=a && 9<=b)
   count++;

  if(121>=a && 121<=b)
   count++;

  if(484>=a && 484<=b)
   count++;

  cout<<"Case #"<<cases<<": "<<count<<endl;
 }
 return 0;
}
