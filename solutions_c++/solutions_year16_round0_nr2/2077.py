#include <iostream>
#include <string>

using namespace std;



int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		string S;
		cin>>S;
		char tab[100];
		tab[0]=S[0];
		int j=1;
		for(int i=1; i<S.length(); ++i)
		{
			if(S[i]==tab[j-1]){
				continue;
			}
			tab[j++]=S[i];
		}
		if(j==1 && tab[0]=='+'){
			cout<<"Case #"<<t+1<<": "<<0<<"\n";
			continue;
		}



		int wyn = 0;
		int len = j;
		if(tab[j-1]=='+')
			len--;
		


		wyn+=len;
		cout<<"Case #"<<t+1<<": "<<wyn<<"\n";
	}
	return 0;
}