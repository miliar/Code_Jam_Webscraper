#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<fstream>
#pragma warning (disable : 4996)

using namespace std;

int main() {

	FILE *read = fopen("B.in", "r");
	
	FILE *write = fopen("B.txt","w");

	int t;
	fscanf(read, "%d", &t);

	for (int i = 0;i < t;i++) {

		int n;
		fscanf(read, "%d", &n);

		vector<int> height;

		for (int j = 0;j < 2*n-1;++j) {

			for (int k = 0;k < n;++k) {

				int val;
				fscanf(read, "%d", &val);

				bool match = false;
				for (int l = 0;l < height.size();l++) {
					if (height[l] == val) {
						match = true;
						height.erase(height.begin() + l);
						//cout << val;
						break;
					}
				}
				if (match == false) {
					height.push_back(val);
				}

			}
		}

		sort(height.begin(), height.end());
		
		fprintf(write,"Case #%d:",i+1);

		for (int j = 0;j < height.size();j++) {
			fprintf(write, " %d", height[j]);
		}

		fprintf(write,"\n");

	}
	
	fclose(read);
	fclose(write);

	return 0;
}