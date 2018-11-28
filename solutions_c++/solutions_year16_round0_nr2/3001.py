#include <iostream>
#include <stack>
#include <string>

using namespace std;

class PancakeStack{
public:
	PancakeStack(string& p){
		for (string::reverse_iterator rit=p.rbegin(); rit!=p.rend(); ++rit) 
			pancakes.push(*rit);
	}

	int solve(){
		int n = 0;
    while (flip()){
			++n;		
		}
		return n;
	}
	
protected:
	char flipPancake(char face){
		return face == '+' ? '-' : '+';
	}
	
	void moveTopPancake(stack<char>& destStack){
		destStack.push(pancakes.top());
		pancakes.pop();
	}
	// flips if needed
	bool flip(){
		stack<char> flippingPancakes;
		while (!pancakes.empty() && pancakes.top() == '+')
			moveTopPancake(flippingPancakes);

		while (!pancakes.empty() && pancakes.top() == '-')
			moveTopPancake(flippingPancakes);
	
		if (flippingPancakes.top() == '+')
			return false;	

		while (!flippingPancakes.empty()){
			pancakes.push(flipPancake(flippingPancakes.top()));
			flippingPancakes.pop();
		}

		return true;
	}

private:
	stack<char> pancakes;
};

int main(){
  int numCases, caseId = 1;
	string pancakeStackStr;
  cin >> numCases;
  while(cin >> pancakeStackStr){
		PancakeStack pancakeStack(pancakeStackStr);
		cout << "Case #"<< caseId++ << ": " 
				 << pancakeStack.solve() << "\n";
  }

	return 0;
}
