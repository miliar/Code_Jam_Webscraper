#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

bool consonant(string sub, int num){
	int count = 0;

	for(int i=0; i<sub.length(); i++)
	{
		if(sub[i]=='a' || sub[i]=='e' || sub[i]=='i' || sub[i]=='o' || sub[i]=='u')
		{
			count=0;
			continue;
		}
		count++;
		if(count >= num) return true;
	}

	return false;
}

int findResult(string str, int num)
{
	int len = str.length();
	int count = 0;

	for(int st=0; st<=len-num; st++){
		for(int size=num; size<=len-st; size++){
			string sub = str.substr(st, size);

			if(consonant(sub, num)){
				count += (len-st - size + 1);
				break;
			}
		}
	}

	return count;
}


int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int input_count;
	cin >> input_count;

	int counter = 1;
	while(input_count)
	{
		string str;
		long num;

		cin >> str;
		cin >> num;
		int result = findResult(str, num);
		cout << "Case #" << counter++ << ": " << result << "\n";

		//finish work
		input_count--;
	}

	return 0;
}