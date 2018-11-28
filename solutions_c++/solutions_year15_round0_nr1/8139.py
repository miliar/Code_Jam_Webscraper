#include <iostream>
#include <string>
#include <fstream>
using namespace std;
long code(long m_shy, string arr_shy){
	int *arr = new int[m_shy+1];
	int k = 0;
	long aud_stand = 0;
	long aud_req = 0;
	while(k<m_shy+1){
	arr[k] = arr_shy[k] - 48;
	k++;
	}
	k = 0;
	while(k<m_shy+1){
		if (k<=aud_stand){
			aud_stand += arr[k];
		}
		else{
			aud_req += k - aud_stand;
			aud_stand += arr[k] + k - aud_stand;

		}
	k++;}
	return aud_req;
	delete[] arr;
}

int main(){
long num_cases;
ifstream fcin;
fcin.open("A-large.in");
fcin >> num_cases;
if(!fcin.is_open()){
	cout << "error";
}
ofstream fcout;
fcout.open("output-large.out",ios::trunc);
long *arr_of_cases = new long[num_cases];
string *arr_of_all_shyness = new string[num_cases];
long i= 0;
while(i < num_cases){
	fcin >> arr_of_cases[i];
	fcin >> arr_of_all_shyness[i];
	i++;
}
fcin.close();
i=0;
while(i < num_cases){
	fcout << "Case #"<<i+1<<": "<<code(arr_of_cases[i],arr_of_all_shyness[i])<<"\n";
	i++;
}
delete[] arr_of_cases;
delete[] arr_of_all_shyness;

return 0;
}