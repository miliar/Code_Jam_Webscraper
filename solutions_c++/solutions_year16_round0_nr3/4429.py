#include<iostream>
#include<iomanip>
#include<sstream>
#include<vector>
#include<math.h>

using namespace std;

long long int whether_prime(unsigned long long int num){

	if(num%2==0){
		return 2;
	}

	unsigned long long int half=3;



    while(half<=sqrt(num)){
    	if(num%half==0){
    		return half;
    	}

    	half=half+2;
    }

    return -1;

}

void string_factory(vector<string>* record, int length){

	string s="1";

		for(int i=1; i<length-1; ++i){//the string without ending "1"
			s=s+'0';
		}
		s=s+'1';
		(*record).push_back(s);

		s="1";
		int count=1;
		int pos=1;


		while(count<=length-2){

			while(pos+count<=length-1){

		for(int i=1;i<pos;++i){
			s=s+'0';
		}

			for(int j=0;j<count;++j){
				s=s+'1';
			}

			for(int p=pos+count; p<length-1; ++p){
			s=s+'0';
		}

		s=s+'1';
		(*record).push_back(s);

		s="1";
		++pos;
			}

		s="1";
		++count;
		pos=1;

		}

}


unsigned long long int power(int base, int p){
	 unsigned long long int num=1;

	for(int i=0; i<p; ++i){
		num=num*base;
	}

	return num;
}



void num_factory(string s, int length, vector< unsigned long long int>* num){
	 unsigned long long int number=0;
	 unsigned long long int reg;

	for(int i=2; i<=10; ++i){
		for(int j=0; j<=length-1; ++j){
			int offset=s[j]-'0';
//			cout<<"offset:"<<offset<<endl;

			reg=power(i, length-1-j)*offset;
			number=number+reg;
		}

		(*num).push_back(number);
		number=0;
	}


}


bool jamcoin(string s, int length, vector< unsigned long long int>* record){

	 vector< unsigned long long int> nums;//record base from 2 to 10
	 num_factory(s, length, &nums);

	 vector< unsigned long long int> divisor;

	 for (vector< unsigned long long int>::iterator it=nums.begin(); it!=nums.end(); ++it){

//		 cout<<"num:"<<*it<<endl;
		 long long int i=whether_prime(*it);
		 if(i==-1){
			 return false;//has a prime
		 }else{
			 divisor.push_back(i);
		 }
	 			 }

	 unsigned long long int reg;

	 istringstream ss(s);
	 ss>>reg;

	 (*record).push_back(reg);

	 for (vector< unsigned long long int>::iterator it=divisor.begin(); it!=divisor.end(); ++it){
		 (*record).push_back(*it);
	 }

	return true;
}




int main(){
	int totalcase;
	cin>>totalcase;


	int length;
	int total_num;
	int count=0;


	int case_num=1;
//	vector<string> record_string;
//	vector<int> record_result;


	for(int i=1; i<=totalcase; ++i){
		cin>>length;
		cin>>total_num;
		vector<string> record_string;
		vector< unsigned long long int> record_result;

		string_factory(&record_string, length);
		int pos=0;

	/*	 for (vector<string>::iterator it=record_string.begin(); it!=record_string.end(); ++it){
			 cout<<pos<<": "<<*it<<endl;
			 ++pos;
		 }*/

	 while(count < total_num){
		string s=record_string.at(pos);

		//cout<<"s:"<<s<<endl;
		bool value=jamcoin(s, length, &record_result);

		//cout<<"value:"<<value<<endl;
		if(value==true){
			++count;
		}

		++pos;
	 }

	 count=0;

	 int posi=0;
	 cout<<"Case #"<<i<<":"<<endl;
	 for (vector< unsigned long long int>::iterator it=record_result.begin(); it!=record_result.end(); ++it){
		 		//cout<<record_result.at(posi);
		 		++posi;

			 cout<<*it;

		 		if(posi%10==0){
		 			cout<<endl;
		 		}else{
		 			cout<<" ";
		 		}

		 	 }




	}


//		bool value=jamcoin("1001", 4, &record_result);



//	 for(int i=1;i<=totalcase;++i){
//		 cout<<"Case #"<<i<<":"<<endl;

/*
	 for (vector<int>::iterator it=record_result.begin(); it!=record_result.end(); ++it){
	 		//cout<<record_result.at(posi);
	 		++posi;

		 cout<<*it;

	 		if(posi%10==0){
	 			cout<<endl;
	 		}else{
	 			cout<<" ";
	 		}

	 	 }*/

//	 }


}
