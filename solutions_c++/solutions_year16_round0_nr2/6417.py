#include<iostream>
#include<string>
using namespace std;
int main(){
	
	int c,j=1;
	cin >> c;
	while(c--)
	{
		string s;
		cin >> s;
		int mode = 0;
		int i = 0;
		int count = 0;
		while(s.size() >= i)
		{
			if(mode){
				if(s[(s.size()-i)-1] == '+'){
					count++;
					mode = 0;
				}	
			}else{
				if(s[(s.size()-i)-1] == '-'){
					count++;
					mode = 1;
				}			
			}
			i++;
		}
		cout <<"Case #" << j <<": "<< count << endl;
		j++;
	}	
	return 0;
}

