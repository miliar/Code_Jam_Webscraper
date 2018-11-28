#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int T;
  cin>>T;
  for(int case_count=1;case_count<=T;case_count++){
    vector<double> n,k;
    int N;
    cin>>N;
    for(int i=0;i<N;i++){
      double temp;
      cin>>temp;
      n.push_back(temp);
    }

    for(int i=0;i<N;i++){
      double temp;
      cin>>temp;
      k.push_back(temp);
    }

    sort(n.begin(), n.end());
    sort(k.begin(), k.end());

    /*    for(int i=0;i<N;i++){
      cout<<n[i]<<" ";
    }cout<<endl;


    for(int i=0;i<N;i++){
      cout<<k[i]<<" ";
    }cout<<endl;
    */

    int n_wins = 0;
    int b_index = 0;
    for(int i=0;i<N;i++){
      if ( k[i] < n[b_index]) {
        n_wins++;
        continue;
      }
      b_index++;
    }

    int n_wins_deceitful = N;
    b_index = 0;
    for(int i=0;i<N;i++){
      if (n[i] < k[b_index]){
        n_wins_deceitful -= 1;
        continue;
      }
      b_index++;
    }

    cout<<"Case #"<<case_count<<": "<<n_wins_deceitful<<" "<<n_wins<<endl;
  }
  return 0;
}
