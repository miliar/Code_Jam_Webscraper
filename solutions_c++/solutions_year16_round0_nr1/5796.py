#include<string>
#include<iostream>
#include<fstream>
using namespace std;
string multiply(string num1, string num2)   
{  
    string rs(num1.length()+num2.length(), '0');  
    for (int i = num1.length()-1, d = rs.length()-1; i >= 0; i--, d--)  
    {  
       int carry = 0, k = d;  
       for (int j = num2.length()-1; j >= 0; j--, k--)  
       {  
           int a = num1[i] - '0';  
           int b = num2[j] - '0';  
           a = a*b+carry + (rs[k]-'0');  
           carry = a/10;  
           rs[k] = a%10 + '0';  
       }  
       while (carry)  
       {  
           int sum = carry + (rs[k]-'0');  
           carry = sum / 10;  
           rs[k--] = sum % 10 + '0';  
       }  
    } 
    while (rs.size() > 1 && rs[0] == '0') rs.erase(rs.begin());  
    return rs;  
    }
int main() {
	ifstream fin("A-large.in");
	ofstream fout("cnt_sheep.out");
	int N;
	fin >> N;
	for (int cnt = 0; cnt < N; cnt++) {
		bool mark[10];
		for (int j = 0; j < 10; j++)
			mark[j] = false;
		bool sleep = false;
		int i = 1, notpossible=1<<15;
		string in;
		fin >> in;
		cout << "end input" << endl;
		string rslt = "";
		while (!sleep) {
			rslt = multiply(in, to_string(i));
			cout << rslt << endl;
			for (int j = 0; j < rslt.length(); j++)
				mark[rslt[j] - '0'] = true;
			sleep = true;
			for (int j = 0; j < 10; j++)
				if (mark[j] == false) {
					sleep = false;
					break;
				}
			i++;
			if(i>notpossible) break;
		}
		if(i<notpossible)
			fout <<"Case #"<<cnt+1<<": "<<rslt<<endl;
		else
			fout <<"Case #"<<cnt+1<<": INSOMNIA"<<endl;
	}

	return 0;
}
