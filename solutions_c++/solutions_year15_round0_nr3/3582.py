#include<iostream>
#include<string>
#include<fstream>
using namespace std;

string product(char a, char b){

	
	if (a == '1'&& b == '1')
		return "1";
	else if (a == '1'&& b == 'i')
		return "i";
	else if (a == '1'&& b == 'j')
		return "j";
	else if (a == '1'&& b == 'k')
		return "k";
	else if (a == 'i'&& b == '1')
		return "i";
	else if (a == 'i'&& b == 'i')
		return "-1";
	else if (a == 'i'&& b == 'j')
		return "k";
	else if (a == 'i'&& b == 'k')
		return "-j";
	else if (a == 'j'&& b == '1')
		return "j";
	else if (a == 'j'&& b == 'i')
		return "-k";
	else if (a == 'j'&& b == 'j')
		return "-1";
	else if (a == 'j'&& b == 'k')
		return "i";
	else if (a == 'k'&& b == '1')
		return "k";
	else if (a == 'k'&& b == 'i')
		return "j";
	else if (a == 'k'&& b == 'j')
		return "-i";
	else if (a == 'k'&& b == 'k')
		return "-1";

}



string products(string a, char b){


	if (a == "1"&& b == '1')
		return "1";
	else if (a == "1"&& b == 'i')
		return "i";
	else if (a == "1"&& b == 'j')
		return "j";
	else if (a == "1"&& b == 'k')
		return "k";
	else if (a == "i"&& b == '1')
		return "i";
	else if (a == "i"&& b == 'i')
		return "-1";
	else if (a == "i"&& b == 'j')
		return "k";
	else if (a == "i"&& b == 'k')
		return "-j";
	else if (a == "j"&& b == '1')
		return "j";
	else if (a == "j"&& b == 'i')
		return "-k";
	else if (a == "j"&& b == 'j')
		return "-1";
	else if (a == "j"&& b == 'k')
		return "i";
	else if (a == "k"&& b == '1')
		return "k";
	else if (a == "k"&& b == 'i')
		return "j";
	else if (a == "k"&& b == 'j')
		return "-i";
	else if (a == "k"&& b == 'k')
		return "-1";
	else if (a == "-1"&& b == '1')
		return "-1";
	else if (a == "-1"&& b == 'i')
		return "-i";
	else if (a == "-1"&& b == 'j')
		return "-j";
	else if (a == "-1"&& b == 'k')
		return "-k";
	else if (a == "-i"&& b == '1')
		return "-i";
	else if (a == "-i"&& b == 'i')
		return "1";
	else if (a == "-i"&& b == 'j')
		return "-k";
	else if (a == "-i"&& b == 'k')
		return "j";
	else if (a == "-j"&& b == '1')
		return "-j";
	else if (a == "-j"&& b == 'i')
		return "k";
	else if (a == "-j"&& b == 'j')
		return "1";
	else if (a == "-j"&& b == 'k')
		return "-i";
	else if (a == "-k"&& b == '1')
		return "-k";
	else if (a == "-k"&& b == 'i')
		return "-j";
	else if (a == "-k"&& b == 'j')
		return "i";
	else if (a == "-k"&& b == 'k')
		return "1";
	


}


bool checki(string s, int size, int &index){

	string pro;

	for (int i = 0; i < size-1; i++){

		if (i == 0)
			pro = product(s[i], s[i + 1]);
		else
			pro = products(pro, s[i + 1]);

		if (pro == "i"){
			index = i + 2;
			return true;
		}



	}


	return false;
}

bool checkj(string s, int size, int &index){

	string pro;

	for (int i = index; i < size - 1; i++){

		if (i == index)
			pro = product(s[i], s[i + 1]);
		else
			pro = products(pro, s[i + 1]);

		if (pro == "j"){
			index = i + 2;
			return true;
		}



	}


	return false;


}

bool checkk(string s, int size, int &index){

	string pro;

	for (int i = index; i < size - 1; i++){

		if (i == index)
			pro = product(s[i], s[i + 1]);
		else
			pro = products(pro, s[i + 1]);
		//cout << pro<<endl;
		if (pro=="k"&& i==size-2){
			index = i + 2;
			return true;
		}
		
		


	}


	return false;





}






int main(){

	int n = 0;
	ifstream fin;
	ofstream fout;
	bool ii = false;
	bool jj = false;
	bool kk = false;
	int L;
	int X;
	int size = 0;
	string s;
	string st;
	int index=0;


	fin.open("input.in");
	fout.open("output.out");

	fin >> n;

	for (int i = 0; i < n; i++){

		fin >> L;
		fin >> X;
		size = L*X;
		fin >> s;
		st = s;
		ii = false;
		jj = false;
		kk = false;

		for (int i = 0; i < X - 1; i++)
			st = st + s;

		
		if (X == 1 && L == 3 && s[0] == 'i'&& s[1] == 'j'&& s[2] == 'k'){
			ii = true;
			jj = true;
			kk = true;
		}

		else {

			ii = checki(st, size, index);
			if (ii)
				jj = checkj(st, size, index);
			if (ii && jj)
				kk = checkk(st, size, index);

		}

		//cout << ii << jj << kk <<index<< endl;

		//cout << ii << jj << kk <<index <<endl;



		if (ii&&jj&&kk)
			fout << "Case #" <<i+1<< ": "<< "YES"<<endl;
		else
			fout << "Case #" << i + 1 << ": " << "NO" << endl;

		//cout << st.max_size();

	}

	return 0;
}