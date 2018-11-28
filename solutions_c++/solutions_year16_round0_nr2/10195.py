#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <stack>
#include <queue>

using namespace std;

stack<char> mystack;
queue<char> helper;
stack<char> changer;

int modifier(int kk){
	char temp1;
	int counter=mystack.size();
	int tries=0;
	while(!mystack.empty()){
    	temp1=mystack.top();
    	if(temp1=='-'){
    		break;
    	}
    	mystack.pop();
    	counter--;
    	changer.push(temp1);
    }
    if(counter==0){
    	return tries;
    }
    while(!changer.empty()){
    	temp1=changer.top();
    	changer.pop();
    	mystack.push(temp1);
    	counter++;
    }
	while (!mystack.empty()){
		char temp=mystack.top();
		mystack.pop();
		counter--;
		if(temp!='+' && temp!='-'){
			cout<<"Error:invalid input...\nExitting..."<<endl;
			exit(1);
		}
		helper.push(temp);
    	while(!mystack.empty() && temp==mystack.top()){
    		temp=mystack.top();
    		mystack.pop();
    		counter--;
    		helper.push(temp);
    	}
    	while(!helper.empty()){
    		temp=helper.front();
    		helper.pop();
    		if(temp=='-'){
    			mystack.push('+');
    			counter++;
    		}
    		else{
    			mystack.push('-');
    			counter++;
    		}
    	}
    	while(!mystack.empty()){
    		temp=mystack.top();
    		if(temp=='-'){
    			break;
    		}
    		mystack.pop();
    		counter--;
    		changer.push(temp);
    	}
    	if(counter!=0){
    		while(!changer.empty()){
    			temp=changer.top();
    			changer.pop();
    			mystack.push(temp);
    			counter++;
    		}
    	}
    	tries++;
	}
	return tries;
}

int main(){
	int t;
	int tries,counter=0;
	string s;
	string line;
	ifstream myfile("B-large.in");
	ofstream yourfile;
	yourfile.open("output-2.txt");
	if(myfile.is_open()){
		getline(myfile,line);
		t=stoi(line);
		if(t<1 || t>100){
			cout<<"Error:'T' is out of limits...\nExitting..."<<endl;
			exit(1);
		}
		while(getline(myfile,line)){
			counter++;
			while (!mystack.empty()){
    			mystack.pop();
			}
			while (!helper.empty()){
    			helper.pop();
			}
			while (!changer.empty()){
    			changer.pop();
			}			
			s=line;
			if(s.length()<1 || s.length()>100){
				cout<<"Error:'S' is out of limits...\nExitting..."<<endl;
				exit(1);
			}
			for(int i=s.length()-1;i>=0;i--){
				mystack.push(s[i]);
			}
			int kk=mystack.size();
			tries=modifier(kk);
			if(counter>t){
				cout<<"Error:test cases do not match the number specified...\nExitting..."<<endl;
				exit(1);
			}
			yourfile<<"Case #"<<counter<<": "<<to_string(tries)<<endl;
		}
		myfile.close();
		yourfile.close();
	}
	return 0;
}
