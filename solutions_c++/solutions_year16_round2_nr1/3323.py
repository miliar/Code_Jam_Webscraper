#include<iostream>
#include<string>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int flag[15];

		for (int j=0;j<15;j++)
			flag[j]=0;

		string S,ans;
		ans.clear();
		S.clear();
		//memset(S,'\0',2001);
		cin>>S;
		
		std::sort(S.begin(),S.end());
//		cout<<S;
		int len=S.length();
	
		for(int j=0;j<len;j++)
		{
			switch(S.at(j))
			{
				case 'E':flag[0]++;
					break;
				case 'F':flag[1]++;
					break;
				case 'G':flag[2]++;
					break;
				case 'H':flag[3]++;
					break;
				case 'I':flag[4]++;
					break;
				case 'N':flag[5]++;
					break;
				case 'O':flag[6]++;
					break;
				case 'R':flag[7]++;
					break;
				case 'S':flag[8]++;
					break;
				case 'T':flag[9]++;
					break;
				case 'U':flag[10]++;
					break;
				case 'V':flag[11]++;
					break;
				case 'W':flag[12]++;
					break;
				case 'X':flag[13]++;
					break;
				case 'Z':flag[14]++;
					break;

					
			}
		}
		cout<<"Case #"<<i+1<<": ";

		while((flag[2]>0)&&(flag[0]>0)&&(flag[4]>0)&&(flag[3]>0)&&(flag[9]>0))
		{
			flag[0]--;
			flag[4]--;
			flag[2]--;
			flag[3]--;flag[9]--;
			ans=ans+"8";
		}

		while((flag[14]>0)&&(flag[0]>0)&&(flag[7]>0)&&(flag[6]>0))
		{
			flag[14]--;
			flag[0]--;
			flag[7]--;
			flag[6]--;
			ans=ans+"0";
		}

		while((flag[10]>0)&&(flag[1]>0)&&(flag[6]>0)&&(flag[7]>0))
		{
			flag[1]--;
			flag[6]--;
			flag[10]--;
			flag[7]--;
			ans=ans+"4";
		}
		while((flag[12]>0)&&(flag[9]>0)&&(flag[6]>0))
		{
			flag[9]--;
			flag[12]--;
			flag[6]--;
			ans=ans+"2";
		}


		while((flag[13]>0)&&(flag[8]>0)&&(flag[4]>0))
		{
			flag[8]--;
			flag[4]--;
			flag[13]--;
			ans=ans+"6";
		}

		while((flag[9]>0)&&(flag[3]>0)&&(flag[7]>0)&&(flag[0]>1))
		{
			flag[9]--;
			flag[3]--;
			flag[7]--;
			flag[0]--;flag[0]--;
			ans=ans+"3";
		}

		while((flag[8]>0)&&(flag[11]>0)&&(flag[5]>0)&&(flag[0]>1))
		{
			flag[8]--;
			flag[11]--;
			flag[5]--;
			flag[0]--;flag[0]--;
			ans=ans+"7";
		}



		while((flag[1]>0)&&(flag[4]>0)&&(flag[11]>0)&&(flag[0]>0))
		{
			flag[1]--;
			flag[4]--;
			flag[11]--;
			flag[0]--;
			ans=ans+"5";
		}

		while((flag[5]>1)&&(flag[4]>0)&&(flag[0]>0))
		{
			flag[5]--;
			flag[4]--;
			flag[5]--;
			flag[0]--;
			ans=ans+"9";
		}
		while((flag[6]>0)&&(flag[5]>0)&&(flag[0]>0))
		{
			flag[6]--;
			flag[5]--;
			flag[0]--;
			ans=ans+"1";
		}
		

		std::sort(ans.begin(),ans.end());

		cout<<ans<<endl;		
	}
}
