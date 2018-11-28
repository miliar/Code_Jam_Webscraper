#include <iostream>
using namespace std;
enum result{
  X_WIN,
  O_WIN,
  DRAW,
  NOT_COMPLETE
};

class board{
private:
  
  char same_column(int i);
  char same_row(int i);
  char same_cross();
  bool has_empty();
public:
  int empty_cell;
  char B[4][4];
  char get_result();
};

char board::same_cross(){
  char result = 'U';
  if(B[0][0]=='.')
    return 'U';
  if(B[0][0]=='T'){
    if(B[1][1]==B[2][2] && B[3][3] == B[2][2]){
      return B[1][1];
    }
  }
  else{
    for(auto i=1;i<4;i++){
      if(B[i][i]==B[0][0] || B[i][i]=='T'){
	result = B[0][0];
      }
      else{
	result = 'U';
	break;
      }
    }
  }
  if(result!='U'){
    return result;
  }
  if(B[0][3]=='.')
    return 'U';
  if(B[0][3]=='T'){
    if(B[1][2]==B[2][1] && B[3][0] == B[2][1]){
      return B[2][1];
    }
  }
  else{
    for(auto i=1;i<4;i++){
      if(B[i][3-i]==B[0][3] || B[i][3-i]=='T'){
	result = B[0][3];
      }
      else{
	result = 'U';
	break;
      }
    }
  }
  return result;
}


bool board::has_empty(){
  if(empty_cell!=0){
    return true;
  }
  for(auto i=0; i< 4; i++){
    for(auto j=0; j< 4; j++){
      if(B[i][j]=='.'){
	return true;
      }
    }
  }
  return false;
}

char board::get_result(){
  bool has_empty = false;
  char result = same_cross();
  if(result!='U'){
    return result;
  }
  for(auto i=0; i< 4; i++){
    char result = same_row(i);
    if(result !='U'){
      return result;
    }
  }
  for(auto i=0; i< 4; i++){
    char result = same_column(i);
    if(result != 'U'){
      return result;
    }
  }
  return this->has_empty()?'U':'D';
}

char board::same_row(int i){
  if(B[i][0]=='.'){
    empty_cell = 1;
    return 'U';
  }
  if(B[i][0]=='T'){
    if(B[i][1]==B[i][2] && B[i][2]==B[i][3]){
      return B[i][1];
    }else{
      return 'U';
    }
  }
  else{
    for(auto j=1; j< 4; j++){
      if(B[i][j] == B[i][0] || B[i][j] == 'T'){
      }else{
	return 'U';
      }
    }
    return B[i][0];
  }
}

char board::same_column(int i){
  if(B[0][i]=='.'){
    empty_cell = 1;
    return 'U';
  }
  if(B[0][i]=='T'){
    if(B[1][i]==B[2][i] && B[2][i]==B[3][i]){
      return B[1][i];
    }else{
      return 'U';
    }
  }
  else{
    for(auto j=1; j< 4; j++){
      if(B[j][i] == B[0][i] || B[j][i] == 'T'){
      }else{
	return 'U';
      }
    }
    return B[0][i];
  }
}

int main(int argc, char** argv){
  int T;
  board b;
  cin>>T;
  for(auto i=0;i<T;i++){
    for(auto j=0;j<4;j++){
      for(auto k=0; k<4; k++){
	cin>>b.B[j][k];
      }
    }
    b.empty_cell = 0;
    char result = b.get_result();
    cout<<"Case #"<<i+1<<": ";
    switch(result){
    case 'X':
      cout<<"X won"<<endl;
      break;
    case 'O':
      cout<<"O won"<<endl;
      break;
    case 'D':
      cout<<"Draw"<<endl;
      break;
    case 'U':
      cout<<"Game has not completed"<<endl;
      break;
    default:
      cout<<"Illegal"<<endl;
      break;
    }
  }
  return 0;
}
