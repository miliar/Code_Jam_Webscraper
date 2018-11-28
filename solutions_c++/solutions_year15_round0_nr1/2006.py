#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
int T;
cin>>T;
for(int i=0;i<T;++i){
int n;
cin>>n;
string s;
cin>>s;
int X=0,Y=0;
for(int j=0;j<=n;++j){
if(X<j){Y+=j-X; X=j;}
X+=int(s[j])-48;
}
cout<<"Case #"<<i+1<<": "<<Y<<endl;


}

}
