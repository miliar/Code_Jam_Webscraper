#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <conio.h>

using namespace std;


int inOrder (string stack){
	int inOrder = 1;
	for (int q=0; q<stack.size(); q++){
		if (stack[q] == '-')
			inOrder = 0;
	}
	return inOrder;
}


int revOrder (string stack){
	int revOrder = 1;
	for (int q=0; q<stack.size(); q++){
		if(stack[q] == '+')
			revOrder = 0;
	}
	return revOrder;

}


int noFlips(string stack)
{
	//cout << stack<<endl;
	
	if (inOrder(stack))
		return 0;
	if (revOrder(stack))
		return 1;

	
	int ans = 10000000;
	int N = stack.size();
	//cout<<"size"<<N<<endl;
	for (int i=1; i<=N-1; i++){
		int flips; 
		
		string top = stack.substr(0, i);
		string bot = stack.substr(i, string::npos);
		if (inOrder(bot) == 1) {
			flips = noFlips(top);
		}
		else {
			std::reverse(bot.begin(), bot.end());
			flips = noFlips(top) + noFlips(bot) + 1;
					
			
		}
		
		if (flips < ans)
			ans = flips;
	}
	return ans;	
	
	
	//getch();
	
}


int main ()
{
	
	std::ifstream fin("B_small.txt", std::ifstream::in);
	std::ofstream fout("B_small_out.txt", std::ifstream::out);
	
	int no_tc;
	fin >> no_tc;
	
	for (int tc=1; tc<=no_tc; tc++){
		string stack;
		fin >> stack;
		
		int ans = noFlips(stack);
		fout << "Case #"<<tc<<": "<<ans<<endl;
			
	}
	
	return 0;
	
}
