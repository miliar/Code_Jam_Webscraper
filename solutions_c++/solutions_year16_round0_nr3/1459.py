#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int T, i, j, k, l;
	cin>>T;
	int N, J;
	string p="3 4 5 6 7 8 9 10 11\n";
	while(T--)
	{
		cin>>N>>J;
		cout<<"Case #1:\n";
		if(N==32)
		{
			string t="";
			t+='1';
			for(i=1; i<=30; ++i)
				t+='0';
			t+='1';
			int cnt=1;
			cout<<t<<" "<<p;
			for(i=1; i<=30; ++i)
			{
				for(j=i+1; j<=30; ++j)
				{
					for(k=j+1; k<=30; ++k)
					{
						for(l=k+1; l<=30; ++l)
						{
							if((i%2==0 && j%2==1 && k%2==0 && l%2==1) || (i%2==1 && j%2==0 && k%2==1 && l%2==0) || (i%2==0 && j%2==1 && k%2==1 && l%2==0) || (i%2==1 && j%2==0 && k%2==0 && l%2==1)|| (i%2==1 && j%2==1 && k%2==0 && l%2==0) || (i%2==0 && j%2==0 && k%2==1 && l%2==1))
							{
								cnt++;
								t[i]=t[j]=t[k]=t[l]='1';
								cout<<t<<" "<<p;
								t[i]=t[j]=t[k]=t[l]='0';
							}
							if(cnt==J)	break;
						}
						if(cnt==J)	break;
					}
					if(cnt==J)	break;
				}
				if(cnt==J)	break;
			}
			
			//cout<<cnt<<endl;
			continue;
		}
	}
	return 0;
}