using namespace std;
#include <fstream>
#include <string>

int main()
{
	ifstream in;
	ofstream out;
	int T;
	int r1;
	int r2;
	int count;
	string gar;
	int a1[4];
	int a2[4];
	in.open("c:\\Users\\Mohammed\\Desktop\\GoogleCode\\A-small-attempt0.in");
	out.open("c:\\Users\\Mohammed\\Desktop\\GoogleCode\\output.txt", ios::out);
	getline(in, gar);
	T = stoi(gar);
	for(int k = 0; k < T; k++)
	{
		count  = 0;
		getline(in, gar);
		r1 = stoi(gar);
		for(int i = 0; i<r1-1; i++)
			getline(in, gar);
		for(int i = 0; i <3; i++)
			in >> a1[i];
		getline(in, gar);
		a1[3] = stoi(gar);
		for(int i = 0; i < 4-r1; i++)
			getline(in, gar);
		///////////
		getline(in, gar);
		r2 = stoi(gar);
		for(int i = 0; i<r2-1; i++)
			getline(in, gar);
		for(int i = 0; i <3; i++)
			in >> a2[i];
		getline(in, gar);
		a2[3] = stoi(gar);
		for(int i = 0; i < 4-r2; i++)
			getline(in, gar);
		for(int i = 0; i<4; i++)
		{
			for(int j = 0; j <4; j++)
				if(a1[i] == a2[j])
				{ count++; r1 = a1[i]; }
		}		
		if(count == 1)
		{ out << "Case #" << k+1 <<": " << r1 << endl; }
		if(count == 0)
		{ out << "Case #" << k+1 <<": Volunteer cheated!" << endl; }
		if(count > 1)
		{ out << "Case #" << k+1 <<": Bad magician!" <<endl; }
	}
	out.close();
	in.close();
}
	