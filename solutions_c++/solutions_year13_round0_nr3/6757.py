#include <iostream> 
#include <vector>
#include <fstream>
using namespace std;  
int main() 
{ 
	long long int all[] = {1LL, 4LL, 9LL, 121LL, 484LL, 10201LL, 12321LL, 
						14641LL, 40804LL, 44944LL, 1002001LL, 1234321LL, 
						4008004LL, 100020001LL, 102030201LL, 104060401LL, 
						121242121LL, 123454321LL, 125686521LL, 
						400080004LL, 404090404LL, 10000200001LL, 
						10221412201LL, 12102420121LL, 12345654321LL, 
						40000800004LL, 1000002000001LL, 1002003002001LL, 
						1004006004001LL, 1020304030201LL, 1022325232201LL, 
						1024348434201LL, 1210024200121LL, 1212225222121LL, 
						1214428244121LL, 1232346432321LL, 1234567654321LL, 
						4000008000004LL, 4004009004004LL};
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");
	int N; //number of cases
	input >> N;
	
	for (int i = 1; i<=N; i++)
	{
		long long int a, b;
		input >> a; 
		input >> b;
		
		int indexa = 0;
		while ( (indexa<40) && (all[indexa] < a))
			indexa++;
		
		int indexb = indexa;
		while ( (indexb<40) && (all[indexb] <= b))
			indexb++;
		
		//if indexa == indexb that means we didn't include any;
		
		output << "Case #" << i << ": " << (indexb-indexa) << endl;
	}
		
		
	return 0;

}

/*The commented code here was used to pregenerate the list*/
/*
vector<int> GetDigits(long long int i)
{
    vector<int> Digits;
    while (i > 0)
    {
        Digits.push_back(i%10LL);
        i = i/10LL;
    }
    return Digits;
}

void PrintDigits(const vector<int> &D)
{
    for(int i=0; i<D.size(); i++)
    {
        cout << D[i] << " ";
    }
    cout << endl;
}

bool isFair(long long int i)
{
    vector<int> Digits = GetDigits(i);
    for (int i =0; i<(Digits.size()/2); i++)
    {
        if (Digits[i] != Digits[Digits.size()-i-1])
            return false;
    }
    return true;
}


int main()
{
    cout << "{";
    for (long long int i = 1LL; i < 10000000LL; i++)
    {
        if (isFair(i) && isFair(i*i))
            cout << i*i << "LL," << endl;
    }
    cout << "}";

    return 0;
}
*/
