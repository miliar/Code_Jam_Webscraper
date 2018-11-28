#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main(){
int T;
cin>>T;

for(int i=0;i<T;++i){
int n;
cin>>n;
vector<int> mush(n);
for(int j=0;j<n;++j){
cin>>mush[j];
}
int e1=0,e2=0;
int m=0;
for(int j=0;j<n-1;++j) {
e1+=max(0,mush[j]-mush[j+1]);

m=max(m,mush[j]-mush[j+1]);
}
for(int j=0;j<n-1;++j){
e2+=min(mush[j],m);}
cout<<"Case #"<<i+1<<": "<<e1<<" "<<e2<<endl;
}


}
