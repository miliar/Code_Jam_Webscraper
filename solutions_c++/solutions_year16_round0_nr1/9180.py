#include <iostream>
#include <fstream>
#include <algorithm>
#include <string.h>
#include <conio.h>

using namespace std;

int isFound[10];


string addBig (string a, string b)
{
	
	int num1[255], num2[255], sum[255];
	char s1[255], s2[255], sumString[255];
	int l1, l2;

	a.copy(s1, a.size(), 0);
	b.copy(s2, b.size(), 0);
	s1[a.size()] = '\0';
	s2[b.size()] = '\0';
	

	/* convert character to integer*/
	
	for (l1 = 0; s1[l1] != '\0'; l1++)
		num1[l1] = s1[l1] - '0';
	
	for (l2 = 0; s2[l2] != '\0'; l2++)
		num2[l2] = s2[l2] - '0';
	
	int carry = 0;
	int k = 0;
	int i = l1 - 1;
	int j = l2 - 1;
	
	for (; i >= 0 && j >= 0; i--, j--, k++) {
		sum[k] = (num1[i] + num2[j] + carry) % 10;
		carry = (num1[i] + num2[j] + carry) / 10;
	}
	if (l1 > l2) {
	
		while (i >= 0) {
			sum[k++] = (num1[i] + carry) % 10;
			carry = (num1[i--] + carry) / 10;
		}
	
	} else if (l1 < l2) {
		while (j >= 0) {
			sum[k++] = (num2[j] + carry) % 10;
			carry = (num2[j--] + carry) / 10;
		}
	} else {
		if (carry > 0)
			sum[k++] = carry;
	}
	
	int nDigits = 0;
	for (k--; k >= 0; k--){
		sumString[k]=sum[k] + '0'; 
		nDigits++;
	}
	sumString[nDigits] = '\0';
	
	string result(sumString);
	std::reverse(result.begin(), result.end());
	return result;
}




int updateDigits (string num)
{
	int counter = 0;
	for (int i=0; i<num.size();i++){
		if (isFound[num[i] - '0'] == 0)
			counter++;
		isFound[num[i] - '0'] = 1;
		
	}
	
	/*while (1){
		int digit = num %10;
		if (isFound[digit] == 0)
			counter++;
		isFound[digit] = 1;
		num = num/10;
		if (num == 0)
			break;
	}*/
	
	return counter;
	
}




int main ()
{
	
	std::ifstream fin("A_small.txt", std::ifstream::in);
	std::ofstream fout("A_large_out.txt", std::ifstream::out);
	
	

	int no_tc;
	fin >> no_tc;
	
	for (int tc=1; tc<=no_tc; tc++){
		for (int x=0;x<10;x++){
			isFound[x] = 0;
		}
		int counter = 0;
		fout <<"Case #"<<tc<<": ";

		
		string num;
		fin >> num; 	
		if (num=="0"){
			fout<<"INSOMNIA"<<endl;
			continue;
		}
		
		string checkNum(num);
		while (1){
			//cout<<num<<endl;
			//getch();
			counter += updateDigits (checkNum);
			if (counter == 10){
				fout<<checkNum<<endl;
				break;	
			}
			
			checkNum = addBig(checkNum,num);
		}
			
	}
	return 1;
	
}
