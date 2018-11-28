#include <iostream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int case_id=0;case_id<T;case_id++)
	{
		string S;
		cin>>S;
		int length=S.length();

		int array[26];
		for (int i=0;i<26;i++)
			array[i]=0;

		for (int i=0;i<length;i++)
			array[S[i]-'A']++;

		int ans[10];
		ans[0]=array['Z'-'A'];
		ans[2]=array['W'-'A'];
		ans[4]=array['U'-'A'];
		ans[6]=array['X'-'A'];
		ans[8]=array['G'-'A'];

		ans[3]=array['H'-'A']-ans[8];
		ans[5]=array['F'-'A']-ans[4];
		ans[7]=array['S'-'A']-ans[6];
		ans[1]=array['O'-'A']-ans[0]-ans[2]-ans[4];
		ans[9]=array['I'-'A']-ans[5]-ans[6]-ans[8];


	
		cout<<"Case #"<<case_id+1<<": ";
		for(int i=0;i<10;i++)
			for (int j=0;j<ans[i];j++)
				cout<<i;
			cout<<endl;			
	}
	return 0;	
}