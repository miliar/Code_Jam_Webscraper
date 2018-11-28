#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#pragma warning (disable : 4996)

using namespace std;

int main() {

	FILE* read=fopen("A.in", "r");
	FILE* write = fopen("A.txt", "w");
	
	int t;
	fscanf_s(read,"%d",&t);

	for (int i = 0;i < t;i++) {

		bool sample[10] = { false };

		int n;
		fscanf_s(read, "%d", &n);

		vector<int> data;		

		//check
		bool flag = true;
		int iter = 1;
		do {

			int value = iter*n;

			//cout << "V : " << value << endl;

			bool out = false;
			for (int j = 0;j < data.size();j++) {
				if (value == data.at(j)) {
					out = true;
					//cout << "Case #" << i + 1 << ": INMSONIA"<<endl;
					fprintf(write,"Case #%d: INSOMNIA\n",i+1);
					break;
				}
			}
			if (out == true)break;

			data.push_back(value);

			string val_str = to_string(value);

			for (int j = 0;j < val_str.length();j++) {
				int num = val_str[j] - '0';
				sample[num] = true;
			}


			

			//check
			flag = true;
			for (int j = 0;j < 10;j++) {
				if (sample[j] == false) {
					flag = false;
				}
			}


			if (flag == true) {
				//cout<<"Case #"<<i+1<<": " << value << endl;
				fprintf(write, "Case #%d: %d\n", i + 1, value);
			}

			iter++;


		}while(flag==false);

	}
	
	

	return 0;
}