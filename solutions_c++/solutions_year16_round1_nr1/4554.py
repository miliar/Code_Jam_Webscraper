#include<iostream>
#include<cstring>
using namespace std;
 

int main(void)
{
	int t,i,j,k;
	char s[15],ans[40];
	int n =1;
	cin>>t;
	while(t--)
	{
		cin>>s;
		char prev = s[0];
		ans[20] = s[0];
		for(i = 19,j=21,k=1;k<strlen(s);k++)
		{
			//cout<<s[k]<<"  ";
			if(s[k]>=prev){
				ans[i--] = prev = s[k];

			}
			else ans[j++]  = s[k];
			
		}
		//cout<<"\n"<<i<<"   "<<j;
		i++;
		j--;
		cout<<"Case #"<<n++<<": "; 
		for(int m = i;m<=j;m++)
		{
			cout<<ans[m];
		}
		cout<<endl;
	}

	return 0;
}