#include<cstdio>
#include<iostream>
using namespace std;

int main()
{	int t;
	cin>>t;
	for ( int l=1; l<=t; l++ )
	{	int orig, nw, tmp;
		cin>>orig;
		int orig_pos[17], new_pos[17];
		for ( int i=1; i<=4; i++ )
			for ( int j=1; j<=4; j++ )
			{	cin>>tmp;
				orig_pos[tmp]=i;
			}
		cin>>nw;
		for ( int i=1; i<=4; i++ )
			for ( int j=1; j<=4; j++ )
			{	cin>>tmp;
				new_pos[tmp]=i;
			}
		bool mark[17]={0};
		for ( int i=1; i<=16; i++ )
			if ( orig_pos[i] == orig )
				mark[i]=1;
		int count=0;
		for ( int i=1; i<=16; i++ )
		{	if ( new_pos[i] == nw && mark[i] == 1 )
			{	count++;
				tmp=i;
			}
		}
		if ( count == 1 )
			cout<<"Case #"<<l<<": "<<tmp<<endl;
		else if ( count > 1 )
			cout<<"Case #"<<l<<": Bad magician!"<<endl;			// count > 1 -> bad magician
		else if ( count == 0 )
			cout<<"Case #"<<l<<": Volunteer cheated!"<<endl;
	}
	return 0;
}
