#include <vector>
#include <iostream>

using namespace std;

class mag
{
public:
	void load_r1()
	{	r1.clear();
		for( int i =0; i < 4; i++)
		{
			vector<int> row;
			for( int j = 0; j < 4; j++)
			{
				int x;
				cin>>x;
				row.push_back(x);
			}
			r1.push_back(row);
		}
	}
	void load_r2()
	{
		r2.clear();
                for( int i =0; i < 4; i++)
                {
                        vector<int> row;
                        for( int j = 0; j < 4; j++)
                        {
                                int x;
                                cin>>x;
                                row.push_back(x);
                        }
                        r2.push_back(row);
                }
        }


	vector< vector< int > > r1; 
	vector< vector< int > > r2;

	bool cheated();

	int solve(int a,int b)
	{
		vector<int> p1 = r1[a];
		vector<int> p2 = r2[b];

		vector<int> choices;
		for(int i =0; i < 4; i++)
		{
			for( int j = 0; j < 4; j++)
				if(p1[i] == p2[j])
					choices.push_back(p1[i]);	
		}

		if(choices.size() == 0)
			return -1;
		if(choices.size() > 1)
			return -2;
		return choices[0];
	}


};

int main()
{
	int ncases;
	cin>>ncases;
	mag prob;
	for(int icases = 0; icases < ncases; icases++)
	{
		int a,b;
		cin>>a;
		prob.load_r1();
		cin>>b;
		prob.load_r2();
		int sol = prob.solve(a-1,b-1);
		if(sol == -2)
			cout<<"Case #"<<icases+1<<": Bad magician!"<<endl;
		else if(sol == -1)
			cout<<"Case #"<<icases+1<<": Volunteer cheated!"<<endl;
		else
			cout<<"Case #"<<icases+1<<": "<<sol<<endl;
	}
}
