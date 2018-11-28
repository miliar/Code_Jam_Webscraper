#include<iostream>
#include<fstream>
#include<string>
#include <sstream>

using namespace std;

bool comp(string a){

	for(int i=0;i<a.length()/2;i++){

		if(a[i]!=a[a.length()-i-1])
			return 0;
	}
	return 1;

}
int myfunc2(int start, int end){

	int start1=sqrt(start);
	
	end =sqrt(end);
	int count=0;
	for(int i=start1;i<=end;i++){
		
		string str;

		stringstream convert; 

		convert << i;

		str= convert.str();
		//string rev;
		//rev = string ( str.rbegin(), str.rend() );
		if(comp(str)){
			string a;//string which will contain the result
		
		stringstream d; // stringstream used for the conversion
		int k=i*i;
		d << k;//add the value of Number to the characters in the stream

		a= d.str();//set Result to the content of the stream
		//string reve=a;
		//reve=string(a.rbegin(),a.rend());
		if(comp(a))
			count++;


		}


	}
	long float a=sqrt(start);
;

	long float b=start1;

	if(a!=b){
		string str;

		stringstream convert; 

		convert << start1;

		str= convert.str();
		//string rev;
		//rev = string ( str.rbegin(), str.rend() );
		if(comp(str)){
			string a;//string which will contain the result
		
		stringstream d; // stringstream used for the conversion
		int k=start1*start1;
		d << k;//add the value of Number to the characters in the stream

		a= d.str();//set Result to the content of the stream
		//string reve=a;
		//reve=string(a.rbegin(),a.rend());
		if(comp(a))
		count=count-1;
		}
	}
	return count;
}


int main (){

	fstream myfile;
	ofstream out;
	string number;
	myfile.open("input.txt");
	out.open("output.txt");
	if(myfile.is_open()){
		getline(myfile,number);
		int numb;
		stringstream a(number);
		a >> numb;
		
		for(int i=0;i<numb;i++){
			
			string a;
			

			getline(myfile,a);
			int g=a.length();
			int b=g;
			int start=0, end=0;
			for(g--;a[g]!=' ';g--){
				end=end+(a[g]-48)*pow(10,b-g-1);
			
			}
			b=g;
			for(g--;g>=0;g--)
				start=start+(a[g]-48)*pow(10,b-g-1);
			cout<<start<<endl;
			cout<<end<<endl;
			
			out<<"Case #"<<i+1<<": "<<myfunc2(start,end)<<endl;
		}

		out.close();
	}

	
	
}