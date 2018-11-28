#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int stoi(string s){
	int n=s.size();
	int result=0;
	int i;
	if(s[0]!='-'){
		i=0;
	}else{
		i=1;
	}
	for(i;i<n;++i){
		result=result*10+s[i]-'0';
	}
	if(s[0]=='-'){
		result=-result;
	}
	return result;
}

int last_num(int input_num){
	int a[10]={0,0,0,0,0,0,0,0,0,0};
	int table_sum=0;
	int cur_num=input_num;
	int multiply_count=2;
	if(input_num==0){
		return 0;
	}
	while(table_sum<10){
		int tmp_num=cur_num;
		while(tmp_num!=0){
			if(a[tmp_num%10]==0){
				++table_sum;
				a[tmp_num%10]=1;
			}
			tmp_num=tmp_num/10;
		}
		cur_num=input_num*multiply_count;
		++multiply_count;
	}
	return input_num*(multiply_count-2);
}

int main () {
  string line;
  ifstream myfile ("A-large.in");
  ofstream result_file;
  result_file.open("q1_result_large.txt");
  if (myfile.is_open())
  {
  	getline(myfile,line);
  	int t=stoi(line);
    for(int i=0;i<t;++i){
	  getline (myfile,line);
      int cur_num=stoi(line);
      int neg_sign=0;
      if(cur_num<0){
      	cur_num=-cur_num;
      	neg_sign=1;
	  }
      int case_result=last_num(cur_num);
      if(neg_sign){
      	case_result=-case_result;
	  }
      if(case_result==0){
	    result_file<<"Case #"<<i+1<<": "<<"INSOMNIA\n";
  	  }else{
  	  	result_file<<"Case #"<<i+1<<": "<<case_result<<"\n";
      }
    }
    myfile.close();
    result_file.close();
  }
  return 0;
}
