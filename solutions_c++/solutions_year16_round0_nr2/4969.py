#include <iostream>
#include <string>
using namespace std;


int main() {
	
	int caseNum;
	string input; 
	cin>>caseNum;
	for(int i = 0; i<caseNum  ;i++)
		{
			cin>>input;
			int len = input.size();
			int ans = 0;
			char first = input[0];
			int trans = 0;
			for(int j = 1; j < len; j++)
				{
					
					if(input[j] != input[j-1])
						trans++;
				}
			if((first == '+' && ((trans & 1) == 0)) || 
					(first == '-' && (trans&1)))
					ans = trans;
			else
					ans = trans+1;
					
			cout<<"Case #"<<i+1<<":"<<" "<<ans<<endl;
		}
	// your code goes here
	return 0;
}