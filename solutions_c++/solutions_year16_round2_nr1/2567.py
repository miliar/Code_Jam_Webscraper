#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main(int argc, char const *argv[]){

	int t;
	cin >> t;
	string s;
	string nums[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

	for (int i = 0; i < t; ++i)
	{	
		cin >> s;
		int sz = s.size();
		string phone = "";

		while(s.find('Z') != string::npos)
		{
			phone += '0';
			for(char& c : nums[0]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }				
		}
		while(s.find('W') != string::npos)
		{
			phone += '2';
			for(char& c : nums[2]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}
		while(s.find('U') != string::npos)
		{
			phone += '4';
			for(char& c : nums[4]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}
		while(s.find('X') != string::npos)
		{
			phone += '6';
			for(char& c : nums[6]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}
		while(s.find('G') != string::npos)
		{
			phone += '8';
			for(char& c : nums[8]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}

		while(s.find('O') != string::npos)
		{
			phone += '1';
			for(char& c : nums[1]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}

		while(s.find('T') != string::npos)
		{
			phone += '3';
			for(char& c : nums[3]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}

		while(s.find('F') != string::npos)
		{
			phone += '5';
			for(char& c : nums[5]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}

		while(s.find('F') != string::npos)
		{
			phone += '5';
			for(char& c : nums[5]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}

		while(s.find('V') != string::npos)
		{
			phone += '7';
			for(char& c : nums[7]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}

		while(s.find('E') != string::npos)
		{
			phone += '9';
			for(char& c : nums[9]) {
		        s.erase(remove(s.begin(), s.begin() + s.find(c) + 1, c), s.begin() + s.find(c) + 1);
		    }
		}

		/*while(s.size() !=0)
		{
			cout << s << endl;
			break;
		}*/

		sort(phone.begin(), phone.end());
		cout << "Case #" << (i + 1) << ": " << phone << endl;	
	}
	
	return 0;
}