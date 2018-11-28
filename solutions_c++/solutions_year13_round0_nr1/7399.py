#include<iostream>
#include<string>
using namespace std;
//X : 1
//O : 3
//T : 2
//. : 0

int check(int l1,int l2,int l3,int l4){
  if(l1==0 || l2==0 || l3==0 || l4==0)
    return 0;

  int sum = l1+l2+l3+l4;
  if(sum==4 || sum==5 || sum==11 || sum==12)
    return sum;

  return 0;
}

int solve(int **b){
  // -1 : draw
  // 0  : not complete
  int r;
  //check by row
  for(int j=0;j<4;++j){
    if((r=check(b[j][0],b[j][1],b[j][2],b[j][3]))>0)
      return r;
  }

  //check by col
  for(int k=0;k<4;++k){
    if((r=check(b[0][k],b[1][k],b[2][k],b[3][k]))>0)
      return r;
  }

  //check by diagonal
  if((r=check(b[0][0],b[1][1],b[2][2],b[3][3]))>0)
    return r;

  if((r=check(b[0][3],b[1][2],b[2][1],b[3][0]))>0)
    return r;


  for(int i=0;i<4;++i){
    for(int j=0;j<4;++j){
      if(b[i][j]==0)
	return 0;
    }
  }

  return -1;
}

int main(){
  int T;
  cin>>T;

  int **b = new int*[4];
  for(int i=0;i<4;++i)
    b[i] = new int[4];

  string str;
  for(int i=0;i<T;++i){

    for(int j=0;j<4;++j){
      cin>>str;
      for(int k=0;k<4;++k){
	if(str[k]=='X')
	  b[j][k] = 1;
	else if(str[k]=='O')
	  b[j][k] = 3;
	else if(str[k]=='T')
	  b[j][k] = 2;
	else
	  b[j][k] = 0;
      }
    }

    int s = solve(b);
    if(s==4 || s==5)
      cout<<"Case #"<<i+1<<": X won\n";
    else if(s==11 || s==12)
      cout<<"Case #"<<i+1<<": O won\n";
    else if(s == 0)
      cout<<"Case #"<<i+1<<": Game has not completed\n";
    else
      cout<<"Case #"<<i+1<<": Draw\n";
  }

  return 0;
}
