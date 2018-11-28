#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
typedef vector<int> vi;

ifstream in("a.in"); ofstream out("a.out");
int T, l=1;

int main()
{
	in>>T;
	while(T--)
	{
		string word, seq;
		int occ[26] = {0}, n;
		in>>word;
		
		for(int i = 0; i< word.size(); i++)
		{
			occ[word[i]-'A']++;
		}
		
		//first stage
		if(occ['Z'-'A']) {n = occ['Z'-'A']; occ['Z'-'A']-=n; occ['E'-'A']-=n;occ['R'-'A']-=n; occ['O'-'A']-=n; for(int j = 0; j<n;j++) seq+='0';}
		if(occ['W'-'A']) {n = occ['W'-'A']; occ['T'-'A']-=n; occ['W'-'A']-=n;occ['O'-'A']-=n; for(int j = 0; j<n;j++) seq+='2';}
		if(occ['U'-'A']) {n = occ['U'-'A']; occ['F'-'A']-=n; occ['O'-'A']-=n;occ['U'-'A']-=n; occ['R'-'A']-=n; for(int j = 0; j<n;j++) seq+='4';}
		if(occ['X'-'A']) {n = occ['X'-'A']; occ['S'-'A']-=n; occ['I'-'A']-=n;occ['X'-'A']-=n; for(int j = 0; j<n;j++) seq+='6';}
		if(occ['G'-'A']) {n = occ['G'-'A']; occ['E'-'A']-=n; occ['I'-'A']-=n;occ['G'-'A']-=n; occ['H'-'A']-=n; occ['T'-'A']-=n; for(int j = 0; j<n;j++) seq+='8';}
		
        //second stage
		if(occ['O'-'A']) {n = occ['O'-'A']; occ['O'-'A']-=n; occ['N'-'A']-=n;occ['E'-'A']-=n; for(int j = 0; j<n;j++) seq+='1';}
		if(occ['R'-'A']) {n = occ['R'-'A']; occ['T'-'A']-=n; occ['H'-'A']-=n;occ['R'-'A']-=n; occ['E'-'A']-=2*n; for(int j = 0; j<n;j++) seq+='3';}
		if(occ['F'-'A']) {n = occ['F'-'A']; occ['F'-'A']-=n; occ['I'-'A']-=n;occ['V'-'A']-=n; occ['E'-'A']-=n; for(int j = 0; j<n;j++) seq+='5';}
		if(occ['S'-'A']) {n = occ['S'-'A']; occ['S'-'A']-=n; occ['E'-'A']-=2*n;occ['V'-'A']-=n; occ['N'-'A']-=n; for(int j = 0; j<n;j++) seq+='7';}

		//third stage
		if(occ['I'-'A']) {n = occ['I'-'A']; for(int j = 0; j<n;j++) seq+='9';}
		
		sort(seq.begin(),seq.end());
		
		out<<"Case #"<<l<<": "<<seq<<endl;
	    l++;
		
	}
}




