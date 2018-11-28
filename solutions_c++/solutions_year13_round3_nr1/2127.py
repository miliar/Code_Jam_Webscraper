#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <sstream>


using namespace std;

#define pb push_back

//g++ -o a.exe a.cpp
//./a.exe < A-small-practice.in > A-small-practice.out


int cases;

bool consec(string input,int lim){
	int count=0;
	for(int i=0;i<input.length();i++){
		if(input[i]!='\0'&&input[i]!='a'&&input[i]!='e'&&input[i]!='i'&&input[i]!='o'&&input[i]!='u'){
			count ++;
			if(count==lim){
				//cout<<input<<endl;
				return true;
			}
			
		}
		else{count=0;}
	}
	return false;
}


int main()
{
	string name,subst;
	int sublen,ans;
	cin>> cases;	
		//cout << "begin"<<endl;
		for(int caseno=1;caseno<=cases;caseno++)
		{
			cin>>name>>sublen;
			ans=0;
			
			for (int i=0;i<name.length();i++){
				for (int j=1;j<=name.length()-i;j++){
					
					
					
					if(consec(name.substr(i,j),sublen)){
						ans++;
						
					}
				}
			}
		
			
			
			
			cout <<"Case #"<< caseno<<": "<< ans << endl;
		}
	
	return 0;
}

