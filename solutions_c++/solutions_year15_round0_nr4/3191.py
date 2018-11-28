#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T, tc = 1;
	int X, R, C;
	string ans;
	
	cin >> T;
	while(tc <= T)
	{
		cin >> X >> R >> C;
			
		if (R > C)
		{
			int temp = R;
			R = C;
			C = temp;
		}
		
		if (X == 1)
			ans = "GABRIEL";
		else if (X == 2)
		{
			if(R%2 == 0 || C%2 == 0)
				ans = "GABRIEL";
			else
				ans = "RICHARD";
		}
		else if (X == 3)
		{
			if (R*C < 3 || (R*C)%3 != 0) //tira 1x1, 1x2, 1x4, 2x2, 2x4, 4x4 (falta 1x3, 2x3, 3x3, 3x4)
				ans = "RICHARD";
			else
			{
				if (R == 1 && C == 3)
					ans = "RICHARD";
				else if(R == 2 && C == 3)
					ans = "GABRIEL";
				else if (R == 3 && C == 3)
					ans = "GABRIEL";
				else if (R == 3 && C == 4)
					ans = "GABRIEL";
			}
		}
		else if (X == 4)
		{
			if (R*C < 4 || (R*C)%4 != 0) //tira 1x1, 1x2, 1x3, 2x3, 3x3 (falta 1x4, 2x2, 2x4, 3x4, 4x4)
				ans = "RICHARD";
			else
			{
				if (R == 1 && C == 4)
					ans = "RICHARD";
				else if (R == 2 && C == 2)
					ans = "RICHARD";
				else if (R == 2 && C == 4)
					ans = "RICHARD";
				else if (R == 3 && C == 4)
					ans = "GABRIEL";
				else if (R == 4 && C == 4)
					ans = "GABRIEL";
			} 
		}
			
			//1x1, 1x2, 1x3, 1x4
			//2x2, 2x3, 2x4
			//3x3, 3x4
			//4x4
			cout << "Case #" << tc << ": " << ans << '\n';
			tc++;
	}
	return 0;
}
