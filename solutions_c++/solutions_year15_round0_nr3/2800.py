#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{
	long long int t,n,l,x,f1=0,f2=0,F[10002],B[10002],K[10002],c2=0,c1=0,co=0,i,j;
	int flag=0;
	char tp,tpp;
	ifstream fin;
	fin.open("C-small-attempt1.in");
	ofstream fout;
	fout.open("output.txt");
	string A[120][120],s1,s,s2;
	A['1']['1']=1; A['1']['i']="i"; A['1']['j']="j"; A['1']['k']="k";
	A['i']['1']="i"; A['i']['i']="-1"; A['i']['j']="k"; A['i']['k']="-j";
	A['j']['1']="j"; A['j']['i']="-k"; A['j']['j']="-1"; A['j']['k']="i";
	A['k']['1']="k"; A['k']['i']="j"; A['k']['j']="-i";A['k']['k']="-1";
	//cout<<A['i']['i'];
	fin>>t;
	while(t--)
	{
		co++;
		c1=0;c2=0;
		fin>>l>>x;
		flag=0;
		n=l*x;
		fin>>s2;
		s="";
		for(i=0;i<x;i++)
		{
			//strcat(s,s);
			s=s+s2;
		}
	//	cout<<s<<endl;
	//	cin>>i;
		if(s[0]=='i')
		F[c1++]=0;
		tp=s[0];
		K[0]=-1;
		//cout<<"$"<<tp<<endl;
		for(i=1;i<n;i++)
		{
			s1=A[tp][s[i]];
				if(s1.length()>1)
			{
				f1=1-f1;
			//	cout<<s1;
				tp=s1[1];
			//	cout<<" "<<tp<<endl;
			}
			else
			{
				tp=s1[0];
			//	cout<<" tp1"<<tp<<endl;
			}
			
			if(tp=='i' && f1==0)
			{
				F[c1++]=i;
			//	cout<<"F of"<<c1-1<<F[c1-1]<<"\n";
			}
			if(tp=='k' && f1==0)
			{
				K[i]=i;
			}
			else
			K[i]=-1;
			
		}
		c2=0;
		
		
			//j=n-1;
			//cout<<"$"<<s[n-1]<<endl;
			f1=0;
		if(s[n-1]=='k')
		B[c2++]=n-1;
		tpp=s[n-1];
		for(i=n-2;i>=0;i--)
		{
			s1=A[s[i]][tpp];
				if(s1.length()>1)
				{
					f1=1-f1;
					tpp=s1[1];
			//		cout<<"tpp="<<tpp<<endl;
				}
				else
				{
					tpp=s1[0];
			//		cout<<"tpp1="<<tpp<<endl;
				}
			if(tpp=='k' && f1==0)
			{
				B[c2++]=i;
			//	cout<<"i="<<i<<endl;
			}
			//else
			//B[i]=-1;
		
			//j--;
		}
		//cout<<"c1="<<c1<<endl;
		//cin>>i;
		
		f1=0;
		for(i=0;i<c1;i++)
		{
				for(j=c2-1;j>=0;j--)
				{
					if(F[i]+1<B[j] && K[B[j]-1]!=-1 )
					{
						flag=1;
						break;
					}
				}
		/*	for(j=F[i]+1;j<n;j++)
			{
				if(j==F[i]+1)
				tpp=s[F[i]+1];
				else
				{
						s1=A[tpp][s[j]];
						//cout<<"s1"<<s1<<endl;
					if(s1.length()>1)
					{
						f1=1-f1;
						tpp=s1[1];
						
					}
					else
					{
						tpp=s1[0];
						//cout<<"tpp="<<tpp<<endl;
			     	}
				}
				
					if(tpp=='j' && B[j+1]!=-1 &&f1==0)
					{
						flag=1;
						break;
					}	
				
			}*/
			if(flag==1)
			break;
		
		}
	//	for(i=0;i<c1;i++)
		
		if(flag==1)
		{
			flag=0;
			fout<<"Case #"<<co<<": "<<"YES\n";
		}
		else
		fout<<"Case #"<<co<<": "<<"NO\n";
		
	}
//	cout<<a;
}
