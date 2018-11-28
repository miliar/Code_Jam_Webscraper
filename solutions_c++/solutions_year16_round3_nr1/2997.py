#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
  int t,n,i,j,n2;
  scanf("%d",&t);
  vector< pair<int,int> > inp;
  vector< pair<int,int> >::iterator it1,it2;
  for(int zz=1;zz<=t;zz++){
    n2=0;
    printf("Case #%d: ",zz);
    scanf("%d",&n);
    for(i=0;i<n;i++){
      scanf("%d",&j);
      inp.push_back(make_pair(j,i));
      n2+=j;
    }
    //cout<<inp['A'];
    //n2=n;
    for(i=n2;i>0;i--){
      sort(inp.begin(),inp.end());
      reverse(inp.begin(),inp.end());
      it2=inp.begin();
      it1=it2;
      it2++;
      //cout<<it1->first<<" "<<it1->second<<endl;
      if((float)it2->first/(i-2)<0.5){
        printf("%c%c ",it1->second+65,it1->second+65);
        it1->first--;
        it1->first--;
        i--;
        continue;
      }
      if((float)it2->first/(i-1)>0.5){
        printf("%c%c ",it1->second+65,it2->second+65);
        it1->first--;
        it2->first--;
        i--;
      }
      else{
        printf("%c ",it1->second+65);
        it1->first--;;
      }
    }
    printf("\n");
    inp.clear();
  }
  return 0;
}
