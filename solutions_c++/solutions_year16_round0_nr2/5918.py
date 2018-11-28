#include <iostream>
#include <fstream>
#include <string>
#include <cstring>



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
    int i,j;
    string n;
    int cpt=0;
    int test[100];
    char pancake[100];
    for (i = 0; i < numCase; i++)
    {
        fin >> n;
	int a = n.size();
	strcpy(pancake, n.c_str());
	for (j=0; j<a; j++)
	{
		if(pancake[j]=='+') test[j]=1;
		else{ if (pancake[j]=='-') test[j]=0;  }
	}
	bool flag=0;
	cpt=0;
	int marque = 0;
	while (!flag)
	{
		flag=1;		
		for (int k =a-1; k>=0; k--)
		{
			if ( test[k]==0)
			{
				flag=0;
				marque=k;
							}
		}
		if (!flag)
		{
			if (marque==0) cpt++;
			else cpt+=2;
			while (test[marque]==0)
			{
				test[marque]=1;
				marque++;
			}
		}
	}	

        fout << "Case #" << (i + 1) << ": " << cpt << endl;
	
    }
    fin.close();
    fout.close();
    return 0;
}
