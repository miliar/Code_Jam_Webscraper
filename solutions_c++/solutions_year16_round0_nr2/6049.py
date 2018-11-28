#include<iostream>
#include<fstream>
using namespace std;
static int caseNum;
void pancake(string s){
	int count=0,flag=0;
	ofstream outfile;
  	outfile.open("output.txt", std::ios_base::app);
  	int len = s.length();
  	for(int i=len-1;i>=0;i--){
  		if(s[i]=='+' && flag==0){
  			continue;
  		}
  		if(s[i]=='-' && flag==0){
  			count++;
  			flag=1;
  		}
  		if(s[i]=='+' && flag==1){
  			count++;
  			flag=0;
  		}
  		if(s[i]=='-' && flag==1){
  			continue;
  		}
  	}
  	outfile << "Case #"<<caseNum<<": "<<count << endl;
    outfile.close();
    return;
}
int main()
{
	int t;
	string s;
	ifstream myfile ("b.txt");
	if (myfile.is_open())
  	{
  		myfile >> t;
	    while(myfile>>s){
	    	caseNum++;
	   		pancake(s);
		}
		myfile.close();
  	}
	return 0;
}