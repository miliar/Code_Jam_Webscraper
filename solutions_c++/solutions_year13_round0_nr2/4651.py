#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool result(int N, int M, vector<vector<int> >vet){
	if(N == 1 || M == 1)
		return true;
	vector<int> maxrow(N, 0);
	vector<int> maxline(M, 0);
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
		{
			if(vet[i][j] > maxrow[i])
				maxrow[i]=vet[i][j];
			if(vet[i][j] > maxline[j])
				maxline[j]=vet[i][j];
		}
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			if(vet[i][j] < maxrow[i])
				if(vet[i][j] < maxline[j])
					return false;
	return true;
}

int main()
{
	ifstream infile("D:\\input.txt");
	ofstream outfile("D:\\output.txt");
	if(!infile){
		cout << "Can't open input.txt" << endl;
	}
	if(!outfile){
		cout << "Can't open output.txt" << endl;
	}
	int T;
	infile >> T;
	for(int i = 0; i < T; i++)
	{
		int N, M;
		infile >> N >> M;
		vector<vector<int> > vet(N, vector<int>(M));
		for(int i = 0; i < N; i++)
			for(int j = 0; j < M; j++)
				infile >> vet[i][j];
		if(result(N, M, vet))
			outfile << "Case #" << i+1 << ": " << "YES" << endl;
		else
			outfile << "Case #" << i+1 << ": " << "NO" << endl;
	}
	return 0;
}