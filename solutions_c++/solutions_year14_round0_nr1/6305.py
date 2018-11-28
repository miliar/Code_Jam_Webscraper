#include <iostream>
using namespace std;

int main() {

int t;
cin >> t;

for(int i1 =0; i1<t; i1++)
{
	//std::ios_base::sync_with_stdio(false);
	int ans,temp0,temp1,temp2,temp3,temp4;
	cin >> ans;
	ans --;
	
	for(int i2=0;i2<4;i2++)
	{
		if(i2 == ans)
			cin >> temp1 >> temp2 >> temp3 >> temp4;
		else
			cin >> temp0 >> temp0 >> temp0 >> temp0;
	}
	
	
	cin >> ans;
	ans --;
	
	int match = -1;	//-2 = bad job, -1 = vounteer cheated, otherwise
	
	for(int i2=0;i2<16;i2++)
	{
		cin >> temp0;
		if(i2 / 4 == ans)
		{
			if(temp0 == temp1 || temp0 == temp2 || temp0 == temp3 || temp0 == temp4)
			{
				if(match == -1)
					match = temp0;
				else if(match != -2)
					match = -2;
				
			}
		}
	}
	
	
	if(match == -2)
		cout << "Case #"<<i1+1<<": Bad magician!\n";
	else if(match == -1)
		cout << "Case #"<<i1+1<<": Volunteer cheated!\n";
	else
		cout << "Case #"<<i1+1<<": "<<match<<endl;
	
	
}

return 0;
}
