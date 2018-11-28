#include<iostream>
#include<string>

using namespace std;

int main(){

  int num_cases;
  cin >> num_cases;

  for (int i=0;i<num_cases;i++){
    string s;
    cin >> s;
    s = s + "+";

    int req_flips = 0;
    for(int j=s.length()-1;j > 0;j--){
      if(s[j] != s[j-1])
	req_flips++;
    }
    cout << "Case #" << i+1 << ": " << req_flips << endl;
  }
  
  return 0;
}
