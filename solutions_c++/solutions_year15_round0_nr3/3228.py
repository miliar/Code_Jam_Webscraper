#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

//#define _TEST_

#ifdef _TEST_
ifstream fin("C.in");
ofstream fout("C.out");
#else
ifstream fin("C-small-attempt2.in.txt");
ofstream fout("C-small-attempt2.out.txt");
#endif

map<string,string> q;
int T, L, X, counter;
vector<int> dp_i, dp_k;

void precompute()
{
    q["i1"] = q["1i"] = q["jk"] = q["-kj"] = q["k-j"] = "i";
    q["-1i"] = q["i-1"] = q["kj"] = q["-jk"] = q["j-k"] =  "-i";
    q["j1"] = q["1j"] = q["ki"] = q["-ik"] = q["i-k"] = "j";
    q["-1j"] = q["j-1"] = q["ik"] = q["-ki"] = q["k-i"] =  "-j";
    q["k1"] = q["1k"] = q["ij"] = q["-ji"] = q["j-i"] = "k";
    q["-1k"] = q["k-1"] = q["ji"] = q["-ij"] = q["i-j"] =  "-k";
    q["-ii"] = q["-jj"] = q["-kk"] = q["i-i"] = q["j-j"] = q["k-k"] = "1";
    q["ii"] = q["jj"] = q["kk"] = "-1";
}

int find_char(string s, string c, int start)
{
    string cur = string(1,s[start%L]);
    for(int i = start+1; i < L*X; i++)
    {
	if(cur == c) return i;
	if(q.find(cur+s[i%L]) == q.end()) cout << "failed to search for ele!" << endl;
	cur = q[cur+s[i%L]];
    }
    return -1;
}

bool have_k(string s, int start)
{
    string ret = string(1,s[start%L]);
    for(int i = start+1; i < L*X; i++)
    {
	if(q.find(ret+s[i%L]) == q.end()) cout << "failed to search for ele!" << endl;	
	ret = q[ret+s[i%L]];
    }
    return (ret == "k");
}

int main()
{
    precompute();
    fin >> T;
    for(int c = 1; c <= T; c++)
    {
	fin >> L >> X;
	string s; fin >> s;
	if(L*X <= 3)
	{
	    if(s == "ijk") fout << "Case #" << c << ": YES" << endl;
	    else fout << "Case #" << c << ": NO" << endl;
	    continue;
	}

	int idx = find_char(s, "i", 0);
	if(idx < 0 || idx > L*X-2)
	{
	    fout << "Case #" << c << ": NO" << endl;
	    continue;
	}
	idx = find_char(s, "j", idx);
	if(idx < 0 || idx >= L*X-1)
	{
    	    fout << "Case #" << c << ": NO" << endl;
	    continue;
	}
	if(have_k(s,idx)) fout << "Case #" << c << ": YES" << endl;
	else fout << "Case #" << c << ": NO" << endl;
    }

    return 0;
}
