#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define N 102
int n;
char car[N][N];
bool used [N];
bool chused[256];

int ii;
int idx[N];

int pc = 0;
int c = 0;

char bstr[N*N];
void recurs(int starti) {
	///cout<<"["<<starti<<"]\n";
	
	if(ii == n) {
		bstr[0]=0;
		for(int i = 0; i < n; ++i) {
			//cout<<idx[i]<<" ";
			strcat(bstr,car[idx[i]]);
		}
		
		int len = strlen(bstr);
		
		//cout<<bstr;
		memset(chused,0,sizeof(bool)*256);
		for(int i = 0 ; i < len;)
		{
			if(chused[bstr[i]]) {
				//cout<<endl;
				return ;
			}
			
			chused[bstr[i]] = true;
			char ch = bstr[i];
			
			while(ch == bstr[i]) i++;
			
		}
		//cout<<"TRUE\n";
		pc++;
	}
	else {
		for(int i = 0; i < n; ++i) {
			
			if(!used[i])
			{
				//cout<<car[starti]<<" "<<car[i]<<endl;
					//cout<<"*";
					//cout<<">>>"<<car[starti]<<" "<<car[i]<<endl;
					used[i] = true;
					idx[ii] = i;
					ii++;
					recurs(i);
					ii--;
					used[i] = false;
					//cout<<"<<<"<<car[starti]<<" "<<car[i]<<endl;
				
			}
		}

	}
	
	
}

int main() 
{
	int t;
	
	cin>>t;
	for(int ti = 1; ti <= t; ++ti) 
	{
		cout<<"Case #"<<ti<<": ";
		
		cin>>n;
		
		for(int i = 0 ; i < n; ++i) 
		{
			cin>>car[i];
			int len = strlen(car[i]);
			//car[i][1] = car[i][len-1];
			//car[i][2] = 0;
			
			//cout<<car[i]<<" ";
		}
		//cout<<endl;
		pc = 0;
		memset(used,0,sizeof(bool)*N);
		memset(chused,0,sizeof(bool)*256);
		
		ii = 0;
		for(int i = 0; i < n; ++i)
		{
			//cout<<"\n-"<<i<<"-\n";
			used[i] = true;

			idx[ii]=i;
			ii++;
			recurs(i);
			--ii;
			used[i] = false;
		}
		
		
		cout<<pc<<endl;
	}
}
