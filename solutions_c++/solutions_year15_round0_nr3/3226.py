#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <utility>
#include <stack>
#include <queue>
using namespace std;


#define TEST


int main()
{

	freopen("C-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	std::map<std::pair<char,char>, string> myMap;

	//myMap[std::make_pair(10,20)] = 25;
	//std::cout << myMap[std::make_pair(10,20)] << std::endl;

	myMap[make_pair('1','1')] = "1";
	myMap[make_pair('1','i')] = "i";
	myMap[make_pair('1','j')] = "j";
	myMap[make_pair('1','k')] = "k";
	
	myMap[make_pair('i','1')] = "1";
	myMap[make_pair('i','i')] = "-1";
	myMap[make_pair('i','j')] = "k";
	myMap[make_pair('i','k')] = "-j";
	
	myMap[make_pair('j','1')] = "j";
	myMap[make_pair('j','i')] = "-k";
	myMap[make_pair('j','j')] = "-1";
	myMap[make_pair('j','k')] = "i";

	myMap[make_pair('k','1')] = "k";
	myMap[make_pair('k','i')] = "j";
	myMap[make_pair('k','j')] = "-i";
	myMap[make_pair('k','k')] = "-1";



	long long T,L,X; //L characters X times
	cin>>T;
	int t = 0;

	
	while (t++ < T)
	{
		cin>>L>>X;
		bool isNegative = false;
		queue<char> stack;
		string str;
		cin>>str;
		for (int i = 0; i < X; i++)
		{
			for (int j = 0; j < L; j++)
			{
				char c = str[j];
				stack.push(c);
			}
		}
		

		if (L * X < 3)
		{
			cout<<"Case #"<<t<<": NO"<<endl;
			continue;
		}
		else if(L * X == 3)
		{
			if (str[0] != 'i' || str[1] != 'j' || str[2] != 'k')
			{
				cout<<"Case #"<<t<<": NO"<<endl;
				continue;
			}
		}


		bool iFound = false,jFound = false, kFound = false;

		//found for I

		while (iFound != true && stack.size() >= 2)
		{
			char first = stack.front();
			stack.pop();

			if( first == 'i')
			{
				iFound = true;
				break;
			}
			char sec = stack.front();
			//stack.pop();

			string result = myMap[make_pair(first, sec)];

			if (result[0] == '-')
			{
				isNegative = !isNegative;
				stack.front() = result[1];
				//stack.push(result[1]);
			}
			else
			{
				stack.front() = result[0];
				//stack.push(result[0]);
			}
		}

		//find J
		while (iFound == true && stack.size() >= 2)
		{
			char first = stack.front();
			stack.pop();

			if( first == 'j')
			{
				jFound = true;
				break;
			}

			char sec = stack.front();
			//stack.pop();

			string result = myMap[make_pair(first, sec)];

			if (result[0] == '-')
			{
				isNegative = !isNegative;
				stack.front() = result[1];
			}
			else
			{
				stack.front() = result[0];
				//stack.push(result[0]);
			}
		}

		//find k
		while (iFound  == true && jFound == true && stack.size() > 1)
		{
			char first = stack.front();
			stack.pop();

			/*if( first == 'k')
			{
				kFound = true;
				break;
			}*/

			char sec = stack.front();
			//stack.pop();

			string result = myMap[make_pair(first, sec)];

			if (result[0] == '-')
			{
				isNegative = !isNegative;
				stack.front() = result[1];
			}
			else
			{
				stack.front() = result[0];
			}
		}
		if(stack.size() >= 1)
		{
			char first = stack.front();
			if (first == 'k')
			{
				kFound = true;
			}
		}
		cout<<"Case #"<<t<<": ";
		if (iFound && jFound && kFound && !isNegative)
		{
			cout<<"YES"<<endl;
		}
		else
			cout<<"NO"<<endl;
		//cout<<stack.top()<<endl;;
		//cout<<"::"<<isNegative<<endl;
	}

	
}


/*

if (X % 2 == 0)
		{
			if (isNegative == true)
			{
				isNegative = false;
			}
		}
			
		char ch = stack.front();
		for (int i = 0; i < X - 1; i++)
		{
			stack.push(ch);
		}

		while (true)
		{
			if (stack.size() >= 2)
			{
				char first = stack.front();
				stack.pop();
				char sec = stack.front();
				stack.pop();

				string result = myMap[make_pair(first, sec)];

				if (result[0] == '-')
				{
					isNegative = !isNegative;
					stack.push(result[1]);
				}
				else
				{
					stack.push(result[0]);
				}
			}
			else
				break;
		}

*/