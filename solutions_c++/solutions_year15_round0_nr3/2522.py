#include <iostream>
#include <string>

using namespace std;

string multiply(string a, char b){
	if (a == "1"){
		string tmp;
		tmp += b;
		return tmp;
	}
	if (a == "-1"){
		string  tmp = "-";
		tmp += b;
		return tmp;
	}
	////
	if (a == "i"){
		if (b == 'i'){
			return "-1";
		}
		if (b == 'j'){
			return "k";
		}
		if (b == 'k'){
			return "-j";
		}
	}
	if (a == "-i"){
		if (b == 'i'){
			return "1";
		}
		if (b == 'j'){
			return "-k";
		}
		if (b == 'k'){
			return "j";
		}
	}
	/////
	if (a == "j"){
		if (b == 'i'){
			return "-k";
		}
		if (b == 'j'){
			return "-1";
		}
		if (b == 'k'){
			return "i";
		}
	}
	if (a == "-j"){
		if (b == 'i'){
			return "k";
		}
		if (b == 'j'){
			return "1";
		}
		if (b == 'k'){
			return "-i";
		}
	}
	////////
	if (a == "k"){
		if (b == 'i'){
			return "j";
		}
		if (b == 'j'){
			return "-i";
		}
		if (b == 'k'){
			return "-1";
		}
	}
	if (a == "-k"){
		if (b == 'i'){
			return "-j";
		}
		if (b == 'j'){
			return "i";
		}
		if (b == 'k'){
			return "1";
		}
	}

}


int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int L, X;
		string Z, z;
		cin >> L >> X >> z;

		for (int i = 0; i < X; i++)Z += z;

		string curr; curr += z[0];
		bool donei = 0, donej = 0, skip = 0;
		for (int i = 1; i < L*X; i++){
			skip = 0;

			if (curr == "i" && !donei) {
				skip = 1;
				curr = Z[i];
				skip = 1;
				donei = 1;
			}
			else if (curr == "j" && donei && !donej){
				skip = 1;
				curr = Z[i];
				skip = 1;
				donej = 1;
			}
			if (!skip)curr = multiply(curr, Z[i]);
		}
		if (curr == "k" && donei && donej){
			cout << "Case #" << t << ": YES\n";
		}
		else{
			cout << "Case #" << t << ": NO\n";
		}
	}
	

}