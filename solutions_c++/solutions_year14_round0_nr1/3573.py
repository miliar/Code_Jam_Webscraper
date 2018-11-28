#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
  int t,i,j,p,q,a[4],b[4],temp;
  vector<int> v;
  cin >> t;
  int c = 1;
  while(t--){
    v.clear();
    cin>>p;
    for(i=1;i<=4;i++){
      if(i!=p){
	for(j=1;j<=4;j++){
	  cin>>temp;
	}
      }
      else{
	for(j=0;j<4;j++){
	  cin>>a[j];
	}
      }
    }
    sort(a,a+4);
    cin>>q;
    for(i=1;i<=4;i++){
      if(i!=q){
	for(j=1;j<=4;j++){
	  cin>>temp;
	}
      }
      else{
	for(j=0;j<4;j++){
	  cin>>b[j];
	}
      }
    }
    for(i=0;i<4;i++){
      if(binary_search(a,a+4,b[i])){
	v.push_back(b[i]);
      }
    }
    cout<<"Case #"<<c<<": ";
    if(v.size()==0){
      cout<<"Volunteer cheated!"<<endl;
    }
    else{
      if(v.size()==1){
	cout<<v[0]<<endl;
      }
      else{
	cout<<"Bad magician!"<<endl;
      }
    }
    c++;
  }
  return 0;
}