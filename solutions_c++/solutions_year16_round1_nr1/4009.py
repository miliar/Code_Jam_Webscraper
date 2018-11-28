#include<bits/stdc++.h>
using namespace std;

string findLastWord(string s, int start, int end){
	if(start>end){
		string t="\0";
		return t;
	}
	int i, maxIndex=-1;
	char maxChar=-1;
	string temp1, temp2, result;
	for(i=start;i<=end;i++){
		if(s[i]>=maxChar){
			maxChar=s[i];
			maxIndex=i;
		}
	}
	temp1=findLastWord(s,start,maxIndex-1);
	temp2=s.substr(maxIndex+1,end-maxIndex);
	result=maxChar+temp1+temp2;
	// cout<<temp1<<" "<<temp2<<" "<<result<<endl;
	return result;
}

int main(){
	int t;
	string s, result;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		cin>>s;
		result=findLastWord(s, 0, s.length()-1);
		printf("Case #%d: ",cas);
		cout<<result<<endl;
	}
	return 0;
}