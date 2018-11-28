#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

int main(int argc, char *argv[])
{
    if (argc!=3) 
    {
	cout << "Missing arguments." << endl;
	return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    for (int i = 0; i < T; ++i)
    {
		int Smax;
		fin >> Smax;
		string S;
		fin >> S;
		
			
		int f = 0;
		int acc = 0;
		
		for (int j = 0; j < S.size(); ++j)
		{
			
			if (acc < j)
			{
				f += j - acc;
				acc = j;
			}
			
			acc += static_cast<int>(S[j]-'0') ;
			
			
			cout << j << " "<<acc << " " << f << endl;
		}
		cout << endl;
		
		
		
		fout << "Case #" << i+1 << ": "<< f;
		fout << endl;
    }
    return 0;
}
