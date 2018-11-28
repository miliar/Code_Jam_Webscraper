#include <string>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void CoinJam(string temp,int j){
    //express the number as binary then use transfer 1 to 11
    int ind=j,digit;
    for(int num=2;ind!=0;){
        digit = ind & 1;
        //cout<<j<<" "<<digit<<endl;
        if(digit==1){
            temp[num]='1';
            temp[num+1]='1';
            num = num + 2;
        }
        else num++;
        ind=ind>>1;
    }
    cout<<temp<<" "<<"3 "<<"4 "<<"5 "<<"6 "<<"7 "<<"8 "<<"9 "<<"10 "<<"11"<<endl;
}

int main() {
  int t,N,J;
    string temp,str1,str0;
    str1='1';
    str0='0';
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> N >> J;  // read n and then m.
    cout << "Case #" << i << ": " << endl;
    for(int j = 1; j <= J; ++j){
        // reset the temp
        temp = str1+str1;
        for(int k=2; k<N-2;k++)
            temp = temp + str0;
        temp = temp + str1 + str1;
        //temp[N]='\0';
        CoinJam(temp,j);
    //Divisor(temp);
  } 
  return 0;
}

}