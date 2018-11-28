#include<iostream>
#include<vector>
using namespace std;

int main(){
  int T;
  cin>>T;
  vector<int> a(4), b(4);
  int case_count = 1;
  while(T--){
    int row;
    cin>>row;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        int temp;
        cin>>temp;
        if (i+1 != row) continue;
        a[j] = temp;
      }
    }

    cin>>row;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        int temp;
        cin>>temp;
        if (i+1 != row) continue;
        b[j] = temp;
      }
    }

    int common_element_count = 0;
    int ans;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
        if(a[i] == b[j]){
          ans = a[i];
          common_element_count++;
        }
      }
    }

    cout<<"Case #"<<case_count++<<": ";
    if (common_element_count == 1){
      cout<<ans<<endl;
    } else if (common_element_count > 0 ) {
      cout<<"Bad magician!"<<endl;
    } else {
      cout<<"Volunteer cheated!"<<endl;
    }

  }
  return 0;
}
