#include <iostream>
#include <string>
#include <math.h>
#include <list>
#include <cctype>
#include <stdio.h>
using namespace std;

string calculate(string str){
	int len=str.length();
	int number=pow(2,len-1);
	string wordlist[number];
	string returnstr="";
  	std::list<std::string> mylist;
	std::list<std::string>::iterator it;
	if(len==0){
		return "";	
	}else if(len==1){
		return str;
	}else{
		
		for(int i=0;i<len;i++){
			char lastchar=str[i];
			int count=pow(2,i);
			if(count==1){
				wordlist[0]=lastchar;
			}else{
				for(int j=0;j<count/2;j++){
					string prev=wordlist[j];
					if(prev.length()==0){
						wordlist[j]=lastchar;
					}else{
						string pre=lastchar+prev;
						string post=prev+lastchar;
						//cout << prev << ":" << pre << ":" << post << endl;
						wordlist[j]=pre;
						wordlist[j+(count/2)]=post;
					}
				}
			}
		}
		for(int i=0;i<number;i++){
			mylist.push_back(wordlist[i]);
		}
		mylist.sort();
		for (it=mylist.begin(); it!=mylist.end(); ++it){
		    returnstr= *it;
		}		
	}
	return returnstr;
}


int main()
{

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

    	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
	        string str;
	        cin >> str;
		string result=calculate(str);
		cout << "Case #" << i << ": "<< result << endl;

	}


    return 0;
}
