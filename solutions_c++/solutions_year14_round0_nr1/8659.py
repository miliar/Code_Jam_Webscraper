#include<iostream>
using namespace std;
int main(){
  int t,m,n,a[4][4],c[4][4],l=1,k;
  cin>>t;
  int count,ans1;
  while(l<=t){
    cin>>m;
m--;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        cin>>a[i][j];
	 }
    }
 cin>>n;
n--;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        cin>>c[i][j];
	 }
    }
    count =0;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        if(c[n][i] == a[m][j]){
          count++;
	  ans1 = c[n][i];
	}
      }
    }
//cout<<count<<" "<<ans1<<endl;
    if(count ==1){
      cout<<"Case #"<<l<<": "<<ans1<<endl;
     }
    else{
      if(count > 1 ){
        cout<<"Case #"<<l<<": Bad magician!"<<endl;
      }
      else{
        cout<<"Case #"<<l<<": Volunteer cheated!"<<endl;
      }
    }

l++;
  }
  return 0;
}
