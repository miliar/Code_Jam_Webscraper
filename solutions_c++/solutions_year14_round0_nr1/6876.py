#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;


int main() {

	int t = 0, v=0, temp, occurance, num, gar;
	cin >> t;
	int grid[4];

	for (int i = 0; i<t; i++)
	{
			num=0; temp=0;
			occurance=0;
			cin >> v;
			
			for (int j=0; j<(v-1)*4; j++) cin>>gar;
			
			for (int j=0; j<4; j++) 
			{
				cin>>grid[j];
			}
			
			for (int j=0; j<(4-v)*4; j++) cin>>gar;
			
			cin >> v;
			
				for (int j=0; j<(v-1)*4; j++) cin>>gar;

				for (int k=0; k<4; k++)
				{
					cin>>temp;
					cout<<temp<<endl;
					if (temp == grid[k])
					{
						occurance++;
						num = temp;
					}
				}
			
			for (int j=0; j<(4-v)*4; j++) cin>>gar;
			
			
			
			
			
			
			
			cout << "Case #";
			cout << i + 1;
			cout << ": ";
			
			if (occurance == 0 )
			{
			cout << "Volunteer cheated!" << endl;
			}
			else if (occurance > 1)
			{
			cout << "Bad magician!" << endl;
			}
			else
			{
			cout << num << endl;
			}

			
		/*out << "Case #";
		out << i + 1;
		out << ": ";
		out << std::fixed;
		out << std::setprecision(7);
		out << time << endl;*/
		
	}//end_for

	//in.close();
	//out.close();
	return 0;
}
