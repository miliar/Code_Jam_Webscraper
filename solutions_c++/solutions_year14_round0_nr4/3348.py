#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int test_cases,n,i,j,a,b,war=0,d_war=0;
	float *p1, *p2;						//p1=Naomi    p2=Ken
	//ifstream fin("i4.txt");
	ifstream fin("i4.in");
	ofstream fout("Q4_Output.txt");
	fin >> test_cases;
	for (i = 0; i < test_cases; i++){
		fin >> n;
		p1 = new float[n];
		p2 = new float[n];
		for (j = 0; j < n; j++)
			fin >> p1[j];
		for (j = 0; j < n; j++)
			fin >> p2[j];

		for (a = 0; a < n - 1; a++){
			for (b = 0; b < n - 1-a; b++){
				if (p1[b]>p1[b + 1])
					swap(p1[b], p1[b + 1]);
			}
		}
		for (a = 0; a < n - 1; a++){
			for (b = 0; b < n - 1-a; b++){
				if (p2[b]>p2[b + 1])
					swap(p2[b], p2[b + 1]);
			}
		}

		for (a = 0, b = 0; b < n; b++, a++){
			while (p2[b] < p1[a] && b < n)
				b++;
			if (b == n)
				break;
		}
		war = n-a;



		for (a = 0, b = 0; b < n; b++,a++){
			while (p1[b] < p2[a] && b < n)
				b++;
			if (b == n)
				break;
		}
		d_war = a;
		
		fout << "Case #" << i+1<<": "<<d_war<<" "<<war << endl;
		
	}
	system("pause");
	return 0;
}