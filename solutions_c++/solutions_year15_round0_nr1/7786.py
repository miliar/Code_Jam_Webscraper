#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <map>
#include <bitset>

using namespace std;

typedef pair<char, char> CPAIR;
typedef pair<int, int> IPAIR;
typedef pair<string, string> SPAIR;

typedef vector<int> IVECTOR;
typedef vector<int>::iterator IVECTOR_ITR;
typedef vector<char> CVECTOR;
typedef vector<float> FVECTOR;
typedef vector<string> SVECTOR;

typedef map<int, int> IIMAP;
typedef map<char, char> CCMAP;
typedef map<int, string> ISMAP;
typedef map<string, string> SSMAP;
typedef map<string, int> SIMAP;


#define FOR(i,a,n) for (int i=a;i<n;i++)
#define FORN(i,a,n) for (int i=n-1;i>=a;i--)


#define FOR1(i,a,n) for (int i=a;i<=n;i++)
#define FOR1N(i,a,n) for (int i=n;i>a;i--)

void printcase(int n, string& mystring)
{
	printf("Case #%d: ", n);
	FOR(i, 0, mystring.size())
	{
		printf("%c", mystring[i]);
	}
	printf("\n");

}


int main(int argv, char* argc[])
{

	freopen("in.txt", "r+", stdin);
	freopen("out.txt", "w+", stdout);

	int t = 0;
	scanf("%d\n", &t);

	FOR(i, 0, t)
	{
		int shy_max = 0;
		scanf("%d ", &shy_max);
		
	    string line;
		getline(cin, line);

		int audi_count = 0;
		int frnds_count = 0;
		FOR(j, 0, shy_max+1)
		{
			char audi_curr = line[j];


			if (j !=0 && audi_count < j)
			{
				frnds_count++;
				audi_count += 1;
			}
			audi_count += audi_curr - '0';
		}
		string output = to_string(frnds_count);
		printcase(i + 1, output);
	}


	fclose(stdin);
	fclose(stdout);
}