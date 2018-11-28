#include <fstream>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    ofstream output;
    ifstream input ("B-small-attempt0.in");
    output.open("B-small-attempt0.out");

    int t, n, m;

	int lawn[100][100];
    
    input >> t;


	for (int i=0; i<t; i++)
	{
		bool ok = true;

        output << "Case #"<<i+1<<": ";
		input >> n >> m;

		for (int j=0; j<n; j++)
		{
			for(int k=0; k<m; k++)
			{
				input >> lawn[j][k];
			}
		}

		for (int j=0; j<n; j++)
		{
			for(int k=0; k<m; k++)
			{
				int l;
				//x direction
				for (l=0; l<m; l++)
				{
					if (lawn[j][l] > lawn[j][k])
						break;
				}
				
				if (l == m)
					continue;

				//y direction
				for (l=0; l<n; l++)
				{
					if (lawn[l][k] > lawn[j][k])
						break;
				}
			
				if(l==n)
					continue;

				ok = false;
				goto end;
			}
		}
end:
		if (ok)
			output<<"YES";
		else
			output<<"NO";
		output <<endl;
	}

	return 0;
}

