#include <iostream>

using namespace std;
int width = 0;
int height = 0;
int column_max[100];
int row_max[100];
int lawn[10000];
void initialize()
{
	memset(column_max,0,100*sizeof(int));
	memset(row_max,0,100*sizeof(int));

};
bool fillup()
{
	bool result = true;
	//int ij=0;
	for (int i=0;i<height;++i)
	{
		for (int j = 0; j < width ; ++j)
		{  
		
			cin>>lawn[i*width+j];

			/*if (result && i!=0 && j!=0 && (lawn[i*width+j]<lawn[i*width] && lawn[i*width+j]<lawn[j]))
			{
				result= false;
			}*/
			if (lawn[i*width+j]>column_max[j])
			{
				column_max[j] = lawn[i*width+j];
			}
			row_max[i] = (lawn[i*width+j]>row_max[i])? lawn[i*width+j] : row_max[i];
		}
	}
	for (int i = 0; i < height ; ++i)
	{                                      
		for (int j = 0; j < width ; ++j)
		{                                      
			if (lawn[i*width+j]<column_max[j] && lawn[i*width+j]<row_max[i])
			{ 
				//result =false;
				return false;
			}
		}
	}
	return result;
}
void solve_case(int test_case)
{
	
	cin>>height>>width;
	initialize();
	bool result = fillup();
	if (result)
	{
		cout<<"Case #"<<test_case<<": "<<"YES"<<endl;
	} 
	else
	{
		cout<<"Case #"<<test_case<<": "<<"NO"<<endl;
	}

};

int main()
{
	freopen("Blarge.in","r",stdin);
	freopen("Blarge.out","w",stdout);
	initialize();
	int T; scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}