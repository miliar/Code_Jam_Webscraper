#include<iostream>
#include<stdio.h>
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

ifstream fh("C-small-attempt0.in");
ofstream fho("C-small.txt");
//ifstream fh("C-large.in");
//ofstream fho("C-large-output.in");

string to_string(long long n){
  string s = "";
  while(n){
    s += n%10+48;n/=10;
  }
  return s;
}

bool palindrome(long long n)
{
  string s= to_string(n);
  bool flag=true;
  int len = s.length();
  for(int i=0;i<len/2;++i){
    if(s[i]!=s[len-i-1]){
      flag = false;
      break;
    }
  }
  return flag;
}

vector<int> pal_arr(long long n)
{
  vector<int> arr;
  long long i;
  for(i=0;i<n;++i){
    if(palindrome(i)){
      if(palindrome(i*i)){
        arr.push_back(i);
      }
    }
  }
  return arr;
}

int main(){
  //cout.precision(1);
  long long n=1000,m,a,b,low,upp,t=1;
  vector<int> arr = pal_arr(n);
  vector<int>::iterator it = arr.begin();
  while(it < arr.end()){
    cout<<","<<*(it++);
  }
  cout<<endl;
  it = arr.begin();
  fh>>n;
  while(fh >> a>>b){
    long double aa = sqrt(a), bb = sqrt(b);
    int i=0;
    while(i<arr.size() && aa > *(it+i)){++i;}
    low = i-1;

    i=0;
    while(i<arr.size() && bb >= *(it+i)){++i;}
    upp = i;
    fho<<"Case #"<<t<<": "<<upp-low-1<<endl;
    ++t;
  }
  fho<<endl;
  return 0;
}
