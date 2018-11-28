#include<iostream>
#include<cstdio>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
using namespace std;

vector<int> getInp(int pick){
  vector<int> ret;
  int inp;
  for(int i=1;i<=4;i++){
    for(int k=1;k<=4;k++){
      scanf("%d",&inp);
      if(i==pick)ret.push_back(inp);
    }
  }
  return ret;
}
int main(){
  int tc;
  scanf("%d",&tc);
  for(int tcc=1;tcc<=tc;tcc++){
    printf("Case #%d: ",tcc);
    vector<int> try1,try2,intersection;
    int pick,inp;
    scanf("%d",&pick); try1=getInp(pick);
    scanf("%d",&pick); try2=getInp(pick);
    sort(try1.begin(),try1.end()); sort(try2.begin(),try2.end());
    set_intersection(try1.begin(),try1.end(),try2.begin(),try2.end(),back_inserter(intersection));
    if(intersection.size()==1)
      printf("%d\n",intersection[0]);
    else if(intersection.size()==0)
      printf("Volunteer cheated!\n");
    else
      printf("Bad magician!\n");
  }
  return 0;
}
