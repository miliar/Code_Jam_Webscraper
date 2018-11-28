#include<iostream>
#include<conio.h>
#include<vector>
#include<set>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;
int main() {
    long long int q;
    q =0;
    long long int test;
    cin>>test;
    while(q<test) {
                  long long int n;
                  string s;
                  cin>>s;
                  vector<char> inp(s.begin(), s.end());
                  vector<int> v;
                  
                  cin>>n;
                  for(long long int i =0;i<inp.size(); i++) {
                            char temp = inp[i];
                            int value = 1;
                            if(temp == 'a' || temp == 'e' || temp == 'i'|| temp == 'o'|| temp=='u') {
                                value =0;
                            }
                            v.push_back(value);
                            
                  }
                  int sum =0;
                  int count =0;
                  for(long long int i =0; i<v.size(); i++) {
                          for(long long int j=i; j<v.size();j++) {
                                   if(v[j]==1) {
                                                 sum = sum + 1;
                                   } else {
                                          if(sum<n) {
                                                    sum = 0;
                                          }
                                   }
                                   if(sum>=n) {
                                              count++;
                                   }
                          }
                          sum = 0;
                  }
                  cout<<"Case #"<<q+1<<": "<<count<<endl;
                  q++;
    }
}
