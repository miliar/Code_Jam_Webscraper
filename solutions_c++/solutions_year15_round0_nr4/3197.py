#include<bits/stdc++.h>
using namespace std;
int main()
{	

	ios_base::sync_with_stdio(false);
	int test;
	cin>>test;

	for(int case_no=1;case_no<=test;++case_no)
		{
			int x,r,c;
			cin>>x>>r>>c;

			bool can_be_done=false;
			if(x==1)
				can_be_done=1;
			else if(x==2 && r*c%2==0)
				can_be_done=1;
			else if((r*c)%x==0)
			{
				int l=max(r,c),b=min(r,c);
				int total_smaller=min(l/(x),b/(x-1));
				int left_over=r*c-total_smaller*x*(x-1);
				if(total_smaller!=0 && left_over%x==0)
					can_be_done=true;

				total_smaller=min(l/(x-1),b/x);
				left_over=r*c-total_smaller*x*(x-1);
				if(total_smaller!=0 && left_over%x==0)
					can_be_done=true;
			}

			if(can_be_done)
				cout<<"Case #"<<case_no<<": "<<"GABRIEL"<<endl;
			else
				cout<<"Case #"<<case_no<<": "<<"RICHARD"<<endl;
		}
	
return 0;
}
