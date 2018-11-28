#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string process (string input){
	sort(input.begin(),input.end());
	vector<size_t> cntnum(10,0);
	vector<size_t> cntchar(26,0);
	for (size_t i = 0; i < input.size();++i)
		++(cntchar[static_cast<size_t>(input[i]-'A')]);
	{//zero
		cntnum[0]=cntchar['Z'-'A'];
		cntchar['E'-'A']-=cntchar['Z'-'A'];
		cntchar['R'-'A']-=cntchar['Z'-'A'];
		cntchar['O'-'A']-=cntchar['Z'-'A'];
		cntchar['Z'-'A']=0;
	}
	{//two
		cntnum[2]=cntchar['W'-'A'];
		cntchar['T'-'A']-=cntchar['W'-'A'];
		cntchar['O'-'A']-=cntchar['W'-'A'];
		cntchar['W'-'A']=0;
	}
	{//four
		cntnum[4]=cntchar['U'-'A'];
		cntchar['F'-'A']-=cntchar['U'-'A'];
		cntchar['O'-'A']-=cntchar['U'-'A'];
		cntchar['R'-'A']-=cntchar['U'-'A'];
		cntchar['U'-'A']=0;
	}
	{//six
		cntnum[6]=cntchar['X'-'A'];
		cntchar['S'-'A']-=cntchar['X'-'A'];
		cntchar['I'-'A']-=cntchar['X'-'A'];
		cntchar['X'-'A']=0;
	}
	{//eight
		cntnum[8]=cntchar['G'-'A'];
		cntchar['E'-'A']-=cntchar['G'-'A'];
		cntchar['I'-'A']-=cntchar['G'-'A'];
		cntchar['H'-'A']-=cntchar['G'-'A'];
		cntchar['T'-'A']-=cntchar['G'-'A'];
		cntchar['G'-'A']=0;
	}

	{//THREE
		cntnum[3]=cntchar['H'-'A'];
		cntchar['T'-'A']-=cntchar['H'-'A'];
		cntchar['R'-'A']-=cntchar['H'-'A'];
		cntchar['E'-'A']-=2*cntchar['H'-'A'];
		cntchar['H'-'A']=0;
	}	{//FIVE
		cntnum[5]=cntchar['F'-'A'];
		cntchar['I'-'A']-=cntchar['F'-'A'];
		cntchar['E'-'A']-=cntchar['F'-'A'];
		cntchar['V'-'A']-=cntchar['F'-'A'];
		cntchar['F'-'A']=0;
	}	{//SEVEN
		cntnum[7]=cntchar['S'-'A'];
		cntchar['E'-'A']-=2*cntchar['S'-'A'];
		cntchar['V'-'A']-=cntchar['S'-'A'];
		cntchar['N'-'A']-=cntchar['S'-'A'];
		cntchar['S'-'A']=0;
	}

	{//NINE
		cntnum[9]=cntchar['I'-'A'];
		cntchar['N'-'A']-=2*cntchar['I'-'A'];
		cntchar['E'-'A']-=cntchar['I'-'A'];
		cntchar['I'-'A']=0;
	}

	cntnum[1]=cntchar['E'-'A'];
	string result;
	for (size_t i = 0 ; i < 10; ++i)
		for (size_t j = 0 ; j < cntnum[i];++j)
			result.push_back('0'+i);
	return result;
}


int main(int argc, char** argv){
	ifstream ip(argv[1]);
	ofstream op("output.txt");
	size_t T;
	ip >> T;
	string input;
	for (size_t i = 1; i <= T; ++i){
		ip >> input;
		op << "Case #" << i << ": ";
		op << process(input);
		op << endl; 
	}
	op.close();
	ip.close();
	return 0;
}