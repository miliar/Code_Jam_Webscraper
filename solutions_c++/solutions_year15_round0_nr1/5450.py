#include<iostream>
#include<vector>
using namespace std;

int main(){
  int T;
  int t=0;

  cin >> T;
  //cout << T << endl;
  while(t < T){
    int s_max;
    //char si;
    vector<int> shyness;    
    int all=0;
    int stand=0;    
    int invite=0;

    cin >> s_max;
    for(int i=0; i<=s_max; i++){
      char si;
      cin >> si;
      all += int(si-'0');
      shyness.push_back(int(si-'0'));
    }
    
    for(int i=0; i<shyness.size(); i++){            
      if(stand < i && shyness[i] != 0){
	invite += i - stand; stand += invite;
      }
      if(stand+invite >= i) stand += shyness[i];
      //cout << i << ":" <<stand << "," << invite << endl;
    }
    cout << "Case #"  << t+1 << ": " << invite << endl;;

    //cout << "stand:" << stand << endl;
	

    // cout << s_max << "," << all << "," << stand << " ";
    // for(int i=0; i<=s_max; i++)
    //   cout << shyness[i];
    // cout << endl;  
    t++;
  }
}  
