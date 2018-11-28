#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#define FILEIN "A-large.in"
#define FILEOUT "A-large.txt"
std::string find(std::string str,int index);
std::string digit[]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};

template <typename T>
  std::string NumberToString ( T Number )
  {
     std::ostringstream ss;
     ss << Number;
     return ss.str();
  }

int main(){
	freopen(FILEIN,"r",stdin);
	freopen(FILEOUT,"w",stdout);
	std::string S,next,ans,ori;
	int T,Case=1,count;
	scanf("%d",&T);
	getchar();
	while(T--){
		ans="";
		std::getline(std::cin,S);
		ori=S;
		for(int start=0;start<=9;start++){
			count=0;
			for(int i=start;count<=9;count++){
				next=find(S,i);
				if(S.compare(next)!=0){
					S=next;
					ans+=NumberToString(i);
					i--;
					count--;
				}
				if(S.empty()){
					break;
				}
				i++;
				if(i>9){
					i=0;
				}
			}
			if(S.empty()){
				break;
			}
			S=ori;
			ans="";
		}
		std::sort(ans.begin(),ans.end());
		printf("Case #%d: %s\n",Case++,ans.c_str());
	}
	return 0;
}

std::string find(std::string str,int index){
	std::string ori=str;
	int pos;
	for(int i=0;i<digit[index].size();i++){
		pos=str.find_first_of(digit[index].at(i));
		if(pos<0){
			return ori;
		}else{
			str.erase(str.begin()+pos);
		}
	}
	return str;
}