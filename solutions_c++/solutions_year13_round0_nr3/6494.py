#include <iostream>
#include <string>
#include <string.h>
#include <fstream>

using namespace std;
bool is_palindrome(string s){
	string temp;
	int j =0 ;
	for(int i=0,j=s.length()-1;i<s.length();i++,j--){
		temp += s[j];
	}
	return temp == s? true:false;
}

void main(){
	string s;
	string si[1000];
	char temp[100];
	string first;
	string last;
	FILE *pfile=0;
	string output;
	int k=0;
	//pfile=fopen("D:\data.in.txt","r");
	//	while((fgets(temp,99,pfile))!=NULL)//reading from file
	//	{
	//		if(temp[0]!=10)//writig the arrays without enter
	//		{
	//			si[k] = temp;
	//			k++;
	//		}
	//	}
	//	fclose(pfile);
	fstream data_file("E:\data.in.txt", fstream::in);
	while (data_file.good())
				{
    
				getline(data_file,si[k]);
				
				k++;
	}
	int i=0;
	int counter =0;
	for(int h=1;h<=atoi(si[0].c_str());h++){
		s = si[h];
		while((s[i] != ' ')){
			first += s[i] ;
			i++;
		}
		i++;
		while(i <s.length()){
			last += s[i];
			i++;
		}
		for(int j=atoi(first.c_str());j<=(atoi(last.c_str()));j++){
			itoa(j,temp,10);
			string s1 = temp;
			double t = sqrt(j);
			itoa(t == floor(t)? floor(t):133,temp,10);
			string ss = temp;
			if(is_palindrome(ss)&&is_palindrome(s1)){
			counter++;
			}
		}
		
		//output += "case#"+h+':'+counter+'/n';
		output += ("Case #"+to_string(h)+": "+to_string(counter)+"\n");
		
		
		i=0;
		counter = 0;
		first = "";
		last = "";
	}
	fstream data_file1("E:\data.out.txt", fstream::out);
	data_file1 <<output;
	cout <<output;
	system("pause"); 
}