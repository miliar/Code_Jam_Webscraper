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
    int x;
    std::cin >> t >> x;     
    std::vector<int> s(t);
    for(int i=0;i<t;i++)std::cin >> s[i];
    std::sort(s.begin(),s.end(),std::greater<int>());
    std::cout << "Case #" << prob << ": ";
    int cnt=0;
    for(int i=0;i<t;i++){
      if(s[i]!=-1){           
        int p=s[i];
        int maxf=-1;
        for(int j=0;j<t;j++){
          if(j!=i && s[j]!=-1 && s[j]+p<=x){
            if(maxf==-1 || s[maxf]<s[j])maxf=j;
          }
        }
        cnt++;
        if(maxf!=-1){
          s[i]=-1;
          s[maxf]=-1;
        }
      }
    }
    /* Output Here */
    std::cout << cnt << std::endl;
  }
  return 0;
}