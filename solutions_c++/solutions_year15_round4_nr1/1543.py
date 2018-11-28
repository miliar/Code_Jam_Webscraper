#include<bits/stdc++.h>
using namespace std;
#define sc(n) scanf("%d",&(n))
#define f(i,k,n) for(int (i)=(k);(i)<(n);(i)++)
#define ll long long
#define pb push_back
#define mp make_pair
#define pa pair<int,int>
#define x first
#define y second
int main()
{
	int t;
	cin>>t;
	f(T,1,(t+1))
	{
		cout<<"Case #"<<T<<": ";
		int R,C;
		cin>>R>>C;
		char s[110][110];
		f(i,0,R)scanf("%s",s[i]);
		/*f(i,0,R)
		f(j,0,C)
		{
			char d=s[i][j];
			if(i==0&&j==0&&d=='^')c++;
			else if(j==0&&d=='<')c++;
			else if(j==C-1&&d=='>')c++;
			else if(i==0&&j==C-1&&d=='^')c++;
			else if(i==R-1&&j==0&&d=='v')c++;
			else if(i==R-1&&j==C-1&&d=='v')c++;
			else if(i==R-1&&d=='v')c++;
			else if(i==0&&d=='^')c++;
		}
		char s1[110][110],s2[110][110];
		f(i,0,R)
                f(j,0,C)
                {
                        char &d=s1[i][j],&e=s2[i][j];
                        if(i==0&&j==0)d='>',e='v';
			 else if(i==0&&j==C-1)d='v',e='<';
                        else if(i==R-1&&j==0)d='^',e='>';
                        else if(i==R-1&&j==C-1)d='<',e='^';
                        else if(j==0)d='^',e='v';
                        else if(j==C-1)d='v',e='^';
                        else if(i==R-1)d='<',e='>';
                        else if(i==0)d='>',e='<';
			else d=s[i][j],e=s[i][j];
                }*/

		int c=0,flag=1;
		
		f(i,0,R)
		f(j,0,C)
		{
			char d=s[i][j];
			if(d=='^')
			{
				int k;
				for(k=i-1;k>=0;k--)
				if(s[k][j]!='.')break;
				if(k<0)
				{
					c++;
					int f=0;
					for(k=i+1;k<R;k++)
					if(s[k][j]!='.')f=1;
					for(k=j+1;k<C;k++)
					if(s[i][k]!='.')f=1;
					for(k=j-1;k>=0;k--)
					if(s[i][k]!='.')f=1;

					if(!f)flag=0;
				}
			}
			else if(d=='>')
                        {
                                int k,f=0;
				for(k=j+1;k<C;k++)
                                        if(s[i][k]!='.')f=1;
                                if(!f)
                                {//cout<<"yes1"<<endl;
                                        c++;
                        		 for(k=i-1;k>=0;k--)
                                	if(s[k][j]!='.')f=1;
                                        for(k=i+1;k<R;k++)
                                        if(s[k][j]!='.')f=1;
                                        for(k=j+1;k<C;k++)
                                        if(s[i][k]!='.')f=1;
                                        for(k=j-1;k>=0;k--)
                                        if(s[i][k]!='.')f=1;

                                        if(!f)flag=0;
                                }
                        }
			else if(d=='v')
                        {//cout<<"here\n";
                                int k,f=0;
                                for(k=i+1;k<R;k++)
                                        if(s[k][j]!='.')f=1;
                                if(!f)
                                {//cout<<"yes2"<<endl;
                                        c++;
                                         for(k=i-1;k>=0;k--)
                                        if(s[k][j]!='.')f=1;
                                        for(k=i+1;k<R;k++)
                                        if(s[k][j]!='.')f=1;
                                        for(k=j+1;k<C;k++)
                                        if(s[i][k]!='.')f=1;
                                        for(k=j-1;k>=0;k--)
                                        if(s[i][k]!='.')f=1;

                                        if(!f)flag=0;
                                }
                        }
			else if(d=='<')
                        {
                                int k,f=0;
                                for(k=j-1;k>=0;k--)
                                        if(s[i][k]!='.')f=1;
                                if(!f)
                                {
                                        c++;
                                         for(k=i-1;k>=0;k--)
                                        if(s[k][j]!='.')f=1;
                                        for(k=i+1;k<R;k++)
                                        if(s[k][j]!='.')f=1;
                                        for(k=j+1;k<C;k++)
                                        if(s[i][k]!='.')f=1;
                                        for(k=j-1;k>=0;k--)
                                        if(s[i][k]!='.')f=1;

                                        if(!f)flag=0;
                                }
                        }

		}
		if(flag)cout<<c<<endl;
		else cout<<"IMPOSSIBLE\n";
	}
	return 0;
}
