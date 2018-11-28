#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
	int numOfTestCases;
	int number;
	vector<int> vNumber;
	map <char,int> mNum;
	cin >> numOfTestCases;
	while(numOfTestCases)
	{
		cin >> number;
		vNumber.push_back(number);
		--numOfTestCases;
	}
	
//	stringstream s;
	for ( auto i = vNumber.begin(); i != vNumber.end() ; ++i)
	{
		int x=*i;
        int n=1;
        int y = x;
		while ( 1 )
		{

            
            std::string s = std::to_string(y);
          // cout << s << endl;
            if (s == "0")
                {
                cout << "INSOMNIA" << endl;
                break;
            }
			for ( auto j = s.begin() ; j != s.end(); ++j)
			{
				mNum[*j]=1;
			}
			if (mNum.size() == 10 )
			{
				cout << y <<endl;
        		break;
              
          	}
            ++n;
			y=n*x;
		}
	
	}
	return 0;
}
