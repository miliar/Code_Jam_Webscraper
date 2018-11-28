#include <fstream>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

void Tokenize(vector<string> & tokens, string line)
{
        string token="";
        string oneCharString = " ";
        for (int i=0; i< line.size(); i++)
                if (line[i]==' ')
                {
                        tokens.push_back(token);
                        token="";
                }
                else
                {
                        oneCharString[0] = line[i];
                        token += oneCharString;
                }
        if (token!= "")
                tokens.push_back(token);
}

long long divisor(long long n)
{
    if ((n == 2)||(n==3))
        return -1;
    if (n % 2 == 0)
        return 2;
    if (n % 3 == 0)
        return 3;

    long long  i = 5;
    int w = 2;

    while (i * i <= n)
    {
        if (n % i == 0)
            return i;

        i += w;
        w = 6 - w;
    }

    return -1;
}

long long convert(vector<int> & seq, int radix)
{
	long long N=0;
	int s = seq.size();
	//cout << s << endl;
        /*cout <<" ";
	for(auto itr=seq.cbegin(); itr!=seq.cend(); ++itr)
                cout<<*itr;*/
	long long pr = 1;
	for (int i=0; i<s; i++)
	{
		//cout << s-1-i << ", " << pr <<" --";
		N+=seq[s-1-i]*pr;
		pr = pr* radix;
	}
	//cout << " radix " << radix << ": " << N;// << endl;
	return N;
}

void display(ofstream& outf, vector<int> & v)
{
	for(auto itr=v.cbegin(); itr!=v.cend(); ++itr)
		outf<<*itr;
}

int flip(int x)
{
	if (x==0)
		return 1;
	else
		return 0;
}

void FindCoinJams(int size, int Num, ofstream& outf)
{
	//initializing
	vector<int> seq;
	seq.push_back(1);
	for (int i=1; i<size-1; i++)
		seq.push_back(0);
	seq.push_back(1);

	//display(outf, seq);

	long long divisors[10];
	int ctr=0;
	int attmpt=0;
	long long d = -1;
	while (ctr < Num)
	{
		cout << endl << attmpt << "," <<  ctr << endl;
		for (int r=9; r>0; r--)
		{
			d = divisor(convert(seq, r+1));
			//cout << "divisor: " << d << endl;
			if (d==-1)
				break;
			else
				divisors[r]=d;
		}
		if (d!=-1)
		{
			display(outf, seq);
			for (int i=1; i<10; i++)
				outf << " " << divisors[i] << " ";
			outf << endl;
			ctr++;
		}

		//ctr++;
		int prevbit = seq[size-2];
		seq[size-2] = flip(prevbit);
		for (int b=size-3; b>0; b--)
		{
			if ((prevbit==1)&&(seq[b+1]==0))
			{
				prevbit = seq[b];
				seq[b] = flip(seq[b]);
			}
			else
				break;
		}
		attmpt++;
	}

}


int main(int argc, char** argv)
{
	if (argc!=4)
	{
		//cout << "Params: 0 inputFilePath outputFilePath \n"; 
	}

	ifstream inf;
	inf.open(argv[2]);
	ofstream outf;
	outf.open(argv[3]);

	int n=0;
	string line;
	getline(inf,line);
	n = atoi(line.c_str());
	
	for (int i=0; i<n; i++)
	{
		getline(inf,line);
		vector<string> tokens;
		Tokenize(tokens, line);
		int N = atoi(tokens[0].c_str());
		int J = atoi(tokens[1].c_str());
		outf << "Case #" << i+1 <<": " << endl;
		FindCoinJams(N, J, outf);
	}	

	outf.close();
	inf.close();
}
