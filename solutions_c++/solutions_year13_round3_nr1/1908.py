#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>

using namespace std;


int g (string s, int N)
{
	int length=s.length();
	int arr[length];
	int ans[length];

	if (s[0]=='a' || s[0]=='e' || s[0]=='i' || s[0]=='o' || s[0]=='u' )
		arr[0]=0;
	else 
		arr[0]=1;

	for (int i=1;i<length;i++)
	{
		if (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' )
			arr[i]=0;
		else 
			arr[i]=arr[i-1]+1;
	}

/*	for (int i=0;i<length;i++)
		cout << arr[i]<< " ";
	cout<< '\n';
*/
	if (N==1 && arr[0]==1)
		ans[0]=1;
	else
		ans[0]=0;

	for (int i=1;i<length;i++)
	{
		if ( arr[i]>=N)
			ans[i]=i+1-N+1;
		else
			ans[i]=ans[i-1];
	}

	int answer=0;
	
	for (int i=0;i<length;i++)
		answer+=ans[i];

	return answer;

}



int main ()
{
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("output.txt","w",stdout);

	int T;
	cin >> T;

	for (int i=0;i<T;i++)
	{
		string s;
		int N;
		cin >> s;
		cin >> N;
		cout << "Case #"<<i+1<<": "<<g(s,N)<<'\n';
	}

	return 0;
}
