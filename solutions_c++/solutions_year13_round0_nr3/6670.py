#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

string to_string(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

int main()
{
	ifstream input;
	ofstream output;
	
	input.open("input.txt", ios::in);
	output.open("output.txt", ios::out);
	
	bool flag;
	int T, start, end, n, m, result, square;
	double startd;
	string trial;
	ostringstream convert;
	
	input >> T;
	
	for(int a = 0; a < T; a++){
		flag = false;
		result = 0;
		input >> startd >> end;
		start = int(sqrt(startd) + 0.999999999);
		end = int(sqrt(end));
		cout << start << " " << end << " " << startd << endl;
		for(int i = start; i <= end; i++){
			
			trial = to_string(i);
			n = trial.length();
			m = n/2;
			cout << trial << endl;
			for(int j = 0; j <= m; j++){
				if(trial[j] != trial[n-j-1]){
					break;
				}
				if(j==m){
					flag = true;
				}
			}
			if (flag == true){
				flag = false;
				square = i*i;
				trial = to_string(square);
				n = trial.length();
				m = n/2;
				for(int j = 0; j <= m; j++){
					if(trial[j] != trial[n-j-1]){
						break;
					}
					if(j==m){
						flag = true;
					}
				}
				if (flag == true){
					result++;
				}
			}
			
		}
		
		output << "Case #" << a+1 << ": " << result << endl;
	}
    system("PAUSE");
    return EXIT_SUCCESS;
}
