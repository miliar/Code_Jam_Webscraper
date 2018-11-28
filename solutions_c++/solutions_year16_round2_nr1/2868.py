#include<stdio.h>
#include<fstream>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
using namespace std;
vector<int> number;
map<char,int> nums;

void findNumber(string S){
 int len = S.length();
 int temp;
 for(int i=0; i<len; i++){
  if(nums[S[i]]>0){nums[S[i]]++;}
  else{nums[S[i]]=1;}
 }

 if(nums['Z']>0){
  temp = nums['Z'];
  if(nums['E']>=temp && nums['R']>=temp && nums['O']>=temp){
  nums['Z'] -= temp;
  nums['E'] -= temp;
  nums['R'] -= temp;
  nums['O'] -= temp;
  while(temp){
    number.push_back(0);
    temp--;
  }
 }
 }

 if(nums['X']>0){
  temp = nums['X'];
  if(nums['S']>=temp && nums['I']>=temp){
  nums['S'] -= temp;
  nums['I'] -= temp;
  nums['X'] -= temp;
  while(temp){
    number.push_back(6);
    temp--;
  }
 }
 }

 if(nums['W']>0){
  temp = nums['W'];
  if(nums['T']>=temp && nums['O']>=temp){
  nums['T'] -= temp;
  nums['W'] -= temp;
  nums['O'] -= temp;
  while(temp){
    number.push_back(2);
    temp--;
  }
 }
 }

 if(nums['U']>0){
  temp = nums['U'];
  if(nums['F']>=temp && nums['O']>=temp && nums['R']>=temp){
  nums['F'] -= temp;
  nums['O'] -= temp;
  nums['U'] -= temp;
  nums['R'] -= temp;
  while(temp){
    number.push_back(4);
    temp--;
  }
 }
 }

 if(nums['G']>0){
  temp = nums['G'];
  if(nums['E']>=temp && nums['I']>=temp && nums['T']>=temp && nums['H']>=temp){
  nums['E'] -= temp;
  nums['I'] -= temp;
  nums['G'] -= temp;
  nums['H'] -= temp;
  nums['T'] -= temp;
  while(temp){
    number.push_back(8);
    temp--;
  }
 }
 }

 if(nums['S']>0){
  temp = nums['S'];
  if(nums['E']>=(2*temp) && nums['V']>=temp && nums['N']>=temp){
  nums['S'] -= temp;
  nums['E'] -= temp;
  nums['V'] -= temp;
  nums['E'] -= temp;
  nums['N'] -= temp;
  while(temp){
    number.push_back(7);
    temp--;
  }
 }
 }

 if(nums['R']>0){
  temp = nums['R'];
  if(nums['T']>=temp && nums['H']>=temp && nums['E']>=(2*temp)){
  nums['T'] -= temp;
  nums['H'] -= temp;
  nums['R'] -= temp;
  nums['E'] -= temp;
  nums['E'] -= temp;
  while(temp){
    number.push_back(3);
    temp--;
  }
 }
 }

 if(nums['O']>0){
  temp = nums['O'];
  if(nums['N']>=temp && nums['E']>=temp){
  nums['O'] -= temp;
  nums['N'] -= temp;
  nums['E'] -= temp;
  while(temp){
    number.push_back(1);
    temp--;
  }
 }
 }

 if(nums['F']>0){
  temp = nums['F'];
  if(nums['V']>=temp && nums['I']>=temp && nums['E']>=temp){
  nums['F'] -= temp;
  nums['I'] -= temp;
  nums['V'] -= temp;
  nums['E'] -= temp;
  while(temp){
    number.push_back(5);
    temp--;
  }
 }
 }




 if(nums['I']>0){
  temp = nums['I'];
  if(nums['N']>=(2*temp) && nums['E']>=temp){
  nums['N'] -= temp;
  nums['I'] -= temp;
  nums['N'] -= temp;
  nums['E'] -= temp;
  while(temp){
    number.push_back(9);
    temp--;
  }
 }
 }


 sort(number.begin(), number.end());

}





int main(){
  ofstream result;
  result.open("a.txt");
  int T,N=0;
  scanf("%d",&T);
  string S;
  while(T--){
    cin>>S;
    findNumber(S);   

    result<<"case #"<<++N<<": ";
	for(int i=0; i<number.size(); i++){
		result<<number[i];
	}
	result<<endl;
	number.clear();
    //printf("%lld\n",A[target]);
  }
  return 0;
}


