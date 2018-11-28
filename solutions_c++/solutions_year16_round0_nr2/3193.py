#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string s;

void reverse(int start , int end){
  string res = "";
  for(int i = 0 ; i < start ; i++)
    res += s[i];
  for(int i = end ; i >= start ; i--)
    res += s[i];
  for(int i = end+1 ; i < s.size() ; i++)
    res += s[i];
  s = res;
}

void init(int start , int end){
  for(int i = start ; i <= end ; i++){
    if(s[i] == '-')
      s[i] = '+';
    else
      s[i] = '-';
  }
}

bool check(){
  for(int i = 0 ; i < s.size() ; i++)
    if(s[i] == '-')
      return false;
  return true;
}

int main(){
  int t;
  cin >> t;
  for(int i = 0 ; i < t ; i++){
    cin >> s;
    int res = 0 , start = 0 , end = s.size() - 1;
    while(!check()){
      res++;
      while(s[end] == '+')
	end--;
      if(s[start] == '+'){
	for(int i = start ; i <= end ; i++)
	  if(s[i] == '-'){
	    init(start , i-1);
	    break;
	  }
      }else{
	reverse(start , end);
	init(start , end);
      }	    
    }
    cout << "Case #" << i+1 << ": " << res << endl;
  }
  return 0;
}
