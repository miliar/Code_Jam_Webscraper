#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ifstream i("B.txt");
	ofstream o;
	o.open("Bout.txt");
	
	int T, moves, j, flag;
	string s;
	i>>T;
	//cin>>T;
	for(int inc=0; inc<T; inc++){
		i>>s;
		//cin>>s;
		moves = 0;
		j = s.length()-1;
		while(s[j]=='+'){
			j--;
		}
		while(j>=0){
			
			flag = 0;
			while(s[j]=='-' && j>=0){
				j--;
				flag = 1;
			}
			if(flag ==1)
				moves++;
			while(s[j]=='+' && j>=0){
				j--;
				flag = 2;
			}
			if(flag==2)
				moves++;
		}
		//cout<<"Case #"<<inc+1<<": "<<moves<<endl;
		o<<"Case #"<<inc+1<<": "<<moves<<endl;
	}
	
	i.close();
	o.close();
	return 0;
}
