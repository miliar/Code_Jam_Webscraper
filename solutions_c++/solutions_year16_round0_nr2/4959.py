#include <iostream>
using namespace std;


int main() {
    int t;
    cin>>t;
    for (int k=1;k<=t;k++){
    string s;
        int count=0;
        cin>>s;
        int p=s.size();
        for(int i=0;i<p-1;i++){
            if(s.at(i)=='-'&&s.at(i+1)=='+'){
                count++;
      }
            else if(s.at(i)=='+'&&s.at(i+1)=='-'){
                count++;
               }
        }
        if(s.at(p-1)=='-')
            cout<<"Case #"<<k<<": "<<count+1<<"\n";
        else
            cout<<"Case #"<<k<<": "<<count<<"\n";
    }
    return 0;
}