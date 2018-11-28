#include <iostream>
#include <map>
#include <fstream>

using namespace std;


int answer_mag(int v1, int arr1[][4], int v2, int arr2[][4])
{
	int answer;//-1 --> Volunteer Cheated -2 --> Bad Magician
	int i;
	map <int, bool> m;
	bool flag = false;
	for(i=0; i<4; i++)
		m[arr1[v1-1][i]] = true;
	for(i=0; i<4; i++)
	{
		if(flag && m[arr2[v2-1][i]])
		{
			answer = -2;
			break;
		}
		else if(m[arr2[v2-1][i]])
		{
			answer = arr2[v2-1][i];
			flag = true;
		}
		
	}
	if(!flag)
		answer = -1;
	
	return answer;	
}


int main()
{
	ifstream in;
	ofstream out;
	int t;
	in.open("A-small-attempt0.in");
	out.open("out.txt");
	int arr1[4][4], arr2[4][4], v1, v2, i, j, answer;
	int count = 1;
	in>>t;
	//cout<<t<<endl;
	while(t--)
	{
		in>>v1;		
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				in>>arr1[i][j];
	//			cout<<arr1[i][j]<<" ";
			}
	//		cout<<endl;
		}
		in>>v2;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				in>>arr2[i][j];
	//			cout<<arr2[i][j]<<" ";
			}	
	//		cout<<endl;
		}
		answer = answer_mag(v1, arr1, v2, arr2);
		if(answer > 0)
			out<<"Case #"<<count<<": "<<answer<<endl;
		else if(answer == -1)
			out<<"Case #"<<count<<": Volunteer cheated!\n";
		else if(answer == -2)
			out<<"Case #"<<count<<": Bad magician!\n";
		count++;
	}
	
	in.close();
	out.close();
	
	
}





