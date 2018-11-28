#include<bits/stdc++.h>

using namespace std;

int main(){
  int t,_index=0;


 int a,b,c,d,e,f,g,h;








  cin>>t;
  while(t--){
    int n,m,c;
    int digit_comp[10] = {0};
    bool torun = false;
    int count = 0;
    int mul = 1;
    cin>>n;














    if(n == 0){
      torun = true;
    }
    while(!torun){

      if(count == 10) {
        torun = true;
        break;
      }
      m = n * mul;
      c = m;

    //  cout<<"m: "<<m<<endl;

      while(m>0){
        int digit = m % 10;
        //if digit is zero make it 1 in increase count
      //  cout<<"Digit O :"<<digit<<endl;
        if (!digit_comp[digit]){
        //  cout<<"Digit :"<<digit<<endl;
          digit_comp[digit] = 1;
          count++;
        }
        m /= 10;
      }





   //////////this is the code
//this is the level











      mul++;
    }
    // cout<<"count :"<<count<<"->"<<endl;
    // cout<<"Number :"<<n<<" Last Number : "<<c<<endl;
    //
    if(count < 10){
      cout<<"Case #"<<(++_index)<<": INSOMNIA"<<endl;
    }else{
      cout<<"Case #"<<(++_index)<<": "<<c<<endl;
    }
  }
}
