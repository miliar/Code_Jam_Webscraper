#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<queue>
#include<iomanip>

int main(){
  int probN;
  std::cin >> probN;
  for(int prob=1;prob<=probN;prob++){
    int t;
    std::cin >> t;
    std::vector<int> b(t);
    std::vector<std::pair<int,int> > a;
    for(int i=0;i<t;i++){
      std::cin >> b[i];
      a.push_back(std::make_pair(b[i],i));
    }
    std::sort(a.begin(),a.end());
    std::vector<int> l,r;
    int cnt=0;
    for(int i=0;i<a.size();i++){
      int p=a[i].first;
      if(a[i].second<a.size()/2){
        l.push_back(p);
        cnt+=a[i].second;
      }else{
        r.push_back(p);
        cnt+=a.size()-a[i].second-1;
      }            
      for(int j=0;j<a.size();j++){
        if(a[i].second < a[j].second)a[j].second--;
      }
      a.erase(a.begin()+i);
      i--;
    }
    std::cout << "Case #" << prob << ": ";
    std::cout << cnt << std::endl;
  }
  return 0;
}