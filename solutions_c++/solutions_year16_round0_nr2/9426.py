#include <iostream>
#include <string>

using namespace std;

string *str;

bool check(){
  int tam=str->length();
  for(int i=0;i<tam;i++){
    if(str->at(i)=='-'){
      return false;
    }
  }
  return true;
}

char flip(char a){
  if(a=='+')
    return '-';
  else
    return '+';
}

int group(){
  char m=str->at(0);
  for(int i=1;i<str->length();i++){
    if(str->at(i)!=m){
      return i;
    }
  }
  return str->length();
}

void flip_group(int end){
  string *copia = new string(str->c_str(),end);
  for(int i=0;i<end;i++){
    str->at(i)=flip(copia->at(end-1-i));
  }
}

int main(){
  int testCases=0,cas=0;
  int n,i,flips;
  char inp[100];

  str = new string();
  cin>>testCases;
  while(testCases>0){
    cas++;
    cout<<"Case #"<<cas<<": ";
    flips=0;

    cin>>inp;
    str=new string(inp);

    while(!check()){
      flip_group(group());
      flips++;
    }
    cout<<flips<<endl;

    testCases--;
  }
}
