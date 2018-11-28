#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
#include<set>
#include<deque>
#include<iterator>

using namespace std;

const int MAX = 1000;
int number;
int words_number;
char* word;
char sign;
int len;
vector<char> signs[MAX];
vector<int> lengths[MAX];
set<char> words_signs;
set<unsigned int> all_lengths;
unsigned int size;

bool check(){
  for(int i=0; i<words_number; ++i){
    all_lengths.insert(signs[i].size());
  }
  if(all_lengths.size() > 1){
    return false;
  }  
  else{
    size = *(all_lengths.begin());
    for(int i=0; i<size; ++i){
      for(int j=0; j<words_number; ++j){
	words_signs.insert(signs[j][i]);
      }
      if(words_signs.size() > 1){
	return false;
      }
      words_signs.clear();
    }
    return true;
  }
}

void clear(){
  for(int i=0; i<MAX; ++i){
    signs[i].clear();
    lengths[i].clear();
    all_lengths.clear();    
  }
  words_signs.clear();
}

int calculateColumn(int col){
  set<int> col_lengths;
  set<int>::iterator iter;
  int result = 0;
  for(int i=0; i<words_number; ++i){
    col_lengths.insert(lengths[i][col]);
  }
  unsigned int shift = col_lengths.size()/2;
  iter = col_lengths.begin();
  for(int i=0; i<shift; ++i){
    iter++;
  }
  int middle = *iter;
  for(iter=col_lengths.begin(); iter!=col_lengths.end(); ++iter){
    result += abs(*iter-middle);
  }
  return result;
}

int calculate(){
  int result = 0;
  for(int i=0; i<size; ++i){
    int column_result = calculateColumn(i);
    result += column_result;
  }
  return result;
}

void run(){
  scanf("%d", &words_number);
  for(int i=0; i<words_number; ++i){
    word = (char*)malloc(MAX*sizeof(char));
    scanf("%s", word);
    sign = word[0];
    signs[i].push_back(sign);
    len = 1;
    for(int j=1; j<strlen(word); j++){
      if(word[j] == sign){
	len++;
      }
      else{
	lengths[i].push_back(len);
	len = 1;
	sign = word[j];
	signs[i].push_back(sign);
      }
    }
    lengths[i].push_back(len);
  }
  if(check()){
    int result = calculate();
    printf("%d", result);
  }
  else{
    printf("Fegla Won");
  }
  clear();
}

int main(){
  scanf("%d", &number);
  for(int i=1; i<=number; ++i){
    printf("Case #%d: ", i);
    run();
    printf("\n");
  }
  return 0;
}
