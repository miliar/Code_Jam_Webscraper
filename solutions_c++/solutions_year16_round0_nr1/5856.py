#include <iostream>
#include <fstream>



using namespace std;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully 
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;
    int i,n;
    int c;
    for (i = 0; i < numCase; i++)
    {
        fin >> n;
	
	if (n==0)
	{
		fout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
	}
	else
	{
		int j=0,l=0;
		long int k=0;
		int test[10]={0};
	        bool theend= 0;	
		while (theend==0)
		{
			j++;			
			k= j*n;
			cout<<k<<endl;
			int a=0;
			do
			{
				a=k%10;				
				test[a]=1;
				k= k /10;
			}while (k != 0);
			theend=1;
			for ( l=0; l<10;l++)
			{
				if (test[l]==0) theend=0;
			}
			
			
		}
		fout << "Case #" << (i + 1) << ": " << j*n << endl;
	}

        
    }
    fin.close();
    fout.close();
    return 0;
}
