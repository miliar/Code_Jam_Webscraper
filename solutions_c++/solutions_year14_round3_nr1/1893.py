#include <iostream>
#include <algorithm>
#include <vector>
#include<stdio.h>
using namespace std;

int main () {
  int myints[] = {10,20,30,5,15};
  vector<int> v(myints,myints+5);

  make_heap (v.begin(),v.end(),greater<int>());
  cout << "initial max heap   : " << v.front() << endl;

  pop_heap (v.begin(),v.end(),greater<int>()); v.pop_back();
  cout << "max heap after pop : " << v.front() << endl;

  v.push_back(1); push_heap (v.begin(),v.end(),greater<int>());
  cout << "max heap after push: " << v.front() << endl;

  sort_heap (v.begin(),v.end(),greater<int>());

  cout << "final sorted range :";
  for (unsigned i=0; i<v.size(); i++) cout << " " << v[i];

  cout << endl;
  int n;
   scanf("%d",&n);
  return 0;
}
