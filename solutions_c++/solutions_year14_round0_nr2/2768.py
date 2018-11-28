#include <fstream>
#include <iomanip>

using namespace std;


int main()
{
	int T;
	ifstream cin("B-large.in", ios::in);
	ofstream cout("output.txt",ios::out);
	cin >> T;
	for(int i = 1 ; i<=T;i++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double sans = X/2;
		double avec = C/2 + X/(F+2); 
		int count = 1;
		while(sans > avec)
		{
			sans = avec;
			avec -= X/(count*F+2);
			avec += C/(count*F+2);
			count++;
			avec += X/(count*F+2);
		}
		cout << "Case #" << i << ": ";
		cout <<  fixed << setprecision (7)  << sans << endl;
	}
	cin.close();
	cout.close();
	return 0;
}