#include <iostream>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int k = 0; k < T; k++)
	{
		string s1,s2,s3,s4, next;
		cin >> s1 >> s2 >> s3 >> s4;
		//cout << s1 << s2 << s3 <<s4;
		//cin >> next;
		/*Horizontal Examination*/
		int i=k+1;
		if(s1[0]==s1[1] && s1[0]==s1[2] && s1[0]==s1[3] && s1[0]!='.')
		{
			cout << "Case #" << i << ": " << s1[0] << " won" << endl;
		}
		else if(s1[1]==s1[2] && s1[1]==s1[3] && s1[0]=='T' && s1[1]!='.')
		{
			cout << "Case #" << i << ": " << s1[1] << " won" << endl;
		}
		else if(s1[0]==s1[1] && s1[0]==s1[2] && s1[3]=='T' && s1[0]!='.')
		{
			cout << "Case #" << i << ": " << s1[0] << " won" << endl;
		}
		else if(s2[0]==s2[1] && s2[0]==s2[2] && s2[0]==s2[3] && s2[0]!='.')
		{
			cout << "Case #" << i << ": " << s2[0] << " won" << endl;
		}
		else if(s2[1]==s2[2] && s2[1]==s2[3] && s2[0]=='T' && s2[1]!='.')
		{
			cout << "Case #" << i << ": " << s2[1] << " won" << endl;
		}
		else if(s2[0]==s2[1] && s2[0]==s2[2] && s2[3]=='T' && s2[0]!='.')
		{
			cout << "Case #" << i << ": " << s2[0] << " won" << endl;
		}
		else if(s3[0]==s3[1] && s3[0]==s3[2] && s3[0]==s3[3] && s3[0]!='.')
		{
			cout << "Case #" << i << ": " << s3[0] << " won" << endl;
		}
		else if(s3[1]==s3[2] && s3[1]==s3[3] && s3[0]=='T' && s3[1]!='.')
		{
			cout << "Case #" << i << ": " << s3[1] << " won" << endl;
		}
		else if(s3[0]==s3[1] && s3[0]==s3[2] && s3[3]=='T' && s3[0]!='.')
		{
			cout << "Case #" << i << ": " << s3[0] << " won" << endl;
		}
		else if(s4[0]==s4[1] && s4[0]==s4[2] && s4[0]==s4[3] && s4[0]!='.')
		{
			cout << "Case #" << i << ": " << s4[0] << " won" << endl;
		}
		else if(s4[1]==s4[2] && s4[1]==s4[3] && s4[0]=='T' && s4[1]!='.')
		{
			cout << "Case #" << i << ": " << s4[1] << " won" << endl;
		}
		else if(s4[0]==s4[1] && s4[0]==s4[2] && s4[3]=='T' && s4[0]!='.')
		{
			cout << "Case #" << i << ": " << s4[0] << " won" << endl;
		}
		/*Vertical Examination*/
		else if(s1[0]==s2[0] && s1[0]==s3[0] && s1[0]==s4[0] && s1[0]!='.')
		{
			cout << "Case #" << i << ": " << s1[0] << " won" << endl;
		}
		else if(s2[0]==s3[0] && s2[0]==s4[0] && s1[0]=='T'&& s2[0]!='.')
		{
			cout << "Case #" << i << ": " << s2[0] << " won" << endl;
		}
		else if(s1[0]==s2[0] && s1[0]==s3[0] && s4[0]=='T' && s1[0]!='.')
		{
			cout << "Case #" << i << ": " << s1[0] << " won" << endl;
		}
		else if(s1[1]==s2[1] && s1[1]==s3[1] &&s1[1]==s4[1]&& s1[1]!='.')
		{
			cout << "Case #" << i << ": " << s1[1] << " won" << endl;
		}
		else if(s2[1]==s3[1] && s2[1]==s4[1] &&s1[1]=='T'&& s2[1]!='.')
		{
			cout << "Case #" << i << ": " << s2[1] << " won" << endl;
		}
		else if(s1[1]==s2[1] && s1[1]==s3[1] &&s4[1]=='T'&& s1[1]!='.')
		{
			cout << "Case #" << i << ": " << s1[1] << " won" << endl;
		}
		else if(s1[2]==s2[2] && s1[2]==s3[2] && s1[2]==s4[2] && s1[2]!='.')
		{
			cout << "Case #" << i << ": " << s1[2] << " won" << endl;
		}
		else if(s2[2]==s3[2] && s2[2]==s4[2] &&s1[2]=='T'&& s2[2]!='.')
		{
			cout << "Case #" << i << ": " << s2[2] << " won" << endl;
		}
		else if(s1[2]==s2[2] && s1[2]==s3[2] && s4[2]=='T' && s1[2]!='.')
		{
			cout << "Case #" << i << ": " << s1[2] << " won" << endl;
		}
		else if(s1[3]==s2[3] && s1[3]==s3[3] && s1[3]==s4[3] && s1[3]!='.')
		{
			cout << "Case #" << i << ": " << s1[3] << " won" << endl;
		}
		else if(s2[3]==s3[3] && s2[3]==s4[3] && s1[3]=='T'&& s2[3]!='.')
		{
			cout << "Case #" << i << ": " << s2[3] << " won" << endl;
		}
		else if(s1[3]==s2[3] && s1[3]==s3[3] && s4[3]=='T' && s1[3]!='.')
		{
			cout << "Case #" << i << ": " << s1[3] << " won" << endl;
		}
		/*Diagonal Examination*/
		else if(s1[0]==s2[1] && s1[0]==s3[2] && s1[0]==s4[3]&& s1[0]!='.')
		{
			cout << "Case #" << i << ": " << s1[0] << " won" << endl;
		}
		else if(s1[3]==s2[2] && s1[3]==s3[1] && s1[3]==s4[0]&& s1[3]!='.')
		{
			cout << "Case #" << i << ": " << s1[3] << " won" << endl;
		}
		else if(s1[0]==s2[1] && s1[0]==s3[2] && s4[3]=='T'&& s1[0]!='.')
		{
			cout << "Case #" << i << ": " << s1[0] << " won" << endl;
		}
		else if(s1[3]==s2[2] && s1[3]==s3[1] && s4[0]=='T'&& s1[3]!='.')
		{
			cout << "Case #" << i << ": " << s1[3] << " won" << endl;
		}
		else if(s2[1]==s3[2] && s2[1]==s4[3] && s1[0]=='T'&& s1[0]!='.')
		{
			cout << "Case #" << i << ": " << s2[1] << " won" << endl;
		}
		else if(s3[2]==s2[1] && s3[2]==s1[0] && s1[3]=='T'&& s1[3]!='.')
		{
			cout << "Case #" << i << ": " << s3[2] << " won" << endl;
		}
		else
		{
			bool isempty = false;
			for(int j = 0; j < 4; j++)
			{
				if(s1[j] == '.')
				{
					isempty=true;
					break;
				}
				if(s2[j] == '.')
				{
					isempty=true;
					break;
				}
				if(s3[j] == '.')
				{
					isempty=true;
					break;
				}
				if(s4[j] == '.')
				{
					isempty=true;
					break;
				}
			}
			if(isempty)
				cout << "Case #" << i << ": Game has not completed" << endl;
			else
				cout << "Case #" << i << ": Draw" << endl;
		}
	}
}
