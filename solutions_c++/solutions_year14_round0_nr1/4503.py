#include<iostream>
#include<string>
using namespace std;

int first_card[4][4],second_card[4][4];

string hoge_itoa(int data){
	
	string result;
	for(;data>0;data/=10)
		result=((char)(data%10+'0'))+result;
	return result;
}


string solve(int first_ans,int second_ans){
	int count=0,chose_card=0;
	
	for(int fi=0;fi<4;fi++)
		for(int si=0;si<4;si++)
			if(first_card[first_ans-1][fi]==second_card[second_ans-1][si])
			{
				count++;
				chose_card=first_card[first_ans-1][fi];
			}
	
	string result=hoge_itoa(chose_card);
	
	if(count==0)
		return "Volunteer cheated!";
	else if(count>1)
		return "Bad magician!";
	return result;
}


int main(){
	int T;
	int first_ans,second_ans;
	
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		cin>>first_ans;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>first_card[i][j];
		cin>>second_ans;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>second_card[i][j];
		
		string program_answer=solve(first_ans,second_ans);
		
		cout<<"Case #"<<testcase<<": "<<program_answer<<endl;
	}
	
	return 0;
}
