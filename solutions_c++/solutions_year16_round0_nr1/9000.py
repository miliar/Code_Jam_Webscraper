#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

string calc(long int n){

	if(n == 0){
		return "INSOMNIA";
	}
	else{
		string out_last_digit;

		string f_digits = "";
		long int num;
		int index = 0;

		while(f_digits.size() < 10){
			
			index++;
			num = n * index;

			std::ostringstream os;
			os << num;
			string n_digits = os.str();

			for(string::iterator it = n_digits.begin(); it != n_digits.end(); ++it) 
			{
			    string dig = string(1, *it);			   	

				size_t found = f_digits.find(dig);	
				if (found == string::npos)
					f_digits += dig;
				if(f_digits.size() == 10)
					out_last_digit = to_string(num);
			}
			//cout << f_digits << endl;	
		}
		//cout << f_digits << endl;	
		//cout << out_last_digit << endl;	
		return out_last_digit;	
	}
}

int main(int argc, char const *argv[]){

	int t;
	vector<long int> n;

	cin >> t;

	long int tn;
	for (int i = 0; i < t; ++i)
	{
		cin >> tn;
		n.push_back(tn);
	}

	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << (i + 1) << ": " << calc(n[i]) << endl;		
	}

	return 0;
}

