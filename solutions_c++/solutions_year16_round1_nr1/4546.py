#include<cstdio> 
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;
bool cp (string i,string j) { return (i>j);}
int main(){
	//A-small-attempt0.in
	freopen("A-small-attempt0.out","w",stdout);
	string str,str2;
	int Case;
	scanf("%d",&Case)	;
	for(int i=0;i<Case;i++){
		cin>>str;
		str2=str[0];
		for(int j=1;j<str.size();j++){
			if(str[j]>=str2[0]){
				str2=str[j]+str2;
			}else{
				str2=str2+str[j];
			}
		}
		printf("Case #%d: %s\n",i+1,str2.c_str());
		
	} 
	
	
	
	
	return 0;
}
