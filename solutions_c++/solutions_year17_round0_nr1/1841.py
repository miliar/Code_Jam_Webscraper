//#include <bits/stdc++.h>
 #include <iostream>
 #include <string>
using namespace std;

int checkall(int a[], int x, int l, int m)
{
	int flag = 0;
	for(int i = l;i<m;i++)
	{
		if(a[i] != x)
		{
			flag = 1;
			break;
		}
	}
	if(flag == 1)
		return 0;
	else
		return 1;
}


int main(){
	int t;
	cin>>t;
	int case_no=1;
	while(t--){
		string s;
		int k;
		string ans;
		cin>>s>>k;
		int count = 0;
		int n = s.length();
		int temp[n];
		int flag = 0;
		for(int i=0;i<n;i++)
		{
			if(s[i] == '+')
				temp[i] = 1;
			else
				temp[i] = 0;
		}

		int check_1 = checkall(temp,1,0,n);
		
		if(check_1 == 1)
		{
			ans = ans + "0";
		}
		else
		{
			for(int j = 0;j < n;j++)
			{

				if (n-(j*2) <= k)
				{			
					if(n-(j*2) < k)
					{		
						int check_2 = checkall(temp,1,j,j+k);
						
						if(check_2 == 0)
						{
							flag = 1;
							ans = ans + "IMPOSSIBLE";
							break;
						}
						else
						{
							ans = ans + to_string(count);
							break;
						}
					}
					if(n-(j*2) == k)
					{
						int check_3 = checkall(temp,1,j,j+k);
						if(check_3 == 1)
						{
							ans = ans + to_string(count);
							break;
						}
						else
						{
							int check_4 = checkall(temp,0,j,j+k);
							if(check_4 == 1)
							{
								ans = ans + to_string(count+1);
								break;
							}
							else
							{
								flag = 1;
								ans = ans + "IMPOSSIBLE";
								break;
							}
						}
					}

				}

				if(temp[j] == 0)
				{
					for(int y = j;y<j+k;y++)
					{
						if(temp[y] == 0)
							temp[y] = 1;
						else
							temp[y] = 0;
					}
					count++;
					
				}
				if (temp[n-(j+1)] == 0)
				{
					for(int y = n-j+1;y>n-(j+1+k);y--)
					{
						if (temp[y] == 0)
							temp[y] = 1;
						else
							temp[y] = 0;
					}
					count++;
					
				}
				
			}
		}
		cout<<"Case #"<<case_no<<": "<<ans<<endl;
		case_no++;
	}
	return 0;
}
