#include <set>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main(){
  int nTestCases=0;
  scanf("%d",&nTestCases);
  for(int i=0;i<nTestCases;++i){
	int row1;
	int row2;
	int mat1[4][4],mat2[4][4];
	set<int> set1;
	vector<int> vec;
	scanf("%d",&row1);
	for(int j=0;j<4;++j){
	  for(int k=0;k<4;++k){
		scanf("%d",&mat1[j][k]);
	  }
	}
	scanf("%d",&row2);
	for(int j=0;j<4;++j){
	  for(int k=0;k<4;++k){
		scanf("%d",&mat2[j][k]);
	  }
	}
	for(int j=0;j<4;++j){
	  set1.insert(mat1[row1-1][j]);
	}
	for(int j=0;j<4;++j){
	  if(set1.find(mat2[row2-1][j])!=set1.end()){
		vec.push_back(mat2[row2-1][j]);
	  };
	}
	printf("Case #%d: ",i+1);
	char out[100];
	if(vec.size()==1){
	  sprintf(out,"%d\n",vec[0]);
	}
	if(vec.size() == 0){
	  sprintf(out,"Volunteer cheated!\n");
	}
	if(vec.size() > 1){
	  sprintf(out,"Bad magician!\n");
	}
	printf(out);
  }
  return 0;
}
