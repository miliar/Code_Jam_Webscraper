#include<iostream>
#include<assert.h>
using namespace std;
int chtoi(char c){
  if(c<'0' || '9' < c ){
    return -1;
  }
  return c-'0';
}
int main(void){
  int T;
  cin>>T;
  for(int case_count = 1; case_count <= T; case_count++){
    int s;
    string str;
    cin>>s;
    cin.ignore(0xffffffff, ' ');
    getline(cin, str);
    //    cout<<"str = "<<str<<endl;
    //    cout<<"s = "<< s << endl;
    assert( s == str.size() - 1 );
    int sum = 0;
    int res = 0;
    for( int i = 0; i <= s; i++){
      if(sum < i && chtoi(str[i]) > 0 ){
        res += i-sum;
        sum = i;
      }
      sum += chtoi( str[i] );
    }
    cout << "Case #" << case_count << ": " << res <<endl;
  }
  return 0;
}
