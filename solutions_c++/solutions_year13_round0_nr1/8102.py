#include <iostream>
#include <string>
#include <string.h>
#include <fstream>

using namespace std;

string check_row(string* d){
	int counter = 0;
	for(int i=0;i<4;i++){
		if(d[i][0] == 'T'){
			if((d[i][1] == d[i][2])&&(d[i][2] == d[i][3])){
				if(d[i][1]!='.'){
					string temp;
					temp += d[i][1];
					temp += " won";
					return temp ;
					break;
				}
			}
		}

		if(((d[i][0] == d[i][1])||(d[i][1] == 'T'))&&(d[i][0] != '.')){
			counter ++;
		}
		if(((d[i][0] == d[i][2])||(d[i][2] == 'T'))&&(d[i][0] != '.')){
			counter ++;
		}
		if(((d[i][0] == d[i][3])||(d[i][3] == 'T'))&&(d[i][0] != '.')){
			counter ++;
		}
		if(counter == 3){
			string temp;
			temp += d[i][0];
			temp += " won";
			return temp ;
			break;
		}
		counter =0;
	}
	return "NO";
}
string check_coloumn(string* d){
	int counter = 0;
	for(int i=0;i<4;i++){
		if(d[0][i] == 'T'){
			if((d[1][i] == d[2][i])&& (d[2][i]== d[3][i])){
				if(d[1][i]!='.'){
					string temp;
					temp += d[1][i];
					temp += " won";
					return temp ;
					break;
				}
			}
		}
		if(((d[0][i] == d[1][i])||(d[1][i] == 'T'))&&(d[0][i] != '.')){
			counter ++;
		}
		if(((d[0][i] == d[2][i])||(d[2][i] == 'T'))&&(d[0][i] != '.')){
			counter ++;
		}
		if(((d[0][i] == d[3][i])||(d[3][i] == 'T'))&&(d[0][i] != '.')){
			counter ++;
		}
		if(counter == 3){
			string temp;
			temp += d[0][i];
			temp += " won";
			return temp ;
			break;
		}
		counter = 0;
	}
	return "NO";
}
string check_diag(string* d){
	int counter = 0;
	int j =0;
	int i=0;
	if(d[j][i] == 'T'){
		if((d[j+1][i+1] == d[j+2][i+2]) && (d[j+2][i+2]== d[j+3][i+3])){
			if(d[j+1][i+1]!='.'){
				string temp;
				temp += d[j+1][i+1];
				temp += " won";
				return temp ;
			}
		}
	}
	if(((d[j][i] == d[j+1][i+1])||(d[j+1][i+1] == 'T'))&&(d[j][i] != '.')){
		counter ++;
	}
	if(((d[j][i] == d[j+2][i+2])||(d[j+2][i+2] == 'T'))&&(d[j][i] != '.')){
		counter ++;
	}
	if(((d[j][i] == d[j+3][i+3])||(d[j+3][i+3] == 'T'))&&(d[j][i] != '.')){
		counter ++;
	}
	if(counter == 3){
		string temp;
		temp += d[j][i];
		temp += " won";
		return temp ;
	}
	counter = 0;
	i=0;
	j=3;
	if(d[j][i] == 'T'){
		if((d[j-1][i+1] == d[j-2][i+2])&& (d[j-2][i+2]== d[j-3][i+3])){
			if(d[j-1][i+1]!='.'){
				string temp;
				temp += d[j-1][i+1];
				temp += " won";
				return temp ;
			}
		}
	}
	if(((d[j][i] == d[j-1][i+1])||(d[j-1][i+1] == 'T'))&&(d[j][i] != '.')){
		counter ++;
	}
	if(((d[j][i] == d[j-2][i+2])||(d[j-2][i+2] == 'T'))&&(d[j][i] != '.')){
		counter ++;
	}
	if(((d[j][i] == d[j-3][i+3])||(d[j-3][i+3] == 'T'))&&(d[j][i] != '.')){
		counter ++;
	}
	if(counter == 3){
		string temp;
		temp += d[j][i];
		temp += " won";
		return temp ;
	}
	counter = 0; 
	return "NO";
}


void main()
{
	string input[1010];
	int k=0;
	string output;
	fstream data_file("E:\data.in.txt", fstream::in);
	while (data_file.good())
				{
    
				getline(data_file,input[k]);
				
				k++;
	}
	string s[4] ;
	int tt=1;
	for(int h=1;h<=atoi(input[0].c_str());h++){
		int g =0;
	while(input[tt].length() != 0){
		s[g] = input[tt];
		g++;
		tt++;
	}
	tt++;
	int dot_number = 0;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(s[i][j] == '.'){
				dot_number ++;
			}
		}
	}
	if(((check_row(s) == "NO")&&(check_coloumn(s)=="NO"))&&((check_coloumn(s)=="NO")&&(check_diag(s)=="NO")))
	{
		if(!dot_number){
			cout<<"Draw"<<endl;
			output += ("Case #"+to_string(h)+": "+"Draw\n");
		}
		else
		{
			cout << "Game has not completed"<<endl;
			output += ("Case #"+to_string(h)+": "+"Game has not completed\n");
		}
	}
	else{
		bool check = false;
		while((check_row(s) != "NO")){
			cout << (check_row(s))<<endl;
			output += ("Case #"+to_string(h)+": "+(check_row(s))+"\n");
			check = true;
			break;
		}
		while((check_coloumn(s) != "NO")&&(!check)){
			cout << (check_coloumn(s))<<endl;
			output += ("Case #"+to_string(h)+": "+(check_coloumn(s))+"\n");
			break;
		}
		while((check_diag(s) != "NO")&&(!check)){
			cout << (check_diag(s))<<endl;
			output += ("Case #"+to_string(h)+": "+(check_diag(s))+"\n");
			break;
		}
	}
	}
	fstream data_file1("E:\data.out.txt", fstream::out);
	data_file1 <<output;
	system("pause");

}