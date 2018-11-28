#include<iostream>
#include<string>

using namespace::std;

int calculate_people(int max, string str) {
  int si[max+1];
  for (int i=0; i<max+1; i++) {
    si[i] = str[i] - '0';
  }
  int npeople_standing = si[0];
  int res = 0;

  for (int i=1; i<max+1; i++) {
    //cout<<endl<<i;
    while (true) {
      if (i <= npeople_standing) {
        npeople_standing += si[i];
        break;
      } else {
        res++;
        npeople_standing++;
        //cout<<"ins "<<i<<" "<<npeople_standing<<endl;
      }
    }
    //cout<<endl<<npeople_standing<<endl;
  }

  return res;
}

int main () {
  int testcases;
  int s_max;
  string shyness_str;
  cin>>testcases;
  for (int i=0; i<testcases; i++){
    cin>>s_max;
    cin>>shyness_str;
    int result = calculate_people(s_max, shyness_str);
    cout<<"Case #"<<i+1<<": "<<result<<endl;
  }
  return 0;
}
