#include <iostream>
#include <fstream>
#include <queue>
#include <cassert>
#include <climits>
#include <cstring>
#include <map>



using namespace std;

map<string,string> ma;

int main()
{
	ma["11"]="1";
	ma["1i"]="i";
	ma["1j"]="j";
	ma["1k"]="k";
	ma["i1"]="i";
	ma["ii"]="-1";
	ma["ij"]="k";
	ma["ik"]="-j";
	ma["j1"]="j";
	ma["ji"]="-k";
	ma["jj"]="-1";
	ma["jk"]="i";
	ma["k1"]="k";
	ma["ki"]="j";
	ma["kj"]="-i";
	ma["kk"]="-1";
	
	ma["-11"]="-1";
	ma["-1i"]="-i";
	ma["-1j"]="-j";
	ma["-1k"]="-k";
	ma["-i1"]="-i";
	ma["-ii"]="1";
	ma["-ij"]="-k";
	ma["-ik"]="j";
	ma["-j1"]="-j";
	ma["-ji"]="k";
	ma["-jj"]="1";
	ma["-jk"]="-i";
	ma["-k1"]="-k";
	ma["-ki"]="-j";
	ma["-kj"]="i";
	ma["-kk"]="1";
	
	ma["1-1"]="-1";
	ma["1-i"]="-i";
	ma["1-j"]="-j";
	ma["1-k"]="-k";
	ma["i-1"]="-i";
	ma["i-i"]="1";
	ma["i-j"]="-k";
	ma["i-k"]="j";
	ma["j-1"]="-j";
	ma["j-i"]="k";
	ma["j-j"]="1";
	ma["j-k"]="-i";
	ma["k-1"]="-k";
	ma["k-i"]="-j";
	ma["k-j"]="i";
	ma["k-k"]="1";
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t,l,x;
	string s,str;
	in >> t;
	for(int i=0; i<t; i++)
	{
		in >> l >> x;
		in >> s;
		str=s;
		for(int j=0; j<x-1; j++)
			str+=s;
		cout << str;
		string curr = "1";
		int primoNonFatto=0;
		bool tuttoOK=true;
		while(curr!="i")
		{
			if(primoNonFatto==l*x)
			{
				tuttoOK=false;
				break;
			}
			curr = ma[curr+str[primoNonFatto++]];
		}
		curr="1";
		while(curr!="j")
		{
			if(primoNonFatto==l*x)
			{
				tuttoOK=false;
				break;
			}
			curr = ma[curr+str[primoNonFatto++]];
		}
		curr="1";
		while(curr!="k")
		{
			if(primoNonFatto==l*x)
			{
				tuttoOK=false;
				break;
			}
			curr = ma[curr+str[primoNonFatto++]];
		}
		curr="1";
		while(primoNonFatto<l*x)
		{
			curr = ma[curr+str[primoNonFatto++]];
		}
		if(curr!="1")
			tuttoOK=false;
		out << "Case #" << i+1 << ": " << ((tuttoOK) ? "YES" : "NO") << endl;
		
	}
	return 0;
}
