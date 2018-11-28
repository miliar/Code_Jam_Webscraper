#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

bool isPal(vector<int> num)
{
	int s=num.size();
	for(int i=0;i<s/2;i++)
	{
		if(num[i]!=num[s-i-1])
		{
			return false;
		}
	}
	return true;
}

vector<int> square(vector<int> num)
{
	int len=num.size();
	int rip=0;
	vector<int> ris (2*len);
	for(int i=0;i<2*len;i++)
	{
		ris[i]=0;
	}
	
	for(int i=0;i<len;i++)
	{
		for(int j=0;j<len;j++)
		{	
			ris[2*len-(i+j)-1]+=num[i]*num[j];
		}
	}
	
	rip=0;
	for(int i=(2*len)-1;i>=0;i--)
	{
		ris[i]+=rip;
		if(ris[i]>9)
		{
			int resto=ris[i]%10;
			rip=ris[i]/10;
			ris[i]=resto;
		}
	}
	if(ris[0]==0)
	{
		ris.erase(ris.begin());
	}
	return ris;
}

int cmp(vector<int > n1, vector<int> n2)
{
	int len1=n1.size(),len2=n2.size();
	if(len1>len2)
	{
		return -1;
	}
	if(len2>len1)
	{
		return 1;
	}
	for(int i=0;i<len1;i++)
	{
		if(n1[i]>n2[i])
		{
			return -1;
		}
		if(n1[i]<n2[i])
		{
			return 1;
		}
	}
	return 0;
}

vector<int> next(vector<int> n)
{
	int last=n.size()-1;
	for(int i=last/2;i>=0;i--)
	{
		if(n[i]<9)
		{
			n[i]++;
			if(i!=last/2 || last%2!=0)
			{
				n[last-i]++;
			}
			break;
		}
		else
		{
			n[i]=0;
			n[last-i]=0;
			if(i==0)
			{
				n.insert(n.begin(),1);
				n[n.size()-1]=1;
			}
		}
	}
	return n;
}

int main()
{
	int n_case;
	char c;
	cin>>n_case;
	c=cin.get();
	for(int i=0;i<n_case;i++)
	{
		bool first=true;
		int n_cif=0;
		vector<int> start (0);
		vector<int> end (0);
		do
		{
			c=cin.get();
			if(first)
			{
				if(c!=' ')
				{
					start.push_back(c-48);
					n_cif++;
				}
				else
				{
					first=false;
				}
			}
			else
			{
				if(c>=48 && c<=57)
				{
					end.push_back(c-48);
				}
			}
		}
		while(c!='\n');
		
		
		/*for(int j=0;j<start.size();j++)
		{
			cout<<start[j]<<" ";
		}
		cout<<endl;
		for(int j=0;j<end.size();j++)
		{
			cout<<end[j]<<" ";
		}
		cout<<endl;*/
		
		int lun=(n_cif+1)/2;
		
		vector<int> n (lun);
		
		for(int j=0;j<lun;j++)
		{
			n[j]=0;
		}
		n[0]=1;
		n[lun-1]=1;
		
		/*for(int j=0;j<lun;j++)
		{
			cout<<n[j]<<" ";
		}
		cout<<endl;*/
		
		vector<int> sq=square(n);
		int cont=0;
		
	
		while(cmp(sq,end)!=-1)
		{
			if((isPal(sq)) && (cmp(start,sq)!=-1))
			{
				/*for(int j=0;j<sq.size();j++)
				{
					cout<<sq[j]<<" ";
				}
				cout<<endl;*/
				cont++;
			}
			n=next(n);
			/*for(int j=0;j<n.size();j++)
			{
				cout<<n[j]<<" ";
			}
			cout<<endl;*/
			//sq.clear();
			sq=square(n);
			/*for(int j=0;j<sq.size();j++)
			{
				cout<<sq[j]<<" ";
			}
			cout<<endl;*/
		}
		
		cout<<"Case #"<<i+1<<": "<<cont<<endl;
		/*start.clear();
		end.clear();
		n.clear();*/
	}
}


