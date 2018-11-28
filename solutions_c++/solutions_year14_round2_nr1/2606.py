#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cmath>
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

    for (int t = 0; t < T; ++t)
    {
	fout << "Case #" << t+1 << ": ";

	int N;
	fin >> N;	

	vector<string> s;
	s.resize(N);

	for (int i = 0; i < N; ++i)
	{
	    fin >> s[i];
	}


	vector<string> ss;
	ss.resize(N);
	
	for (int i = 0; i < N; ++i)
	{
	    ss[i] = "";
	    ss[i] += s[i][0];
	    int counter = 0;

	    for (int j = 1; j < s[i].size(); ++j)
	    {
		if (s[i][j] == s[i][j-1])
		    continue;
		else
		    ss[i] += s[i][j];
	    }
	}

	
	bool feglawins = false;

	for (int i = 1; i < N; ++i)
	{
	    if (ss[0] == ss[i]) continue;
	    else feglawins = true;
	    
	}

	if (feglawins)
	{
	    fout << "Fegla Won" << endl;
	    continue;
	}

	else
	{
	    vector<vector<int> > rep;
	    rep.resize(N);

	    for (int i = 0; i < N; ++i)
	    {
		int counter = 0;
		char current = s[i][0];

		for (int j = 0; j < s[i].size(); ++j)
		{
		    if (s[i][j] == current)
		    {
			counter++;
		    }
		    else
		    {
			rep[i].push_back(counter);
			counter = 1;
			current = s[i][j];
		    }
		}
		rep[i].push_back(counter);
	    }

	    int change = 0;

	    for (int j = 0; j < ss[0].size(); ++j)
	    {
		vector<int> hist;
		hist.resize(101);
		double mean = 0;
		for (int i = 0; i < N; ++i)
		{
		    hist[rep[i][j]]++;
		    mean += rep[i][j];
		}

		mean /= double(N);


		mean = floor(mean);
		double fmae = 0 ;
		for (int i = 0; i < N; ++i)
		{
		    fmae += abs(mean - rep[i][j]);
		}
		
		mean++;
		double cmae = 0 ;
		for (int i = 0; i < N; ++i)
		{
		    cmae += abs(mean - rep[i][j]);
		}

		double mae = cmae > fmae ? fmae : fmae;
		change += mae;

		
	    }



/*	    for (int i = 0; i < N; ++i)
	    {
		for (int j = 0; j < rep[i].size(); ++j)
		    cout << rep[i][j];
		cout << endl;
	    }*/
	    fout << change << endl;

	    

	}





    }
    return 0;
}


