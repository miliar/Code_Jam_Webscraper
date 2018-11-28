#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <set>
#include <string>
#include <sstream>
using namespace std;

int main()
{
        freopen("A-large.in", "r", stdin);
  freopen("large.txt", "w", stdout);
  long long t,n,count,tt,counter=0;
  long long temp;
  cin >> t;
      set<long long> ar2;
    for(long long j=0;j<10;j++){
        ar2.insert(j);
    }
 /*       for(set<long long> ::iterator j=ar2.begin();j!=ar2.end();j++){
        cout << *j << " --  " << endl;
    }*/
  for(long long i=1;i<=t;i++){
counter=0;
        cin >> n;
count=n;
set<long long> ar;
  while(1){

 //   stringstream ss;
//ss << n;
//string s = ss.str();
 tt=count;
    while(tt!=0){
           // temp=atoi(s[j]);
           temp=tt%10;
           tt/=10;
        ar.insert(temp);
      //   cout << "yoyo" << endl;
    }
  //  cout << "hi" << endl;
  /*          for(set<long long> ::iterator w=ar.begin();w!=ar.end();w++){
        cout << *w << " --  " << endl;
    }
    cout << "hiiiiii" << endl;
*/
counter++;
    if(ar==ar2){
        break;
    }
    else if(counter>12345678)
        break;
    count+=n;
  }
  if(counter<12345678)
 cout << "Case #" << i << ": " << count << "\n";
 else
 cout << "Case #" << i << ": INSOMNIA" << "\n";
  }
    return 0;
}
