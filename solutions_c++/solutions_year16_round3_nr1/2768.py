#include<bits/stdc++.h>

using namespace std;

int main(){

  int T, cases = 1;
  cin>>T;

  while(T--){

    int party_num, sum = 0, party_qnt;
    multimap<int, char> parties;
    char cur_party = 'A';

    cin>>party_num;

    while(party_num--){
      cin>>party_qnt;
      
      parties.insert({party_qnt, cur_party});
      sum += party_qnt;
      cur_party++;
    }

    multimap<int,char>::iterator it;
    vector<char> res;
    cout<<"Case #"<<cases++<<":";
    while(!parties.empty()){
      it = parties.end();
      it--;
      int key = it->first;
      char val = it->second;
      
      parties.erase(it);
      key--;
      sum--;
      
      it = parties.end();
      it--;
      int keynd = it->first;
      char valnd = it->second;
      if(keynd > sum-keynd){
	parties.erase(it);
	keynd--;
	sum--;
	cout<<" "<<val<<valnd;
	if(sum > 0 && keynd > 0)
	  parties.insert({keynd, valnd});
      }
      else{
	cout<<" "<<val;
      }

      if(sum > 0 && key > 0)
	parties.insert({key, val});
      
    }

    cout<<endl;
    
  }


  return 0;
}
