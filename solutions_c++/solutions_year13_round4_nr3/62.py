#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int C=1;C<=T;C++){
    int n;
    scanf("%d",&n);
    vector<vector<int> > e(n);
    int A[2000];
    for(int i=0;i<n;i++){
      scanf("%d",A+i);
    }
    for(int i=0;i<n;i++){
      for(int j=0;j<i;j++){
	if(A[j]>=A[i]){
	  e[i].push_back(j);
	}
      }
      for(int j=i-1;j>=0;j--){
	if(A[j]+1==A[i]){
	  e[j].push_back(i);
	  break;
	}
      }
    }
    int B[2000];
    for(int i=0;i<n;i++){
      scanf("%d",B+i);
    }
    for(int i=n-1;i>=0;i--){
      for(int j=n-1;j>i;j--){
	if(B[j]>=B[i]){
	  e[i].push_back(j);
	}
      }
      for(int j=i+1;j<n;j++){
	if(B[j]+1==B[i]){
	  e[j].push_back(i);
	  break;
	}
      }
    }
    int D[2000]={0};
    for(int i=0;i<n;i++){
      for(int j=0;j<e[i].size();j++){
	D[e[i][j]]++;
      }
    }
    int N=0,X[2000]={0},c[2000]={0};
    priority_queue<int> Q;
    for(int i=0;i<n;i++){
      if(!D[i]){
	Q.push(-i);
      }
    }
    while(!Q.empty()){
      int i=-Q.top();
      Q.pop();
      X[i]=N;
      N++;
      for(int j=0;j<e[i].size();j++){
	int k=e[i][j];
	c[k]++;
	if(c[k]==D[k]){
	  Q.push(-k);
	}
      }
    }
    printf("Case #%d:",C);
    for(int i=0;i<n;i++){
      printf(" %d",X[i]+1);
    }
    putchar('\n');
  }
  return 0;
}
