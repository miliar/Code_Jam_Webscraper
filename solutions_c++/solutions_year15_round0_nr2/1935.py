#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){
int T;
cin>>T;
for(int i=0;i<T;++i){
int n;
cin>>n;
vector<int> v(n);
//cout<<n<<endl;
for(int j=0;j<n;++j){
cin>>v[j];
}
sort(v.rbegin(),v.rend());
int s=v[0];
//cout<<"***************"<<endl<<s<<endl;
int minTime=v[0];
while (s>1){
int x=0;
for(int j=0;j<n;++j) x+=(v[j]-1)/s;
x+=s;
minTime=min(minTime,x);
//cout<<"s"<<s<<"minTime"<<minTime<<endl;
--s;
}

cout<<"Case #"<<i+1<<": "<<minTime<<endl;


}

}
