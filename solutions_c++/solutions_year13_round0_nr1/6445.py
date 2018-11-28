
#include <iostream>
#include <cstring>

using namespace std;

string check(string str0,string str1,string str2,string str3);
char checkcol(char str0,char str1,char str2,char str3);
char checkrow(string str);
char checkdiag(char str0,char str1,char str2,char str3);
char check_score(char str0,char str1,char str2,char str3);

int main(){
	int number_of_testcases;
	cin>>number_of_testcases;
	string testcase[number_of_testcases][4];
	string junk,result;
	for(int i=0;i<number_of_testcases;i++){
		for(int j=0;j<4;j++){
			cin>>testcase[i][j];
		}
	}
	for(int i=0;i<number_of_testcases;i++){
		result = check(testcase[i][0],testcase[i][1],testcase[i][2],testcase[i][3]);
		cout<<"Case "<<"#"<<i+1<<":"<<" "<<result<<endl;
	}
	return 0;
}

	
string check(string str0,string str1,string str2,string str3){
	char ind_result[10];
	string result="Null";
	int count_draw=0,count_g=0;
	for(int i=0;i<4;i++){
		ind_result[i]= checkcol(str0[i],str1[i],str2[i],str3[i]);
	}
	ind_result[4] = checkrow(str0);
	ind_result[5] = checkrow(str1);
	ind_result[6] = checkrow(str2);
	ind_result[7] = checkrow(str3);
	ind_result[8] = checkdiag(str0[0],str1[1],str2[2],str3[3]);
	ind_result[9] = checkdiag(str3[0],str2[1],str1[2],str0[3]);
	for(int i=0;i<10;i++){
		switch(ind_result[i]){
			case 'X' : 	result = "X won";
						break;
			case 'O' :  result = "O won";
						break;
			case 'D' :  count_draw++;
						break;
			case 'G' :  count_g++;
						break;
		}
		if(result != "Null"){
			break;
		}
	}
	if(count_draw  == 10){
		result = "Draw";
	}
	if(result == "Null" && count_g != 0){
		result = "Game has not completed";
	}
	return result;
}

char checkcol(char str0,char str1,char str2,char str3){
	return check_score(str0,str1,str2,str3);
}

char checkrow(string str){
	return check_score(str[0],str[1],str[2],str[3]);
}

char checkdiag(char str0,char str1,char str2,char str3){
	return check_score(str0,str1,str2,str3);
}

int count_ch(char ch,char ch0,char ch1,char ch2,char ch3){
	int count=0;
	if(ch0==ch){count++;}
	if(ch1==ch){count++;}
	if(ch2==ch){count++;}
	if(ch3==ch){count++;}
	return count;
}
	
char check_score(char str0,char str1,char str2,char str3){
	int count_x,count_t,count_o,count_dot;
	count_x =count_ch('X',str0,str1,str2,str3);
	count_t =count_ch('T',str0,str1,str2,str3);
	count_o =count_ch('O',str0,str1,str2,str3);
	count_dot =count_ch('.',str0,str1,str2,str3);
	if(count_x  == 4){
		return 'X';
	}else
	if(count_o == 4){
		return 'O';
	}else
	if(count_x == 3 && count_t == 1){
		return 'X';
	}else
	if(count_o == 3 && count_t == 1){
		return 'O';
	}else
	if(count_dot  == 0){
		return 'D';
	}
	else{
	return 'G';
	}
}
	
		
