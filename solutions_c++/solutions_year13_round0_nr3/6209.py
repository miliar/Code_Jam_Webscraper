#include<iostream>
#include<fstream>
using namespace std;
int t,a,b,ans;
int main(){
    ifstream cin("C-small-attempt0.in");
    ofstream cout("output11.txt");
    cin>>t;
    for(int fd = 0; fd  < t; fd++){
            cin>>a>>b;
            if(a <= 1 && b >= 1) ans++;
            if(a <= 4 && b >= 4) ans++;
            if(a <= 9 && b >= 9) ans++;
            if(a <= 121 && b >= 121) ans++;
            if(a <= 484 && b >= 484) ans++;
            cout<<"Case #"<<fd+1<<": "<<ans<<endl;
            ans=0;
    }
  return 0;
}

