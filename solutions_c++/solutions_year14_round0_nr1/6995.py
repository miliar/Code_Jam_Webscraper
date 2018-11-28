#include <iostream>
#include <cstdio>
using namespace std;
int main(){
  int tt;
  cin>>tt;
  for(int test_case=1;test_case<=tt;test_case++){
    int first_ans,second_ans;
    cin>>first_ans;
    int first_arrange[4][4],second_arrange[4][4];
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	cin>>first_arrange[i][j];
      }
    }
    cin>>second_ans;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	cin>>second_arrange[i][j];
      }
    }
    int matched=0,matched_val;
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	if((first_arrange[first_ans-1][i])==(second_arrange[second_ans-1][j])){
	  matched++;
	  matched_val = first_arrange[first_ans-1][i];
	}
      }
    }
    if(matched==1){
      printf("Case #%d: %d\n",test_case,matched_val);
    }else if(matched>1){
      printf("Case #%d: Bad magician!\n",test_case);
    }else{
      printf("Case #%d: Volunteer cheated!\n",test_case);
    }
  }
  return 0;
}
