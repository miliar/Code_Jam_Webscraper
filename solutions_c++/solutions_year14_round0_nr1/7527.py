#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i=0;i<T;i++){
    int a;
    cin >> a;
    vector<vector <int> > board;
    board.resize(4);
    vector<int> choosen;
    choosen.resize(4);
    for(int j=0;j<4;j++){
      board[j].resize(4);
    }
    for(int j=0;j<4;j++){
      for(int k=0;k<4;k++){
	cin>>board[j][k];
      }
      if(j+1==a){
	for(int k=0;k<4;k++){
	  choosen[k]=board[j][k];
	}
      }
    }
    cin >> a;
    for(int j=0;j<4;j++){
      for(int k=0;k<4;k++){
	cin >>board[j][k];
      }
      if(j+1==a){
	int n=0;
	int c;
	for(int k=0;k<4;k++){
	  for(int q=0;q<4;q++){
	    if(choosen[q]==board[j][k]){
	      n+=1;
	      c=choosen[q];
	    }
	  }
	}
	if(n==1){
	  printf("Case #%d: %d",i+1,c);
	  cout << '\n';
	}
	if(n==0){
	  printf("Case #%d: Volunteer cheated!",i+1);
	  cout << '\n';
	}
	if(n>1){
	  printf("Case #%d: Bad magician!",i+1);
	  cout << '\n';
	}
      }
    }
  }
  return 0;
}
	  