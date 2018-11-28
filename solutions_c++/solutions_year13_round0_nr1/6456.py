

		bool test (char rrr[])
	{
		char rr='\0';
		char r[4];
		r[0]=rrr[0];
		r[1]=rrr[1];
		r[2]=rrr[2];
		r[3]=rrr[3];
		if(r[0]=='T'&&r[1]=='T'&&r[2]=='T'&&r[3]=='T')
			return false;
		else if (r[0]=='.' || r[1]=='.' || r[2]=='.' || r[3]=='.')
			return false;
		else
		{
			for(int i=0;i<4;i++)
			{
				if(r[i]!='T')
				{
					rr=r[i];
					break;
				}
			}
			if(rr!='\0')
			{
				for(int i=0;i<4;i++)
				{
					if(r[i]=='T')
						r[i]=rr;
				}
				for(int i=0; i<3;i++)
				{
					if(r[i]!=r[i+1])
						return false;
				}
			}
			return true;


		}
	}

	bool test2(char r[])
	{
		if (r[0]=='.' || r[1]=='.' || r[2]=='.' || r[3]=='.')
			return true;
		return false;
	}


#include <iostream>
	using namespace std;
	int main()
	{
		int T,A=0;
		int B=0;
		cin>>T;
		char arr[4][4]={0,};
		char varr[4]={0,};
		char r[4]={'.','.','.','.'};
		char rr='\0';

		for(int A=1;A<=T;A++)
		{

			for(int i=0;i<4;i++)
				for(int j=0; j<4; j++)
					cin>>arr[i][j];
			for(int i=0;i<4;i++)
			{
				if(test(arr[i]))
				{
					for(int j=0; j<4; j++)
					{
						if(arr[i][j]!='T')
							rr=arr[i][j];
					}
					cout<<"Case #"<<A<<": "<<rr<<" won"<<endl;
					B=1;
					break;
				}
			}
			if(B==0)
			{

				for(int i=0;i<4;i++)
				{
					for(int j=0;j<4;j++)
					{
						varr[j]=arr[j][i];
					}
					if(test(varr))
					{
						for(int j=0; j<4; j++)
						{
							if(varr[j]!='T')
								rr=varr[j];
						}
						cout<<"Case #"<<A<<": "<<rr<<" won"<<endl;
						B=1;
						break;
					}
				}
			}
			if(B==0)
			{

				varr[0]=arr[0][0];
				varr[1]=arr[1][1];
				varr[2]=arr[2][2];
				varr[3]=arr[3][3];
				if(test(varr))
				{
					for(int j=0; j<4; j++)
					{
						if(varr[j]!='T')
							rr=varr[j];
					}
					cout<<"Case #"<<A<<": "<<rr<<" won"<<endl;
					B=1;
				}
			}
			if(B==0)
			{

				varr[0]=arr[0][3];
				varr[1]=arr[1][2];
				varr[2]=arr[2][1];
				varr[3]=arr[3][0];
				if(test(varr))
				{
					for(int j=0; j<4; j++)
					{
						if(varr[j]!='T')
							rr=varr[j];
					}
					cout<<"Case #"<<A<<": "<<rr<<" won"<<endl;
					B=1;
				}
			}

			if(B==0)
			{
				for(int i=0;i<4;i++)
				{
					if(test2(arr[i]))
					{
						cout<<"Case #"<<A<<": Game has not completed"<<endl;
						B=1;
						break;
					}
				}
			}
			if(B==0)
			{
				cout<<"Case #"<<A<<": Draw"<<endl;
			}
			B=0;
		}

	}