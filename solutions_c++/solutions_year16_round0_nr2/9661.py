#include<iostream>
#include<string>
using namespace std;

void flip_c(char str[],int n)
{
	int i=0;
	for(i=0;i<=n;i++)
	{
		if(str[i]=='+')
			str[i]='-';
		else
			str[i]='+';
	}
}
int main()
{
 freopen("B-large.in", "r", stdin);
    freopen("blarge.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
	int T;
	cin>>T;
    char str[1000];
    int i=0,sz=0,j=0;
	int count = 0,end=0;
	int flip=0 ;

	for (i=0;i<T;i++)
	{
		cin.ignore();
		cout.flush();
		scanf("%s",str);
		//printf("%s",str);
		count=0;
		end=0;
		sz  = strlen(str);
		cout.flush();
		while(end!=1)
		{
			flip=0;
			for(j=0;j<sz;j++)
			{
				if(str[j]=='-' &&  str[j+1]=='+')
				{
					flip=1;
					//j++;
					break;
				}
				else if(str[j]=='-')
					flip=1;
			}
			if(flip==1)
			{
				count++;
				flip_c(str,j);
			}
			else
				end=1;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}

