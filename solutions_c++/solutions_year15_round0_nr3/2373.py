#include <iostream>
#include <fstream>
//#include <vector>
//#include <string>
//#include <cstdlib>
#include <unordered_map>
#include <algorithm>
using namespace std;

void generateValueMap(unordered_map<string, pair<bool, char> > & quaternions)
{
	quaternions["11"] = pair<bool, char>(true, '1');
	quaternions["1i"] = pair<bool, char>(true, 'i');
	quaternions["1j"] = pair<bool, char>(true, 'j');
	quaternions["1k"] = pair<bool, char>(true, 'k');
	quaternions["i1"] = pair<bool, char>(true, 'i');
	quaternions["ii"] = pair<bool, char>(false, '1');
	quaternions["ij"] = pair<bool, char>(true, 'k');
	quaternions["ik"] = pair<bool, char>(false, 'j');
	quaternions["j1"] = pair<bool, char>(true, 'j');
	quaternions["ji"] = pair<bool, char>(false, 'k');
	quaternions["jj"] = pair<bool, char>(false, '1');
	quaternions["jk"] = pair<bool, char>(true, 'i');
	quaternions["k1"] = pair<bool, char>(true, 'k');
	quaternions["ki"] = pair<bool, char>(true, 'j');
	quaternions["kj"] = pair<bool, char>(false, 'i');
	quaternions["kk"] = pair<bool, char>(false, '1');
}

bool isBreakable(string s, int X, unordered_map<string, pair<bool, char> > & quaternions)
{
	int L = s.length();
	if(L * X < 3) return false;
	int i, j;
	string product;
	product += s[0];
	bool sign = true;
	for(i = 1; i < (X%4) * L; i++)
	{
		product += s[i%L];
		if(!quaternions[product].first) sign = !sign;
		product = quaternions[product].second;
	}
	if(sign || product != "1") return false;
	
	product.clear();
	product += s[0];
	sign = true;
	i = 1;
	while(i < min(X, 4) * L)
	{
		if(sign && product == "i") break;
		product += s[i%L];
		if(!quaternions[product].first) sign = !sign;
		product = quaternions[product].second;
		i++;
	}
	if(!sign || product != "i") return false;
	
	//cout << i-1 << " ";
	
	product.clear();
	product += s[i%L];
	sign = true;
	j = i+1;
	while(j < min(X * L, i+4*L))
	{
		if(sign && product == "j") break;
		product += s[j%L];
		if(!quaternions[product].first) sign = !sign;
		product = quaternions[product].second;
		j++;
	}
	if(!sign || product != "j") return false;
	
	//cout << j-1 << endl;
	
	return true;
}


int main()
{
	fstream  infile, outfile;
	infile.open("C-small-attempt0.in", ios::in);
	//infile.open("input.txt", ios::in);
	
	infile.seekg(0, ios::end);  
	if (infile.tellg() == 0) return 0;
	infile.seekg(0, ios::beg);
	
	outfile.open("output.txt", ios::out | ios::trunc);
	
	unordered_map<string, pair<bool, char> > quaternions;
	generateValueMap(quaternions);
	
	int i, nCase, L, X;
	string s;
	infile >> nCase;
	cout << nCase << endl;
	for(i = 0; i < nCase; i++)
	{
		infile >> L;
		infile >> X;
		infile >> s;
		//cout << s << endl;
		
		if(isBreakable(s, X, quaternions)) 
			outfile << "Case #" << i+1 << ": YES" << endl;
		else
			outfile << "Case #" << i+1 << ": NO" << endl;
	}
	infile.close();
	outfile.close();
	
	return 0;
}
