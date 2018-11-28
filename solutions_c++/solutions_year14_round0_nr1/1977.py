#include<iostream>
#include<vector>
using namespace std;
vector<int> V , V2;
int main()
{
	int T;
	cin >> T;
	for(int t = 0;t < T;t ++)
	{
		V.clear();
		V2.clear();
		int a;
		cin >> a;
		a --;
		for(int i = 0;i < 4;i ++)
			for(int j = 0;j < 4;j ++)
			{
				int tmp;
				cin >> tmp;
				if(i == a)
					V.push_back(tmp);
			}
		int b;
		cin >> b;
		b --;
		for(int i = 0;i < 4;i ++)
			for(int j = 0;j < 4;j ++)
			{
				int tmp;
				cin >> tmp;
				if(i == b)
				{
					bool e = false;
					for(int k = 0;k < (int)V.size();k ++)
						if(V[k] == tmp)
							e = true;
					if(e)
						V2.push_back(tmp);
				}	
			}
					
		if(V2.size() > 1)
			cout << "Case #" << t + 1 << ": " << "Bad magician!" << endl;
		else if(V2.size() == 1)
			cout << "Case #" << t + 1 << ": " << V2[0] << endl;
		else
			cout << "Case #" << t + 1 << ": " << "Volunteer cheated!" << endl;
	}
	return 0;
}
