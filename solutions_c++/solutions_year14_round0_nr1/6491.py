# include <iostream>
# include <vector>
using namespace std;

vector <int> f(int *a,int *b)
{
	vector <int> v;
	int i,j;
	for (i=1;i<=4;i++)
	for (j=1;j<=4;j++)
	{
		if (a[i] == b[j])
		v.push_back(a[i]);
	}
	return v;
}

int main()
{
	int k,l;
	cin >> k;
	int list[k];
	for (l=1;l<=k;l++)
	{
	int n,i,j,m;
	int array[4][4],b[4][4];
	cin >> n;
	for (i=1;i<=4;i++)
		for (j=1;j<=4;j++)
			cin >> array[i][j];
	cin >> m;
	for (i=1;i<=4;i++)
		for (j=1;j<=4;j++)
			cin >> b[i][j];
	if (f(array[n],b[m]).size() == 1)
		list[l] = f(array[n],b[m])[0];
	if (f(array[n],b[m]).size() == 0)
		list[l] = 123456789;
	if (f(array[n],b[m]).size() > 1)
		list[l] = 987654321;
	}
	for (l=1;l<=k;l++)
	{
		if (list[l] == 123456789)
			cout << "Case #" << l << ":  " << "Volunteer cheated!" << endl;
		else if (list[l] == 987654321)
			cout << "Case #" << l << ":  " << "Bad magician!" << endl;
		else 
			cout << "Case #" << l << ":  " << list[l] << endl;
	}
}	
		
