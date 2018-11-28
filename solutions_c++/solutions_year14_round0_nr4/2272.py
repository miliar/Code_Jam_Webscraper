#include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int t, N;
double block;

int main()
{
	cin >> t;
	for (int i = 0; i<t; i++){
		cin >> N;
		vector<double> naomi, ken, n2, k2;
		for (int k = 0; k<N; k++){
			cin >> block;
			naomi.push_back(block);
			n2.push_back(block);
		}
		for (int l = 0; l<N; l++){
			cin >> block;
			ken.push_back(block);
			k2.push_back(block);
		}
		int classic = 0;
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		sort(n2.begin(), n2.end());
		sort(k2.begin(), k2.end());
		for (int m = 0; m<N; m++){
			for (int n = 0; n<N; n++){
				if (ken[n]>naomi[m]){
					ken[n] = -1;
					classic++;
					break;
				}
			}
		}
		classic = N - classic;



		int dec = 0, flag = 0;
		for (int o = N - 1; o >= 0; o--){
			flag = 0;
			for (int p = 0; p<N; p++){

				if (k2[o]<n2[p]){
					n2[p] = -1;
					flag = 1;
					dec++;
					break;
				}
			}
			if (flag == 0){
				for (int z = 0; z<N; z++){
					if (n2[z] != -1){
						n2[z] = -1;
						break;
					}
				}
			}
		}


		cout << "Case #" << i + 1 << ": " << dec << " " << classic << endl;
	}

}
