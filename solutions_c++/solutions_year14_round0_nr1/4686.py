#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>

using namespace std;

int main()
{
	int T,cas=1;
	cin >> T;
	while(T--)
	{
	    cout << "Case #" << cas <<": ";
	    cas++;
	    int a,b;
	    vector<int> v1(16),v2(16);
	    cin >> a;
	    a--;
	    for(int i=0;i<16;i++)
		cin >> v1[i];
	    cin >> b;
	    b--;
	    for(int i=0;i<16;i++)
		cin >> v2[i];
	    int count = 0,r=-1;
	    for(int i=0;i<4;i++)
	    {
		for(int j=0;j<4;j++)
		{
		     if(v1[(a*4)+i] == v2[(b*4)+j])
		     {
			r = v1[(a*4)+i];
		 	count++;
                     }
		}
	    }
	    if(count == 1)
		cout << r << endl;
	    else if(count > 1)
		cout << "Bad magician!\n";
	    else if(count == 0)
		cout << "Volunteer cheated!\n";
	}
       return 0;
}
