#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <unordered_set>

using namespace std;

void sheep(int);

void sheep(int n){
    
    unsigned long long last_number = n;
    unsigned long long tmp = n;
    unordered_set <int> s;
    if (n == 0){
        cout<<"INSOMNIA"<<endl;
        return;
    }
    int i = 1;
    while (true){
        if (s.size() == 10)
            break;
        last_number = i*n;
       // cout<<last_number<<endl;
        tmp = last_number;
        while (tmp > 0){
            int digit = tmp % 10;
            s.insert(digit);
            tmp = tmp/10;
        }
        ++i;
    }
    

    cout<<last_number<<endl;
}

int main(){
  //  int n;
    //cin>>n;
    //sheep(n);
    int n;
    int input;
    istringstream ss;
    string  s;
    getline(cin,s);
    ss.str(s);
    ss>>n;
    ss.clear();
    string length;
    //cerr<<n<<endl;
    for (int i=0;i<n;++i){
       // int v;
      //  vector <int> x;
        //cerr<<x.size()<<endl;
        //vector <int> y;
        getline(cin,s);
        ss.str(s);
        ss>>input;
        //cout<<input<<endl;
        ss.clear();
        
        cout<<"Case #"<<i+1<<": ";
        sheep(input);
        
 
    
    }
    
}